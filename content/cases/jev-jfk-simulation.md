---
id: jev-jfk-simulation
category: experiments
order: 710
title:
  en: Jev JFK Simulation — voice-driven airport demo
  zh: Jev JFK Simulation — 机场语音调度演示
source_url: https://www.reddit.com/r/AgentZero/comments/1wj6li0/i_tested_typesafes_jev_model_and_made_it_run_a/
legacy_anchors:
  en:
  - 71-jev-jfk-simulation--voice-driven-airport-demo
  zh:
  - 71-jev-jfk-simulation--机场语音调度演示
---

<!-- case:en -->

[Source](https://www.reddit.com/r/AgentZero/comments/1wj6li0/i_tested_typesafes_jev_model_and_made_it_run_a/)

An author demonstration combines a simulated JFK airport with real-time voice models for radio interaction and Jev for operational judgments. It illustrates separating voice interaction from a bounded decision loop.

**Pattern:** Simulated airport state and radio interaction → Jev judgment → simulated response.

**Scope:** Evidence is the author’s public post and demonstration; no public implementation or complete request trace was verified. It is a simulation, not evidence of real air-traffic-control capability. Timing and judgment quality were not measured here.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://www.reddit.com/r/AgentZero/comments/1wj6li0/i_tested_typesafes_jev_model_and_made_it_run_a/)

作者演示将 JFK 机场仿真、负责无线电交互的实时语音模型，以及负责运行判断的 Jev 组合起来，展示语音交互与有限决策循环的分工。

**实现模式：** 仿真机场状态与无线电交互 → Jev 判断 → 仿真响应。

**边界：** 证据为作者公开帖与演示，未核实公开实现或完整请求记录；仅为仿真，不能作为真实空管能力证据。本轮未测量时延或判断质量。

**核查日期：** 2026-09-18。

