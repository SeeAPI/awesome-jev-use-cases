---
id: valentynkit-jev-skip
category: automation
order: 240
title:
  en: jev-skip — caption-based sponsor detection
  zh: jev-skip — 基于字幕的赞助片段识别
source_url: https://github.com/valentynkit/jev-skip
legacy_anchors:
  en:
  - 24-jev-skip--caption-based-sponsor-detection
  zh:
  - 24-jev-skip--基于字幕的赞助片段识别
---

<!-- case:en -->

[Repository](https://github.com/valentynkit/jev-skip)

A browser extension sends YouTube captions to Jev for sponsor-probability judgments on time segments. Local code displays a seek-bar heatmap and can skip selected segments without relying on a crowdsourced timestamp database.

**Pattern:** Caption text → segment judgments → seek-bar overlay and optional skipping.

**Scope:** No captions means no analysis; this is text classification, not audio or video understanding. The author reports 77% coverage of SponsorBlock-labeled sponsor seconds across 23 videos, with 34 seconds of false skips per hour and $0.0008 per video. These gateway-based measurements were not independently reproduced. The demo replays recorded answers; Jev API calls are still required for new judgments.

**Reviewed:** 2026-09-19 (author documentation; no execution).

<!-- case:zh -->

[项目来源](https://github.com/valentynkit/jev-skip)

浏览器扩展将 YouTube 字幕发送给 Jev，判断各时间片段的赞助概率，再由本地代码显示进度条热力图并按设置跳过片段，不依赖众包时间戳数据库。

**实现模式：** 字幕文本 → 片段判断 → 进度条标记与可选跳过。

**边界：** 没有字幕就不分析；这是文本分类，不是音视频理解。作者以 23 个视频的 SponsorBlock 标注为参照，报告覆盖 77% 的赞助时长，同时每小时误跳过 34 秒、每视频成本约 0.0008 美元。这些经网关取得的数据未经独立复现；演示使用已录制回答回放，新判断仍需调用 Jev API。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

