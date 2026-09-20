# Sift — search result reranking

[Read the full case](../docs/casebook.md#case-sift) · [阅读完整案例](../docs/casebook.zh-CN.md#case-sift)

Metadata reference; the Casebook is the main reading entry.

A Chrome extension asks Jev about relevance, promotional content and depth, then reranks Google results in code.

**Evidence:** `docs-reviewed` · **Reviewed:** 2026-09-18 · **Live-tested by SeeAPI:** no

**Primitive:** noul, score · **Action:** rank

[Original source](https://github.com/tylergibbs1/sift) · [Full case](../docs/casebook.md#case-sift) · [Data record](../data/cases/sift.json)

## Limits

- Judgments use result snippets rather than full pages; search intent affects filtering.

## 中文

Chrome 扩展使用 Jev 判断搜索结果的相关性、推广倾向和信息深度，再由代码重排 Google 搜索结果。

- 依据搜索摘要而非网页全文；过滤策略会考虑搜索意图。

[完整中文案例](../docs/casebook.zh-CN.md#case-sift) · [证据说明](../docs/evidence.md)
