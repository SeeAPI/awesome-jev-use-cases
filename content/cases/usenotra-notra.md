---
id: usenotra-notra
category: productivity
order: 460
title:
  en: Notra — typed evaluation in analytics
  zh: Notra — typed evaluation in analytics
source_url: https://github.com/usenotra/notra
legacy_anchors:
  en:
  - 46-notra--typed-evaluation-in-analytics
  - 31-notra--typed-evaluation-in-analytics
  zh:
  - 46-notra--typed-evaluation-in-analytics
  - 31-notra--typed-evaluation-in-analytics
---

<!-- case:en -->

[Project](https://github.com/usenotra/notra) · [Discovery post](https://x.com/yibie/status/2100619188062523695) · [Implementation / 文档](https://github.com/usenotra/notra/blob/main/packages/ai/src/evaluation/client.ts)

The codebase includes a Jev evaluation client through Vercel AI Gateway, a NOTRA_JEV_CLASSIFIERS flag, and optional typed evaluation alongside brand-mention analysis.

**Pattern:** Introduce typed judgments into an existing analytics workflow with an LLM fallback.

**Scope:** Source inspection establishes an integration path, not independently verified production deployment or latency. Existing LLM judgment still supplies competitor information and excerpts in the inspected workflow.

<!-- case:zh -->

- **场景与做法**：代码提供通过 Vercel AI Gateway 调用 Jev 的评估客户端、NOTRA_JEV_CLASSIFIERS 开关，并在品牌提及分析中接入可选的结构化评估。
- **可借鉴点**：在已有分析工作流中加入结构化判断，并保留 LLM 回退。
- **边界**：代码能证明接入路径，不能独立证明线上启用状态或延迟；所查流程仍由 LLM 提供竞争对手信息与引用片段。
- **来源**：[项目](https://github.com/usenotra/notra) · [发现来源帖子](https://x.com/yibie/status/2100619188062523695) · [Implementation / 文档](https://github.com/usenotra/notra/blob/main/packages/ai/src/evaluation/client.ts)。

