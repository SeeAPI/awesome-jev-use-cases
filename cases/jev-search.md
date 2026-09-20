# Jev Search — intent selection and result reranking

[Read the full case](../docs/casebook.md#case-jev-search) · [阅读完整案例](../docs/casebook.zh-CN.md#case-jev-search)

Metadata reference; the Casebook is the main reading entry.

A TypeScript application asks Jev to select search sources, time ranges, and query candidates, fetches results through Search1API, then judges title/snippet relevance in batches. Code merges URLs and ranks results by relevance, engine agreement, and original position.

**Evidence:** `docs-reviewed` · **Reviewed:** 2026-09-18 · **Live-tested by SeeAPI:** no

**Primitive:** choice, noul · **Action:** select-source, rank

[Original source](https://github.com/superagents-lab/jev-search) · [Full case](../docs/casebook.md#case-jev-search) · [Data record](../data/cases/jev-search.json)

## Limits

- Relevance scores do not verify page facts; snippets can be incomplete or stale. A search can make several provider calls. Source and ranking code were inspected, but retrieval quality, latency, and cost were not measured.

## 中文

TypeScript 应用先让 Jev 选择搜索源、时间范围与检索词候选，经 Search1API 获取结果后，批量判断标题及摘要相关性；代码合并 URL，按相关性、引擎一致性与原始名次排序。

- 相关性分数不验证网页事实，摘要可能不完整或过时；一次搜索可能触发多次供应商调用。本轮查阅了接口与排序管线代码，未测量检索质量、时延或费用。

[完整中文案例](../docs/casebook.zh-CN.md#case-jev-search) · [证据说明](../docs/evidence.md)
