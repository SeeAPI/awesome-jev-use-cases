---
id: jev-search
category: search
order: 430
title:
  en: Jev Search — intent selection and result reranking
  zh: Jev Search — 自然语言搜索意图识别与结果重排
source_url: https://github.com/superagents-lab/jev-search
legacy_anchors:
  en:
  - 43-jev-search--intent-selection-and-result-reranking
  zh:
  - 43-jev-search--自然语言搜索意图识别与结果重排
---

<!-- case:en -->

[Source](https://github.com/superagents-lab/jev-search) · [Implementation / documentation](https://github.com/superagents-lab/jev-search/blob/369b282489f72e58298ba1abc8b0144b1bc15c59/src/lib/typesafe.ts)

A TypeScript application asks Jev to select search sources, time ranges, and query candidates, fetches results through Search1API, then judges title/snippet relevance in batches. Code merges URLs and ranks results by relevance, engine agreement, and original position.

**Pattern:** Search intent → external retrieval → per-result judgments → merged, streamed rankings.

**Scope:** Relevance scores do not verify page facts; snippets can be incomplete or stale. A search can make several provider calls. Source and ranking code were inspected, but retrieval quality, latency, and cost were not measured.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/superagents-lab/jev-search) · [实现或文档](https://github.com/superagents-lab/jev-search/blob/369b282489f72e58298ba1abc8b0144b1bc15c59/src/lib/typesafe.ts)

TypeScript 应用先让 Jev 选择搜索源、时间范围与检索词候选，经 Search1API 获取结果后，批量判断标题及摘要相关性；代码合并 URL，按相关性、引擎一致性与原始名次排序。

**实现模式：** 搜索意图 → 外部检索 → 逐结果判断 → 合并并流式返回排名。

**边界：** 相关性分数不验证网页事实，摘要可能不完整或过时；一次搜索可能触发多次供应商调用。本轮查阅了接口与排序管线代码，未测量检索质量、时延或费用。

**核查日期：** 2026-09-18。

