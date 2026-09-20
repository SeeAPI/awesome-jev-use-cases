# Safer with Jev — typesafe-on-neon

[English](safer-with-jev.md) · [Chinese](safer-with-jev.zh-CN.md)

[Read the full case](../docs/casebook.md#case-safer-with-jev)

Metadata reference; the Casebook is the main reading entry.

An HTTP gate that checks prompt injections, unsafe images, and unsafe replies before optionally forwarding a request. Its image pipeline first uses `gemini-3-flash` to describe the image, then asks Jev to judge risks in that description.

**Evidence:** `docs-reviewed` · **Reviewed:** 2026-09-18 · **Live-tested by SeeAPI:** no

**Primitive:** noul · **Action:** allow, review, block

[Original source](https://github.com/andrelandgraf/typesafe-on-neon) · [Data record](../data/cases/safer-with-jev.json)

## Limits

- this is a vision-model-plus-Jev pipeline, not evidence of native image classification by Jev. The current project is a safety gate; earlier descriptions of it as a model router are outdated. We have not measured its detection accuracy.

[Evidence definitions](../docs/evidence.md)

<a id="中文"></a>[Read this page in Chinese](safer-with-jev.zh-CN.md)
