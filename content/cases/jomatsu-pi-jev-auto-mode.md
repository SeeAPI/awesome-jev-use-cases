---
id: jomatsu-pi-jev-auto-mode
category: automation
order: 230
title:
  en: Pi Jev Auto Mode — tool-call probability gate
  zh: Pi Jev Auto Mode — 工具调用概率门控
source_url: https://github.com/jomatsu/pi-jev-auto-mode
legacy_anchors:
  en:
  - 23-pi-jev-auto-mode--tool-call-probability-gate
  zh:
  - 23-pi-jev-auto-mode--工具调用概率门控
---

<!-- case:en -->

[Source](https://github.com/jomatsu/pi-jev-auto-mode) · [Implementation / documentation](https://github.com/jomatsu/pi-jev-auto-mode/blob/main/src/settings.ts)

A Pi extension combines deterministic command rules with Jev judgments before bash, write, and edit calls. Code compares condition probabilities with thresholds to produce allow, deny, or uncertain decisions.

**Pattern:** Tool call → deterministic checks → semantic conditions → local execution gate.

**Scope:** At review, README describes blocking uncertain results, while src/settings.ts sets uncertain to allow; src/jev/decide.ts treats an uncertain hazard-mode condition as satisfied. Check the actual version and policy rather than assuming fail-closed behavior. No safety guarantee or runtime validation is established here.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/jomatsu/pi-jev-auto-mode) · [实现或文档](https://github.com/jomatsu/pi-jev-auto-mode/blob/main/src/settings.ts)

Pi 扩展在 bash、write、edit 调用前组合确定性规则与 Jev 语义判断，由代码将条件概率与阈值比较，得到允许、拒绝或不确定的决策。

**实现模式：** 工具调用 → 确定性检查 → 语义条件判断 → 本地执行门控。

**边界：** 核查时 README 称不确定结果会被阻止，但 src/settings.ts 默认 uncertain 为 allow，src/jev/decide.ts 将 hazard 模式的不确定条件按满足处理。需核对实际版本与策略，不能默认失败关闭；本轮未运行，也不构成安全保证。

**核查日期：** 2026-09-18。

