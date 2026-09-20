---
id: fhshaik-typesafe-mario
category: experiments
order: 640
title:
  en: TypeSafe Mario
  zh: TypeSafe Mario
source_url: https://github.com/fhshaik/typesafe-mario
legacy_anchors:
  en:
  - 64-typesafe-mario
  zh:
  - 64-typesafe-mario
---

<!-- case:en -->

[Project](https://github.com/fhshaik/typesafe-mario) · [Discovery post](https://x.com/yibie/status/2100619188062523695)

An emulator harness converts telemetry and RAM into structured state; Jev selects NES controller actions and provides jump and danger judgments.

**Pattern:** Structured game state → Choice/Noul/Score → controller input.

**Scope:** The model does not receive screenshots. This is an experimental controller, not evidence of general visual game-playing ability.

<!-- case:zh -->

- **场景与做法**：将模拟器遥测与内存状态转换为结构化信息，Jev 选择 NES 手柄动作，并给出跳跃和危险程度判断。
- **可借鉴点**：结构化游戏状态 → Choice/Noul/Score → 手柄输入。
- **边界**：模型不接收截图；这是实验性控制器，不能作为通用视觉游戏能力的证据。
- **来源**：[项目](https://github.com/fhshaik/typesafe-mario) · [发现来源帖子](https://x.com/yibie/status/2100619188062523695)。

