---
id: jev-ultrafast
category: automation
order: 90
title:
  en: Jev Ultrafast
  zh: Jev Ultrafast
source_url: https://github.com/browser-use/jev-ultrafast
legacy_anchors:
  en:
  - 9-jev-ultrafast
  - 5-jev-ultrafast
  zh:
  - 9-jev-ultrafast
  - 5-jev-ultrafast
---

<!-- case:en -->

[Repository and measurement notes](https://github.com/browser-use/jev-ultrafast)

A browser agent that turns visible controls into indexed candidates. Jev chooses an operation and target; a separate language model writes text when needed.

**Pattern:** observed state → bounded action selection → execution → observation.

**Scope:** the reported roughly 7.1-second flight search is a specific author-measured run, timed after the initial page observation. It is not a general browser-task speed guarantee.

**Demo material**: [Original flight-search demo](https://github.com/browser-use/jev-ultrafast/blob/main/docs/demo.mp4)

<img src="../../assets/cases/browser-use__jev-ultrafast.png" alt="Flight-search result" width="720" />

Original author material: Flight-search result. Measurements shown are author-reported, not SeeAPI tests. MIT · [Source](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/docs/flights-result.png) · [License and attribution](../../THIRD_PARTY_NOTICES.md)

<!-- case:zh -->

- **场景**：浏览器中逐步完成查询、点击与表单输入。
- **做法**：将可见页面控件整理成带索引的候选集合，Jev 选择操作与目标；需要输入文字时再调用文字生成模型。
- **可借鉴点**：把“选择动作”和“生成文字”拆开，缩小每次决策范围。
- **边界**：作者报告的约 7.1 秒航班搜索是特定任务演示，计时从首次页面观察之后开始，不是任意网页任务的速度保证。
- **来源**：[项目与测量边界](https://github.com/browser-use/jev-ultrafast)。

**演示素材**: [原作者航班搜索演示](https://github.com/browser-use/jev-ultrafast/blob/main/docs/demo.mp4)

<img src="../../assets/cases/browser-use__jev-ultrafast.png" alt="航班搜索结果" width="720" />

原作者素材：航班搜索结果；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/docs/flights-result.png) · [许可与署名](../../THIRD_PARTY_NOTICES.md)

