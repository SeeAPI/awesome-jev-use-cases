---
id: dabit3-jev-experiments-tree-main-judge-sheets
category: productivity
order: 450
title:
  en: Judge Sheets — predictive spreadsheets
  zh: Judge Sheets — predictive spreadsheets
source_url: https://github.com/dabit3/jev-experiments/tree/main/judge-sheets
legacy_anchors:
  en:
  - 45-judge-sheets--predictive-spreadsheets
  - 30-judge-sheets--predictive-spreadsheets
  zh:
  - 45-judge-sheets--predictive-spreadsheets
  - 30-judge-sheets--predictive-spreadsheets
---

<!-- case:en -->

[Project](https://github.com/dabit3/jev-experiments/tree/main/judge-sheets) · [Discovery post](https://x.com/dabit3/status/2100780008193020049)

Typing a column header such as Urgency lets Jev infer a prediction schema; confirming it fills rows through JUDGE, PICK, and RATE functions, with grouped requests and streamed updates.

**Pattern:** Header intent → typed schema → row judgments → spreadsheet recalculation.

**Scope:** A standalone spreadsheet demo, not a Google Sheets integration. Roughly 100 ms refers to individual judgments or header interpretation, not the entire column. Timings are author-reported; mock mode is also available.

**Demo material**: [Original screenshot and animated demo](https://github.com/dabit3/jev-experiments/tree/main/judge-sheets#judge-sheets--predictive-spreadsheets)

<!-- case:zh -->

- **场景与做法**：输入 Urgency 等列标题后，Jev 推断预测类型；确认后通过 JUDGE、PICK、RATE 函数填充各行，同一文本的问题合并请求，结果流式返回并触发表格重算。
- **可借鉴点**：表头意图 → 判断类型 → 逐行评估 → 表格重算。
- **边界**：独立表格演示，并非 Google Sheets 插件；约 100 毫秒指单次判断或表头解析，不是整列处理时间。速度为作者报告，也有 mock 模式。
- **来源**：[项目](https://github.com/dabit3/jev-experiments/tree/main/judge-sheets) · [发现来源帖子](https://x.com/dabit3/status/2100780008193020049)。

**演示素材**: [原作者界面截图与动态演示](https://github.com/dabit3/jev-experiments/tree/main/judge-sheets#judge-sheets--predictive-spreadsheets)

