---
id: devmortimer-pi-warden
category: routing
order: 340
title:
  en: Pi Warden — coding-agent rule feedback
  zh: Pi Warden — 规则检查与代理行为提醒
source_url: https://github.com/DevMortimer/pi-warden
legacy_anchors:
  en:
  - 34-pi-warden--coding-agent-rule-feedback
  zh:
  - 34-pi-warden--规则检查与代理行为提醒
---

<!-- case:en -->

[Source](https://github.com/DevMortimer/pi-warden) · [Implementation / documentation](https://github.com/DevMortimer/pi-warden/blob/main/README.md)

A Pi extension checks edits against project rules and places feedback in the agent’s context. Other guards assess task drift, unsupported completion claims, and risky actions; deterministic patterns and model judgments feed code-owned responses.

**Pattern:** Agent context and proposed changes → rule/risk checks → feedback or selected holds.

**Scope:** Many findings steer or warn rather than block. The author’s 150 paired runs report fewer rule violations, but other measured axes showed little or no improvement; results are not independently reproduced. The extension is not a sandbox or complete permission boundary.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/DevMortimer/pi-warden) · [实现或文档](https://github.com/DevMortimer/pi-warden/blob/main/README.md)

Pi 扩展将修改与项目规则对照，把反馈加入 Agent 上下文；其他检查覆盖任务偏离、缺少证据的完成声明及风险动作，由确定性模式和模型判断共同触发代码策略。

**实现模式：** Agent 上下文与拟议修改 → 规则及风险检查 → 反馈或特定拦截。

**边界：** 很多问题只提醒或引导，不会阻断。作者的 150 组配对运行报告规则违规减少，但其他指标改善有限或没有改善，未独立复现；该扩展不是沙箱或完整权限边界。

**核查日期：** 2026-09-18。

