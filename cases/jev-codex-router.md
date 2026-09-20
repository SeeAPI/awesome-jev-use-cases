# Jev Codex Router

[Read the full case](../docs/casebook.md#case-jev-codex-router) · [阅读完整案例](../docs/casebook.zh-CN.md#case-jev-codex-router)

Metadata reference; the Casebook is the main reading entry.

Classifies coding turns with Jev and applies a policy to select a model and reasoning depth, with logging and fallback behavior.

**Evidence:** `docs-reviewed` · **Reviewed:** 2026-09-18 · **Live-tested by SeeAPI:** no

**Primitive:** choice · **Action:** route-model

[Original source](https://github.com/0xNatoshi/jev-codex-router) · [Full case](../docs/casebook.md#case-jev-codex-router) · [Data record](../data/cases/jev-codex-router.json)

## Limits

- the reported roughly 60% savings comes from the author's replay of 237 real turns. It is not a SeeAPI measurement or a guaranteed saving.

## 中文

按编程任务难度选择模型与推理深度。

- 约 60% 成本下降来自作者对 237 个真实 turn 的回放自测，不是 SeeAPI 实测或普遍承诺。

[完整中文案例](../docs/casebook.zh-CN.md#case-jev-codex-router) · [证据说明](../docs/evidence.md)

## Recipe

- [model-routing](../recipes/model-routing.md)
