---
id: xiechengyuan-jev-gomoku
category: experiments
order: 730
title:
  en: Jev Gomoku — candidate-move selection
  zh: Jev Gomoku — 五子棋候选落点选择
source_url: https://github.com/XieChengYuan/jev-gomoku
legacy_anchors:
  en:
  - 73-jev-gomoku--candidate-move-selection
  zh:
  - 73-jev-gomoku--五子棋候选落点选择
---

<!-- case:en -->

[Project](https://github.com/XieChengYuan/jev-gomoku) · [Discovery source](https://x.com/fakeWow_/status/2100889184861110572)

A nine-board Gomoku experiment supplies textual board state and code-generated candidate moves to Jev. Each move uses a Choice question; five input configurations explore the effect of tactical facts, coordinates, directional lines, and short lookahead.

**Pattern:** Board state → deterministic candidate generation → Choice → legal move execution.

**Scope:** Jev selects from heuristic candidates rather than all empty squares. Choice probabilities are not game-winning probabilities. The hosted demo replays recorded decisions; live play requires API access. The small experiment does not establish general playing strength or superiority of one input format.

**Reviewed:** 2026-09-19 (author documentation; no execution).

**Demo material:** [Author recorded-game replay](https://xiechengyuan.github.io/jev-gomoku/). Original author material, linked only; not SeeAPI test results.

<!-- case:zh -->

[项目](https://github.com/XieChengYuan/jev-gomoku) · [发现来源](https://x.com/fakeWow_/status/2100889184861110572)

九棋盘五子棋实验将文本棋盘及代码生成的候选落点交给 Jev，每步使用一个 Choice 问题；通过五种输入配置探索战术事实、坐标、方向棋线及短程前瞻的影响。

**实现模式：** 棋盘状态 → 确定性候选生成 → Choice 选择 → 合法落子执行。

**边界：** Jev 从启发式候选中选择，而非考虑全部空位；Choice 概率不等于最终获胜概率。在线演示重放已记录的判断，实时对弈需要 API 接入；小规模实验不能证明普遍棋力或某种输入格式更优。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

**演示素材：** [作者已录制对局回放](https://xiechengyuan.github.io/jev-gomoku/)。原作者素材，仅提供外链，不代表 SeeAPI 实测。

