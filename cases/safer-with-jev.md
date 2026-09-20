# Safer with Jev — typesafe-on-neon

[Read the full case](../docs/casebook.md#case-safer-with-jev) · [阅读完整案例](../docs/casebook.zh-CN.md#case-safer-with-jev)

Metadata reference; the Casebook is the main reading entry.

An HTTP gate that checks prompt injections, unsafe images, and unsafe replies before optionally forwarding a request. Its image pipeline first uses `gemini-3-flash` to describe the image, then asks Jev to judge risks in that description.

**Evidence:** `docs-reviewed` · **Reviewed:** 2026-09-18 · **Live-tested by SeeAPI:** no

**Primitive:** noul · **Action:** allow, review, block

[Original source](https://github.com/andrelandgraf/typesafe-on-neon) · [Full case](../docs/casebook.md#case-safer-with-jev) · [Data record](../data/cases/safer-with-jev.json)

## Limits

- this is a vision-model-plus-Jev pipeline, not evidence of native image classification by Jev. The current project is a safety gate; earlier descriptions of it as a model router are outdated. We have not measured its detection accuracy.

## 中文

在内容转发或上传前检查提示词注入、图片风险及模型回复风险。

- 不是 Jev 原生视觉 NSFW 检测的证据，也没有在本次核查中验证识别效果。原帖的“模型 Router”介绍已不符合当前 README。

[完整中文案例](../docs/casebook.zh-CN.md#case-safer-with-jev) · [证据说明](../docs/evidence.md)
