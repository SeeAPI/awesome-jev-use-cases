"""Load independently editable bilingual cases; never fetch or execute sources."""
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {'en': 'docs/casebook.md', 'zh': 'docs/casebook.zh-CN.md'}


def settings():
    return json.loads((ROOT / 'data/site.json').read_text())


def slug(text):
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


def body_hash(body):
    normalized = body.replace('(../', '(').replace('src="../', 'src="').strip()
    return hashlib.sha256(normalized.encode()).hexdigest()


def to_casebook(text):
    return text.replace('(../../', '(../').replace('src="../../', 'src="../')


def narrative_summary(row):
    """Reuse scenario/method or opening prose, never media captions."""
    body = row['body']
    fields = re.findall(r'^- \*\*(?:Scenario|Approach|Scenario & approach|场景|做法|场景与做法|图片链路)\*\*[：:]\s*(.+)$', body, re.M | re.I)
    if fields:
        return ' '.join(fields)
    for paragraph in body.split('\n\n'):
        paragraph = paragraph.strip()
        if paragraph and not paragraph.startswith(('[', '<', '**', '- ', '#', 'Original ', '原作者素材')):
            return paragraph.replace('\n', ' ')
    raise ValueError('Missing homepage summary: ' + row['title'])


def narrative_field(row, labels):
    """Read an existing labeled field without modifying the original narrative."""
    pattern = r'^(?:- )?\*\*(?:' + '|'.join(re.escape(x) for x in labels) + r')[：:]?\*\*[：:]?\s*(.+)$'
    match = re.search(pattern, row['body'], re.M)
    return match[1] if match else ''


def first_sentence(text):
    # Preserve decimal numbers and Markdown links; split only sentence endings.
    parts = re.split(r'(?<=。)|(?<=[.!?])\s+(?=[A-Z])', text, maxsplit=1)
    return parts[0].strip()


def load_entries(directory=None):
    entries = []
    ids, sources = set(), set()
    categories = {c['id'] for c in settings()['categories']}
    for p in sorted((directory or ROOT / 'content/cases').glob('*.md')):
        parts = p.read_text().split('---\n', 2)
        if len(parts) != 3 or parts[0]:
            raise ValueError('Missing YAML frontmatter: ' + p.name)
        entry = yaml.safe_load(parts[1])
        required = {'id', 'category', 'order', 'title', 'source_url', 'legacy_anchors'}
        if not isinstance(entry, dict) or set(entry) != required:
            raise ValueError('Invalid case metadata fields: ' + p.name)
        id = entry['id']
        if not isinstance(id, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', id) or p.stem != id or id in ids:
            raise ValueError('Invalid or duplicate case ID: ' + p.name)
        if entry['category'] not in categories:
            raise ValueError('Unknown category: ' + id)
        if type(entry['order']) not in (int, float) or not 0 <= entry['order'] < float('inf'):
            raise ValueError('Invalid display order: ' + id)
        source = entry['source_url']
        if not isinstance(source, str) or not source.startswith('https://') or source in sources:
            raise ValueError('Invalid or duplicate source: ' + id)
        for key in ('title', 'legacy_anchors'):
            if not isinstance(entry[key], dict) or set(entry[key]) != set(LANGUAGES):
                raise ValueError('Missing bilingual ' + key + ': ' + id)
        body_parts = re.split(r'<!-- case:(en|zh) -->', parts[2])
        if len(body_parts) != 5 or body_parts[1::2] != ['en', 'zh'] or body_parts[0].strip():
            raise ValueError('Expected one English and one Chinese body: ' + id)
        entry['bodies'] = {}
        for lang, body in zip(body_parts[1::2], body_parts[2::2]):
            title = entry['title'][lang]
            aliases = entry['legacy_anchors'][lang]
            if not isinstance(title, str) or not title.strip() or not body.strip():
                raise ValueError('Empty title or body: ' + id)
            if not isinstance(aliases, list) or any(not isinstance(a, str) or not re.fullmatch(r'[\w-]+', a) for a in aliases):
                raise ValueError('Invalid legacy anchors: ' + id)
            entry['bodies'][lang] = to_casebook(body.strip())
        entries.append(entry)
        ids.add(id); sources.add(source)
    if not entries:
        raise ValueError('No case sources found')
    return entries


def read_catalog(entries=None):
    categories = settings()['categories']
    by_category = {c['id']: c for c in categories}
    category_order = {c['id']: n for n, c in enumerate(categories)}
    entries = sorted(load_entries() if entries is None else entries,
                     key=lambda r: (category_order[r['category']], r['order'], r['id']))
    localized = {lang: [] for lang in LANGUAGES}
    catalog = []
    for number, entry in enumerate(entries, 1):
        item = {k: entry[k] for k in ('id', 'category', 'source_url', 'title')}
        item.update(number=number, summary={}, takeaway={}, scope={}, details={}, source_path=f"content/cases/{entry['id']}.md")
        for lang, path in LANGUAGES.items():
            row = {'id': entry['id'], 'number': number, 'title': entry['title'][lang],
                   'category': entry['category'], 'category_title': by_category[entry['category']]['title'][lang],
                   'source_url': entry['source_url'], 'anchor': 'case-' + entry['id'],
                   'aliases': entry['legacy_anchors'][lang], 'body': entry['bodies'][lang]}
            localized[lang].append(row)
            item['summary'][lang] = narrative_summary(row)
            item['takeaway'][lang] = narrative_field(row, ['Pattern', '可借鉴点', '实现模式'])
            item['scope'][lang] = first_sentence(narrative_field(row, ['Scope', '边界']))
            item['details'][lang] = path + '#' + row['anchor']
        catalog.append(item)
    return localized, catalog


def load_cases():
    return [json.loads(p.read_text()) for p in sorted((ROOT / 'data/cases').glob('*.json'))]
