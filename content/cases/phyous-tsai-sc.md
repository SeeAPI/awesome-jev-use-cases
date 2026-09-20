---
id: phyous-tsai-sc
category: experiments
order: 660
title:
  en: tsai-sc — StarCraft Strongarm
  zh: tsai-sc — StarCraft Strongarm
source_url: https://github.com/phyous/tsai-sc
legacy_anchors:
  en:
  - 66-tsai-sc--starcraft-strongarm
  - 45-tsai-sc--starcraft-strongarm
  zh:
  - 66-tsai-sc--starcraft-strongarm
  - 45-tsai-sc--starcraft-strongarm
---

<!-- case:en -->

[Project](https://github.com/phyous/tsai-sc) · [Discovery post](https://x.com/yibie/status/2100619188062523695)

A harness reads structured game state, asks Jev to choose commands, and executes mouse and keyboard actions in the original StarCraft shareware mission Strongarm.

**Pattern:** Structured strategy-game state → command selection → input execution.

**Scope:** The game pauses during state reads and inference. The author provides completion evidence for a bounded mission; this is not a real-time competitive-play benchmark or pixel-only agent.

**Demo material**: [Original videos and evidence bundle (1× and 8× playback)](https://github.com/phyous/tsai-sc/releases/tag/v0.1.0)

<!-- case:zh -->

- **场景与做法**：读取星际争霸试玩版 Strongarm 任务的结构化游戏状态，由 Jev 选择指令，再以鼠标键盘执行。
- **可借鉴点**：结构化策略游戏状态 → 指令选择 → 输入执行。
- **边界**：读取状态和推理时游戏会暂停；作者提供了限定任务的完成证据，并非实时竞技评测，也不是纯像素输入 Agent。
- **来源**：[项目](https://github.com/phyous/tsai-sc) · [发现来源帖子](https://x.com/yibie/status/2100619188062523695)。

**演示素材**: [原作者视频与证据包（含原速及 8 倍速）](https://github.com/phyous/tsai-sc/releases/tag/v0.1.0)

