# Sift — 搜索结果重排

[English](sift.md) · [简体中文](sift.zh-CN.md)

[阅读完整案例](../docs/casebook.zh-CN.md#case-sift)

本页为元数据参考，完整案例集是主要阅读入口。

Chrome 扩展使用 Jev 判断搜索结果的相关性、推广倾向和信息深度，再由代码重排 Google 搜索结果。

**证据类型:** `docs-reviewed` · **核查日期:** 2026-09-18 · **SeeAPI 实测:** 否

**判断类型:** noul, score · **后续动作:** rank

[原始来源](https://github.com/tylergibbs1/sift) · [数据记录](../data/cases/sift.json)

## 适用边界

- 依据搜索摘要而非网页全文；过滤策略会考虑搜索意图。

[证据定义](../docs/evidence.zh-CN.md)
