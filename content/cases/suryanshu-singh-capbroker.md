---
id: suryanshu-singh-capbroker
category: moderation
order: 50
title:
  en: Capbroker — advisory screening around capability controls
  zh: Capbroker — 权限边界之外的Jev风险提示
source_url: https://github.com/suryanshu-singh/capbroker
legacy_anchors:
  en:
  - 5-capbroker--advisory-screening-around-capability-controls
  zh:
  - 5-capbroker--权限边界之外的jev风险提示
---

<!-- case:en -->

[Source](https://github.com/suryanshu-singh/capbroker) · [Implementation / documentation](https://github.com/suryanshu-singh/capbroker/blob/f7532aa83e376ad9fbc0bfbb92ada2a2a53c1999/README.md#jev-powered-defense-in-depth-advisory-only--read-this-carefully)

A capability broker optionally uses Jev to flag suspicious MCP tool output and show risk advice at a human-approval prompt. Deterministic capability checks and the human approval decision remain separate from the model advice.

**Pattern:** Capability enforcement → optional content warning or risk advice → human decision where required.

**Scope:** The Jev layer is advisory and does not make the broker’s permission decision. The author’s attack demos use a fake upstream and test credentials. Missing warnings do not establish safety, and permitted operations can still be misused. Not executed here.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/suryanshu-singh/capbroker) · [实现或文档](https://github.com/suryanshu-singh/capbroker/blob/f7532aa83e376ad9fbc0bfbb92ada2a2a53c1999/README.md#jev-powered-defense-in-depth-advisory-only--read-this-carefully)

能力权限代理可选用 Jev 标注可疑 MCP 工具输出，并在人工审批提示中展示风险建议。确定性权限校验与人工审批独立于模型建议。

**实现模式：** 能力权限校验 → 可选内容警告或风险建议 → 必要时人工裁决。

**边界：** Jev 只提供建议，不决定代理的权限放行。作者攻击演示使用假上游及测试凭据；没有警告不代表安全，权限范围内的动作仍可能被滥用。本轮未执行。

**核查日期：** 2026-09-18。

