# Jev Search — intent selection and result reranking

[English](jev-search.md) · [Chinese](jev-search.zh-CN.md)

[Read the full case](../docs/casebook.md#case-jev-search)

Metadata reference; the Casebook is the main reading entry.

A TypeScript application asks Jev to select search sources, time ranges, and query candidates, fetches results through Search1API, then judges title/snippet relevance in batches. Code merges URLs and ranks results by relevance, engine agreement, and original position.

**Evidence:** `docs-reviewed` · **Reviewed:** 2026-09-18 · **Live-tested by SeeAPI:** no

**Primitive:** choice, noul · **Action:** select-source, rank

[Original source](https://github.com/superagents-lab/jev-search) · [Data record](../data/cases/jev-search.json)

## Limits

- Relevance scores do not verify page facts; snippets can be incomplete or stale. A search can make several provider calls. Source and ranking code were inspected, but retrieval quality, latency, and cost were not measured.

[Evidence definitions](../docs/evidence.md)

<a id="中文"></a>[Read this page in Chinese](jev-search.zh-CN.md)
