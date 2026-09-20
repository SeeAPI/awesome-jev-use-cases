#!/usr/bin/env python3
"""Validate metadata, generated outputs, preserved cases, and local links offline."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from jsonschema import Draft202012Validator, FormatChecker
from catalog import ROOT, LANGUAGES, read_catalog, load_cases, body_hash, slug
from generate import build


def check_metadata(records, catalog):
    schema = json.loads((ROOT / 'data/case.schema.json').read_text())
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    seen = set()
    sources = set()
    for r in records:
        errors.extend(f"{r.get('id', '?')}: {e.message}" for e in validator.iter_errors(r))
        if r.get('id') in seen or r.get('source_url') in sources:
            errors.append('Duplicate curated ID or source: ' + str(r.get('id')))
        seen.add(r.get('id')); sources.add(r.get('source_url'))
        row = next((item for item in catalog if item['id'] == r.get('id')), None)
        if row is None:
            errors.append('Unknown catalog ID: ' + str(r.get('id')))
            continue
        for key in ['title','category','source_url']:
            if r.get(key) != row[key]:
                errors.append(f"{r.get('id')}: catalog mismatch for {key}")
        for key in ['report_path','dataset_path']:
            path = r.get('evidence', {}).get(key)
            if path and (not (ROOT/path).is_file() or ROOT not in (ROOT/path).resolve().parents):
                errors.append('Missing or external evidence artifact: ' + path)
    return errors


def anchors(text):
    values = re.findall(r'<a id="([^"]+)"></a>', text)
    counts = {}
    for h in re.findall(r'^#{1,6} (.+)$', text, re.M):
        a = slug(h)
        count = counts.get(a, 0); counts[a] = count + 1
        values.append(a if count == 0 else a + '-' + str(count))
    return values


def main():
    errors = []
    localized, catalog = read_catalog()
    records = load_cases()
    errors.extend(check_metadata(records,catalog))
    baseline = json.loads((ROOT/'data/migration-baseline.json').read_text())
    for lang, cases in localized.items():
        original = baseline['languages'][lang]
        if len(cases) < len(original):
            errors.append('Cases removed in ' + lang)
        for old in original:
            same = [r for r in cases if r['title']==old['title'] and r['source_url']==old['source_url']]
            if len(same)!=1 or body_hash(same[0]['body'])!=old['body_sha256']:
                errors.append('Migration changed original case: ' + lang + ' ' + old['title'])
        rootfile = 'README.md' if lang=='en' else 'README.zh-CN.md'
        rootanchors = set(anchors((ROOT/rootfile).read_text()))
        bookanchors = set(anchors((ROOT/LANGUAGES[lang]).read_text()))
        for case in cases:
            for a in [case['anchor']] + case['aliases']:
                if a not in rootanchors or a not in bookanchors:
                    errors.append('Lost old README anchor: ' + a)
        if [r['number'] for r in cases] != list(range(1,len(cases)+1)):
            errors.append('Nonconsecutive case numbers')
    for name, expected in build().items():
        if not (ROOT/name).exists() or (ROOT/name).read_text()!=expected:
            errors.append('Stale generated file: '+name)
    # Check actual documents, including anchors in archived casebooks. No network.
    files = [p for p in ROOT.rglob('*.md') if '.git' not in p.parts and '.venv' not in p.parts]
    for p in files:
        s=p.read_text()
        if re.search(r'^(<<<<<<<|=======|>>>>>>>)',s,re.M):
            errors.append('Conflict marker: '+str(p.relative_to(ROOT)))
        ids=re.findall(r'<a id="([^"]+)"></a>',s)
        # Bilingual authoring files may preserve the same legacy anchor in both bodies.
        # Their generated, separate-language casebooks are checked independently.
        if p.parent != ROOT/'content/cases' and len(ids)!=len(set(ids)):
            errors.append('Duplicate explicit anchor: '+str(p.relative_to(ROOT)))
        for pair in re.findall(r'\]\(([^\s)]+)\)|src="([^"]+)"',s):
            url=pair[0] or pair[1]
            parsed=urlsplit(url)
            if parsed.scheme or url.startswith('//'):
                continue
            target=(p.parent/unquote(parsed.path)).resolve() if parsed.path else p
            if not target.exists():
                errors.append(f'{p.relative_to(ROOT)}: missing {url}')
            elif parsed.fragment and target.suffix=='.md':
                if unquote(parsed.fragment) not in anchors(target.read_text()):
                    errors.append(f'{p.relative_to(ROOT)}: missing anchor {url}')
    if errors:
        print('\n'.join(errors),file=sys.stderr);return 1
    print(f'PASS: {len(catalog)} bilingual cases, {len(records)} schema-valid records, preservation hashes, generated files and local links.')
    return 0

if __name__=='__main__':
    sys.exit(main())
