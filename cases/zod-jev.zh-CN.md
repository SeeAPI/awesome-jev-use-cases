# zod-jev — 表单语义校验

[English](zod-jev.md) · [简体中文](zod-jev.zh-CN.md)

[阅读完整案例](../docs/casebook.zh-CN.md#case-zod-jev)

本页为元数据参考，完整案例集是主要阅读入口。

在 Zod 格式校验之上加入 Jev 语义判断，将概率转为校验结果，适合检查内容含义、分类与描述是否匹配。

**证据类型:** `docs-reviewed` · **核查日期:** 2026-09-18 · **SeeAPI 实测:** 否

**判断类型:** noul · **后续动作:** accept, reject, review

[原始来源](https://github.com/jomatsu/zod-jev) · [数据记录](../data/cases/zod-jev.json)

## 适用边界

- 需要处理不确定和服务不可用的结果；通过校验不代表事实一定正确。

[证据定义](../docs/evidence.zh-CN.md)
