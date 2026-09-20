---
id: jev-codex-router
category: routing
order: 250
title:
  en: Jev Codex Router
  zh: Jev Codex Router
source_url: https://github.com/0xNatoshi/jev-codex-router
legacy_anchors:
  en:
  - 25-jev-codex-router
  - 17-jev-codex-router
  zh:
  - 25-jev-codex-router
  - 17-jev-codex-router
---

<!-- case:en -->

[Repository and backtest](https://github.com/0xNatoshi/jev-codex-router)

Classifies coding turns with Jev and applies a policy to select a model and reasoning depth, with logging and fallback behavior.

**Pattern:** task classification → model selection → quality and cost evaluation.

**Scope:** the reported roughly 60% savings comes from the author's replay of 237 real turns. It is not a SeeAPI measurement or a guaranteed saving.

<!-- case:zh -->

- **场景**：按编程任务难度选择模型与推理深度。
- **做法**：每轮先由 Jev 分类，再按策略路由到不同模型，记录结果并处理低置信度或错误。
- **可借鉴点**：在质量、延迟和费用之间建立可观察的路由策略。
- **边界**：约 60% 成本下降来自作者对 237 个真实 turn 的回放自测，不是 SeeAPI 实测或普遍承诺。
- **来源**：[项目及回测入口](https://github.com/0xNatoshi/jev-codex-router)。

