# Jev Search — 自然语言搜索意图识别与结果重排

[English](jev-search.md) · [简体中文](jev-search.zh-CN.md)

[阅读完整案例](../docs/casebook.zh-CN.md#case-jev-search)

本页为元数据参考，完整案例集是主要阅读入口。

TypeScript 应用先让 Jev 选择搜索源、时间范围与检索词候选，经 Search1API 获取结果后，批量判断标题及摘要相关性；代码合并 URL，按相关性、引擎一致性与原始名次排序。

**证据类型:** `docs-reviewed` · **核查日期:** 2026-09-18 · **SeeAPI 实测:** 否

**判断类型:** choice, noul · **后续动作:** select-source, rank

[原始来源](https://github.com/superagents-lab/jev-search) · [数据记录](../data/cases/jev-search.json)

## 适用边界

- 相关性分数不验证网页事实，摘要可能不完整或过时；一次搜索可能触发多次供应商调用。本轮查阅了接口与排序管线代码，未测量检索质量、时延或费用。

[证据定义](../docs/evidence.zh-CN.md)
