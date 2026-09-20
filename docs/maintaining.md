# Maintaining the casebook

[English](maintaining.md) · [Chinese](maintaining.zh-CN.md)

## Source ownership

| Editable source | Responsibility | Generated outputs |
| --- | --- | --- |
| `content/cases/<stable-id>.md` | One project's identity, category, bilingual narrative, original media and legacy anchors | Full Casebooks, README summaries, discovery index |
| `content/pages/background.en.md`, `background.zh.md` | Model background, access guide, scope and source notes | Casebook background sections |
| `data/site.json` | Explicit category IDs, bilingual labels, descriptions and content update date | Homepage and Casebook directories |
| `data/cases/<stable-id>.json` | Optional enriched metadata and evidence; currently 12 projects | `data/cases.json`, compatibility metadata cards |
| `data/featured-media.json` | Pinned author media or implementation links for featured cases; screenshot provenance and mock-mode captions | README and Casebook media blocks |
| `data/search-aliases.json` | Small, reviewed bilingual keyword groups | Offline search behavior |
| `scripts/generate.py` | Homepage layout and six editorial selections | READMEs, Casebooks, catalogs, metadata cards and `llms.txt` |

Readers start in the README and open the full Casebook for details. The `cases/` cards are metadata references retained for existing links, not another required reading step. `README_zh.md` remains a generated compatibility entry.

## Add or edit a case

1. Edit only that case's `content/cases/<stable-id>.md`. For a new entry, copy an existing source structure and give it a unique lowercase ID, source URL, category and display order. Use `legacy_anchors: {en: [], zh: []}` for a new case.
2. Keep the `<!-- case:en -->` and `<!-- case:zh -->` sections. Write the concrete problem and Jev's role in the opening paragraph or the existing scenario/approach fields; these become homepage and search summaries. Include implementation, evidence, limitations and original source links in the body.
3. Keep relative links correct from `content/cases/` (for example `../../assets/...`). Generation rebases them for the Casebook and homepage.
4. Keep an existing ID and `legacy_anchors` unchanged. `order` only controls display within the category; it is not an identity. Equal orders use the stable ID as a deterministic tie-breaker. Display numbers are generated and need no manual renumbering.
5. Add enriched metadata only when supported by evidence; its `id` must match the case. Do not invent primitives or a test result to fill fields.
6. Update `data/site.json`'s content date and `CHANGELOG.md`, regenerate, and inspect both languages. This date means collection content changed, not that all projects were re-tested.

Do not hand-edit generated READMEs, Casebooks, aggregate JSON or cards. For concurrent contributions, resolve the independent case source changes first, then regenerate shared outputs. This reduces manual merges; it does not prevent Git from reporting conflicts in generated files.

## Checks

Python 3.9+:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/generate.py
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
```

The PR workflow runs validation and tests against committed outputs; it does not regenerate away stale files, call models, sync Feishu, or publish. No secrets are required.

Validation covers case metadata, identity alignment, original body hashes, old README anchors, generated-file freshness and local links. Tests cover inserted/reordered cases, bilingual search and routing failure handling. Neither establishes that external websites remain accessible or models perform well.

`data/migration-baseline.json` records original body hashes at the pre-refactor commit. It was not rewritten during the file split. An intentional content correction requires a narrowly scoped baseline update explained in the changelog and PR; never regenerate the entire baseline to hide missing content.

## Next increments

- Improve summaries, add documented aliases and review metadata in small batches.
- Add recipes only with useful copyable inputs, clear limitations and offline checks.
- Publish independent benchmarks only after raw evidence is available and reviewed.
- Measure traffic and referrers separately. Repository structure alone does not establish Star or traffic gains.


Homepage entries also reuse an existing pattern field in the corresponding language when available and the first sentence of scope field. Keep that first sentence self-contained; full limitations remain in the Casebook. No new claims should be inferred to fill an empty pattern field.
