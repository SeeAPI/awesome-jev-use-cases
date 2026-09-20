---
id: ndolinschi-lanebreak
category: productivity
order: 520
title:
  en: LaneBreak — support ticket routing
  zh: LaneBreak — 客服工单分组与优先级
source_url: https://github.com/ndolinschi/lanebreak
legacy_anchors:
  en:
  - 52-lanebreak--support-ticket-routing
  - 37-lanebreak--support-ticket-routing
  zh:
  - 52-lanebreak--客服工单分组与优先级
  - 37-lanebreak--客服工单分组与优先级
---

<!-- case:en -->

[Project](https://github.com/ndolinschi/lanebreak) · [Implementation](https://github.com/ndolinschi/lanebreak/blob/acf11293f36597c8fb706ae492a9468455b69928/src/lib/product.ts)

Uses Choice for team assignment, Score for priority, and Noul for refund intent, churn signals and human escalation.

**Scope:** Without an API key the implementation uses local heuristic demo responses; those are not Jev results.

<!-- case:zh -->

[项目来源](https://github.com/ndolinschi/lanebreak) · [实现代码](https://github.com/ndolinschi/lanebreak/blob/acf11293f36597c8fb706ae492a9468455b69928/src/lib/product.ts)

用 Choice 分配客服团队、Score 判断优先级、Noul 识别退款意图、流失信号与转人工需求。

**边界:** 未配置 API key 时使用本地规则模拟，模拟结果不属于 Jev 实测。

