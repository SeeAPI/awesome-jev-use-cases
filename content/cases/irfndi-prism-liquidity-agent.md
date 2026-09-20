---
id: irfndi-prism-liquidity-agent
category: experiments
order: 610
title:
  en: Prism's Jev judgment service
  zh: Prism 的 Jev 判断服务
source_url: https://github.com/irfndi/prism-liquidity-agent
legacy_anchors:
  en:
  - 61-prisms-jev-judgment-service
  - 40-prisms-jev-judgment-service
  zh:
  - 61-prism-的-jev-判断服务
  - 40-prism-的-jev-判断服务
---

<!-- case:en -->

[Repository](https://github.com/irfndi/prism-liquidity-agent) · [Jev service](https://github.com/irfndi/prism-liquidity-agent/blob/main/engine/jev-service.ts)

Maps liquidity-strategy questions about distribution choice, toxic flow, recovery holding, and market stress to Choice and Noul judgments alongside existing heuristics.

**Pattern:** compare model advice with existing rules in shadow or advisory mode.

**Scope:** the inspected Jev module explicitly states shadow/advisory use. It is not evidence of profitable autonomous trading by Jev.

<!-- case:zh -->

- **场景**：对流动性策略中的分布方式、有害交易流、恢复持有与市场压力给出辅助判断。
- **做法**：`engine/jev-service.ts` 将窄问题映射到 Choice 与 Noul，与既有启发式判断对应。
- **可借鉴点**：先以 shadow/advisory 方式记录与对照模型意见，再评估是否适合进入执行流程。
- **边界**：所核查 Jev 模块明确为 shadow/advisory，不能宣传为 Jev 自动交易或盈利案例。
- **来源**：[项目](https://github.com/irfndi/prism-liquidity-agent)、[Jev 服务实现](https://github.com/irfndi/prism-liquidity-agent/blob/main/engine/jev-service.ts)。

