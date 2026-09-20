#!/usr/bin/env python3
"""Offline keyword discovery over every bilingual case summary; not semantic search."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def query_groups(query):
    query = query.lower().strip()
    groups = []
    for aliases in json.loads((ROOT / 'data/search-aliases.json').read_text()):
        matched = [a for a in aliases if (a in query if re.search(r'[\u3400-\u9fff]', a)
                   else re.search(r'(?<!\w)' + re.escape(a) + r'(?!\w)', query))]
        if matched:
            groups.append(aliases)
            for alias in sorted(matched, key=len, reverse=True):
                query = query.replace(alias, ' ')
    groups.extend([term] for term in re.findall(r'[\w-]+', query))
    return groups


def search(query, limit=5):
    groups = query_groups(query)
    if not groups:
        return []
    curated = json.loads((ROOT / 'data/cases.json').read_text())
    by_id = {r['id']: r for r in curated}
    catalog = json.loads((ROOT / 'data/catalog.json').read_text())
    candidates = []
    for row in catalog:
        record = by_id.get(row['id'])
        # Exclude URLs, evidence boilerplate and JSON field names from matching.
        fields = [(5, row['title']), (3, row['summary']), (2, row.get('takeaway', {}))]
        if record:
            fields += [(4, record['tags']), (2, record['summary']),
                       (1, record['task']), (1, record['input_type'])]
        score = sum(weight for group in groups for weight, field in fields
                    if any(term in json.dumps(field, ensure_ascii=False).lower() for term in group))
        if not score:
            continue
        result = {'id': row['id'], 'title': row['title'], 'summary': row['summary'],
                  'source_url': row['source_url'], 'details': row['details'],
                  'evidence': record['evidence'] if record else None,
                  'recipe_ids': record['recipe_ids'] if record else [],
                  'record_path': 'data/cases/' + record['id'] + '.json' if record else row['source_path']}
        candidates.append((score, bool(record), row['id'], result))
    candidates.sort(key=lambda x: (-x[0], -x[1], x[2]))
    return [r[3] for r in candidates[:limit]]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query')
    parser.add_argument('--limit', type=int, default=5)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error('--limit must be positive')
    print(json.dumps(search(args.query, args.limit), ensure_ascii=False, indent=2))
