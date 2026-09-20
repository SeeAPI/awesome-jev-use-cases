# Case data

- `catalog.json`: generated index of every case, including stable ID, bilingual title, purpose summary, documented pattern and key scope, original source, authoring path and full-detail links. Search covers all summaries.
- `cases/*.json`: editable enriched metadata for 12 cases. Join to the full catalog by stable `id`, never by display number.
- `cases.json`: generated aggregate of enriched metadata. Do not edit directly.
- `case.schema.json`: required metadata fields and evidence assertions.
- `featured-media.json`: pinned author screenshot and documentation references, with explicit mock-mode captions.
- `site.json`: explicit category definitions and collection content update date.
- `search-aliases.json`: reviewed bilingual keyword groups; the search is keyword-based, not embedding or semantic search.
- `migration-baseline.json`: original case identities and body hashes at the recorded commit. Do not update merely to silence a preservation failure.

All bilingual narratives are maintained in `content/cases/<stable-id>.md`. The generator produces the reader-facing Casebooks and homepages. A metadata record is optional: cases without one retain `evidence: null` in search results rather than acquiring an unsupported test label.

Evidence dates refer to the documented review, not file conversion. `verified_by_seeapi` requires an actual run with a report. See [evidence definitions](../docs/evidence.md) and [maintenance instructions](../docs/maintaining.md).

Install `requirements-dev.txt`, then run:

```sh
python3 scripts/generate.py
python3 scripts/validate.py
```
