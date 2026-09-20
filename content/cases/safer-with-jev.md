---
id: safer-with-jev
category: moderation
order: 10
title:
  en: Safer with Jev — typesafe-on-neon
  zh: Safer with Jev（原 TypeSafe on Neon）
source_url: https://github.com/andrelandgraf/typesafe-on-neon
legacy_anchors:
  en:
  - 1-safer-with-jev--typesafe-on-neon
  zh:
  - 1-safer-with-jev原-typesafe-on-neon
---

<!-- case:en -->

[Repository](https://github.com/andrelandgraf/typesafe-on-neon) · [Vision implementation](https://github.com/andrelandgraf/typesafe-on-neon/blob/main/src/lib/vision.ts) · [Jev judgments](https://github.com/andrelandgraf/typesafe-on-neon/blob/main/src/lib/judge.ts)

An HTTP gate that checks prompt injections, unsafe images, and unsafe replies before optionally forwarding a request. Its image pipeline first uses `gemini-3-flash` to describe the image, then asks Jev to judge risks in that description.

**Pattern:** detection and interpretation → typed risk judgments → allow, review, or block.

**Scope:** this is a vision-model-plus-Jev pipeline, not evidence of native image classification by Jev. The current project is a safety gate; earlier descriptions of it as a model router are outdated. We have not measured its detection accuracy.

<!-- case:zh -->

- **场景**：在内容转发或上传前检查提示词注入、图片风险及模型回复风险。
- **做法**：HTTP 网关接收内容，输出放行、复核或拦截结果；通过后可转发到指定上游。
- **图片链路**：当前实现用 `gemini-3-flash` 生成结构化图片描述，再由 Jev 对描述中的性内容、血腥暴力等风险进行判断。Jev 在这里承担描述审核与决策环节。
- **可借鉴点**：将检测结果连接到上传拦截、人工复核与下游调用流程。
- **边界**：不是 Jev 原生视觉 NSFW 检测的证据，也没有在本次核查中验证识别效果。原帖的“模型 Router”介绍已不符合当前 README。
- **来源**：[项目](https://github.com/andrelandgraf/typesafe-on-neon)、[视觉描述实现](https://github.com/andrelandgraf/typesafe-on-neon/blob/main/src/lib/vision.ts)、[Jev 判断实现](https://github.com/andrelandgraf/typesafe-on-neon/blob/main/src/lib/judge.ts)。

