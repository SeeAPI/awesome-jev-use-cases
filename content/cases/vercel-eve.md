---
id: vercel-eve
category: routing
order: 290
title:
  en: eve — typed evaluation and model selection
  zh: eve — typed evaluation and model selection
source_url: https://github.com/vercel/eve
legacy_anchors:
  en:
  - 29-eve--typed-evaluation-and-model-selection
  - 21-eve--typed-evaluation-and-model-selection
  zh:
  - 29-eve--typed-evaluation-and-model-selection
  - 21-eve--typed-evaluation-and-model-selection
---

<!-- case:en -->

[Project](https://github.com/vercel/eve) · [Discovery post](https://x.com/yibie/status/2100619188062523695) · [Implementation / 文档](https://github.com/vercel/eve/blob/main/docs/guides/evaluate.md)

The agent framework uses Jev by default for automatic model selection and typed evaluations; its documented tool-approval integration can escalate uncertain or failed reviews to a human.

**Pattern:** Embed typed evaluation in model routing, tools, and approval decisions.

**Scope:** Jev is the evaluator, not the sole model powering eve. The underlying AI SDK evaluation specification is experimental.

<!-- case:zh -->

- **场景与做法**：Agent 框架默认使用 Jev 做自动模型选择和结构化评估，文档还展示了工具执行审批中的判断与人工复核。
- **可借鉴点**：将结构化评估接入模型路由、工具和审批流程。
- **边界**：Jev 是评估器，不是 eve 的唯一运行模型；底层 AI SDK evaluation 规范仍为实验性。
- **来源**：[项目](https://github.com/vercel/eve) · [发现来源帖子](https://x.com/yibie/status/2100619188062523695) · [Implementation / 文档](https://github.com/vercel/eve/blob/main/docs/guides/evaluate.md)。

