## What changed / 改了什么

Explain the case added, corrected, or reorganized. Link the original public source.

## Evidence / 证据

Explain Jev's input and judgment, how code uses the answer, and known limitations. Distinguish documentation review, author demo, and your own execution. Identify screenshot licensing when applicable.

## Checks / 检查

- [ ] Edited the bilingual source in `content/cases/<stable-id>.md`; preserved its ID and legacy anchors.
- [ ] Updated optional `data/cases/<stable-id>.json` metadata if affected; did not invent a testing claim.
- [ ] Regenerated outputs and ran `python3 scripts/validate.py`.
- [ ] For code changes, ran `python3 -m unittest discover -s tests -v`.
- [ ] Any intentional preservation-baseline change is limited to the corrected case and explained in this PR and the changelog.
