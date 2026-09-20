---
id: emrickgarrett-onevonejev
category: experiments
order: 620
title:
  en: 1v1 Jev — Quickscope Arena
  zh: 1v1 Jev — Quickscope Arena
source_url: https://github.com/emrickgarrett/OneVOneJev
legacy_anchors:
  en:
  - 62-1v1-jev--quickscope-arena
  - 41-1v1-jev--quickscope-arena
  zh:
  - 62-1v1-jev--quickscope-arena
  - 41-1v1-jev--quickscope-arena
---

<!-- case:en -->

[Repository](https://github.com/emrickgarrett/OneVOneJev)

A browser FPS opponent controlled through Choice/Noul questions about movement, aim, ADS, firing, and jumping. The server supplies structured game state and includes a heuristic fallback.

**Pattern:** repeated bounded decisions drive a real-time interactive agent.

**Scope:** the README's approximately 9 Hz loop describes this project, not a universal Jev performance figure. The agent is not shown to operate from raw visual input alone.

<!-- case:zh -->

- **场景**：浏览器 FPS 游戏中控制对手移动、瞄准、射击等动作。
- **做法**：服务端将结构化游戏状态转换为 Choice/Noul 问题；README 描述决策频率约为 9 Hz，并提供模型不可用时的启发式回退。
- **可借鉴点**：展示连续小决策组成实时交互的方式。
- **边界**：9 Hz 是该项目的决策循环描述，不是所有 Jev 请求的通用性能指标；不是纯视觉游戏控制证据。
- **来源**：[项目 README](https://github.com/emrickgarrett/OneVOneJev)。

