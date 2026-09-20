---
id: ghalebdweikat-winnow
category: routing
order: 260
title:
  en: Winnow
  zh: Winnow
source_url: https://github.com/GhalebDweikat/winnow
legacy_anchors:
  en:
  - 26-winnow
  - 18-winnow
  zh:
  - 26-winnow
  - 18-winnow
---

<!-- case:en -->

[Repository](https://github.com/GhalebDweikat/winnow)

Judges blocks of long Claude Code tool outputs for task relevance. Confidently irrelevant blocks become summaries or stubs, while full text remains recoverable; uncertain blocks are retained.

**Pattern:** reversible relevance filtering before context ingestion.

**Scope:** judgment and summary generation are separate stages. Results using an alternative judge adapter should not be attributed to Jev.

<!-- case:zh -->

- **场景**：压缩进入 Claude Code 上下文的长工具输出。
- **做法**：Jev 判断分块内容是否与当前任务有关；高置信度无关内容替换为摘要或占位说明，原文缓存并支持按需恢复。不确定内容保留。
- **可借鉴点**：保留召回机制的上下文筛选，而非直接删除信息。
- **边界**：筛选判断与摘要生成是不同步骤；配置其他判断适配器时不能把结果一概归为 Jev 效果。
- **来源**：[项目 README](https://github.com/GhalebDweikat/winnow)。

