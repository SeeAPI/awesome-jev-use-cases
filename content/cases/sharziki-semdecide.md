---
id: sharziki-semdecide
category: automation
order: 120
title:
  en: SemDecide
  zh: SemDecide
source_url: https://github.com/sharziki/semdecide
legacy_anchors:
  en:
  - 12-semdecide
  - 8-semdecide
  zh:
  - 12-semdecide
  - 8-semdecide
---

<!-- case:en -->

[Repository](https://github.com/sharziki/semdecide)

Brings semantic predicates, routing, scoring, filtering, and guard decisions into Unix pipelines and CI through `is`, `choose`, `score`, `filter`, and `guard` commands.

**Pattern:** typed judgments with explicit thresholds, uncertainty, and process exit codes.

**Scope:** semantic judgments do not replace authorization or execution controls.

<!-- case:zh -->

- **场景**：在命令行、CI 或数据流水线中做语义判断、路由、评分与过滤。
- **做法**：提供 `is`、`choose`、`score`、`filter` 和 `guard` 命令，将不确定性、阈值与进程退出码纳入接口。
- **可借鉴点**：既输出判断结果，也明确表示“不确定”和“调用失败”。
- **边界**：模型判断不是权限系统；自动执行仍由调用方流程决定。
- **来源**：[项目 README](https://github.com/sharziki/semdecide)。

