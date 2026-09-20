---
id: maxim-saplin-llm-chess
category: benchmarks
order: 810
title:
  en: LLM Chess Jev Player — constrained chess evaluation
  zh: LLM Chess Jev Player — 合法棋步选择评测
source_url: https://github.com/maxim-saplin/llm_chess
legacy_anchors:
  en:
  - 81-llm-chess-jev-player--constrained-chess-evaluation
  zh:
  - 81-llm-chess-jev-player--合法棋步选择评测
---

<!-- case:en -->

[Source](https://github.com/maxim-saplin/llm_chess) · [Implementation / documentation](https://github.com/maxim-saplin/llm_chess/blob/29b5bdaf9dd844134f2c89588642bb4d61703e73/README.md#typesafe-jev-request--response)

An adapter adds Jev to an existing chess evaluation framework. For each move, application code provides the FEN position, side to move, and legal UCI candidates; a Choice answer is converted into a make_move action.

**Pattern:** Board state and legal moves → Choice → move execution and game records.

**Scope:** Legal candidates are supplied by code, so protocol success does not establish chess strength. Jev and dialog-model players use different interaction protocols; rankings do not establish general reasoning ability. Games and author measurements were not reproduced.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/maxim-saplin/llm_chess) · [实现或文档](https://github.com/maxim-saplin/llm_chess/blob/29b5bdaf9dd844134f2c89588642bb4d61703e73/README.md#typesafe-jev-request--response)

适配器将 Jev 接入既有国际象棋评测框架。每一步由代码提供 FEN 棋局、行棋方和合法 UCI 候选，Choice 的答案转为 make_move 动作。

**实现模式：** 棋局与合法候选 → Choice → 执行棋步并记录对局。

**边界：** 合法候选由代码提供，协议成功不等于棋力。Jev 与对话模型使用不同交互协议，排名不能证明通用推理能力；本轮未复跑对局或复现作者数据。

**核查日期：** 2026-09-18。

