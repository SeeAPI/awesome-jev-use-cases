---
id: valentynkit-jev-plays-pokemon-red
category: experiments
order: 740
title:
  en: jev-plays-pokemon-red — bounded game decisions on PyBoy
  zh: jev-plays-pokemon-red — PyBoy 上的受限游戏决策
source_url: https://github.com/valentynkit/jev-plays-pokemon-red
legacy_anchors:
  en:
  - 74-jev-plays-pokemon-red--bounded-game-decisions-on-pyboy
  zh:
  - 74-jev-plays-pokemon-red--pyboy-上的受限游戏决策
---

<!-- case:en -->

[Repository](https://github.com/valentynkit/jev-plays-pokemon-red)

A Pokémon Red experiment reads emulator RAM into structured state. Deterministic Python handles routes, battle arithmetic, and legal actions; Jev selects among candidates at branch points. The harness records turn-level faint predictions and outcomes for later Brier-score evaluation.

**Pattern:** RAM-derived state and legal candidates → branch-point judgment → emulator action and outcome recording.

**Scope:** This is a code-guided experiment, not autonomous long-horizon planning or screenshot-based play. The author explicitly withholds calibration results because the labeled sample is too small; an evaluation mechanism does not establish calibrated probabilities. No gameplay or measurements were reproduced here.

**Reviewed:** 2026-09-19 (author documentation; no execution).

<!-- case:zh -->

[项目来源](https://github.com/valentynkit/jev-plays-pokemon-red)

宝可梦红实验从模拟器 RAM 提取结构化状态，确定性 Python 代码负责路线、战斗运算及合法动作，Jev 仅在分支点从候选中选择。框架记录逐回合倒下概率预测及实际结果，以供后续计算 Brier 分数。

**实现模式：** RAM 状态与合法候选 → 分支点判断 → 模拟器动作与结果记录。

**边界：** 这是代码引导的实验，不是自主长程规划或基于截图的游戏操作。作者明确因标注样本过少而尚未公布概率校准结果；提供评测机制不代表已证明概率可靠。本次未复现游戏流程或测量结果。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

