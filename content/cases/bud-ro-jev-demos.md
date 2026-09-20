---
id: bud-ro-jev-demos
category: benchmarks
order: 830
title:
  en: Jev Maze Lookahead — a negative planning experiment
  zh: Jev Maze Lookahead — 并行多步规划负向实验
source_url: https://github.com/Bud-ro/jev-demos
legacy_anchors:
  en:
  - 83-jev-maze-lookahead--a-negative-planning-experiment
  zh:
  - 83-jev-maze-lookahead--并行多步规划负向实验
---

<!-- case:en -->

[Source](https://github.com/Bud-ro/jev-demos) · [Implementation / documentation](https://github.com/Bud-ro/jev-demos/blob/main/packages/maze_lookahead/README.md)

A maze experiment compares parallel future-step questions with single-step decisions and explicit adjacent-tile hints. The project separates a deterministic BFS mock from real-API runs.

**Pattern:** Maze state → proposed moves → environment checks → recorded successes and failures.

**Scope:** The author reports zero solved mazes in the quick multi-step setting; with adjacency hints and one next-move question, 6 of 10 small 5×5 mazes were solved. These are configuration-specific author results, not a reproduced general limit on spatial reasoning.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/Bud-ro/jev-demos) · [实现或文档](https://github.com/Bud-ro/jev-demos/blob/main/packages/maze_lookahead/README.md)

迷宫实验对比并行询问未来多步与单步决策，并测试相邻格提示；项目明确区分确定性 BFS Mock 与真实 API 运行。

**实现模式：** 迷宫状态 → 候选动作判断 → 环境检查 → 记录成功与失败。

**边界：** 作者报告 quick 多步配置未解出迷宫；加入邻格提示且只问下一步后，十个 5×5 迷宫解出六个。这是特定配置下的作者结果，本轮未复跑，不能泛化为所有空间推理任务。

**核查日期：** 2026-09-18。

