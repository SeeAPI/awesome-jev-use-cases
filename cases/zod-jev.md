# zod-jev — semantic validation

[Read the full case](../docs/casebook.md#case-zod-jev) · [阅读完整案例](../docs/casebook.zh-CN.md#case-zod-jev)

Metadata reference; the Casebook is the main reading entry.

Adds Jev semantic checks to Zod schemas, turning probabilities into validation issues alongside ordinary shape checks.

**Evidence:** `docs-reviewed` · **Reviewed:** 2026-09-18 · **Live-tested by SeeAPI:** no

**Primitive:** noul · **Action:** accept, reject, review

[Original source](https://github.com/jomatsu/zod-jev) · [Full case](../docs/casebook.md#case-zod-jev) · [Data record](../data/cases/zod-jev.json)

## Limits

- Uncertain and unavailable judgments need explicit handling; a passing check does not establish factual correctness.

## 中文

在 Zod 格式校验之上加入 Jev 语义判断，将概率转为校验结果，适合检查内容含义、分类与描述是否匹配。

- 需要处理不确定和服务不可用的结果；通过校验不代表事实一定正确。

[完整中文案例](../docs/casebook.zh-CN.md#case-zod-jev) · [证据说明](../docs/evidence.md)
