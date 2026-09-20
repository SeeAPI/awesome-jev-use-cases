---
id: grayrepo-byte-jev-filter-for-x
category: productivity
order: 580
title:
  en: JevFilterForX — timeline value scoring
  zh: JevFilterForX — 时间线内容价值评分
source_url: https://github.com/grayrepo-byte/jev_filter_for_x
legacy_anchors:
  en:
  - 58-jevfilterforx--timeline-value-scoring
  zh:
  - 58-jevfilterforx--时间线内容价值评分
---

<!-- case:en -->

[Project](https://github.com/grayrepo-byte/jev_filter_for_x) · [Discovery source](https://x.com/0xLogicrw/status/2100861912590205411)

An X extension asks Jev to score signal, actionability, and originality. Local weighting produces a 0–100 value score, while topic and noise labels support filtering and focus modes.

**Pattern:** Post text → rubric scores and labels → weighted score → timeline filtering.

**Scope:** This is timeline scoring, distinct from BlueNoise’s reply filtering and Jevibe Check’s Bluesky labels. Without an API key it uses mock results. Collapsing attached media does not establish that Jev understands images or video; scoring quality was not tested.

**Reviewed:** 2026-09-19 (author documentation; no execution).

**Demo material:** [Author demo video](https://github.com/grayrepo-byte/jev_filter_for_x/blob/main/assets/promo/jevfilterforx-promo.mp4) · [Poster](https://github.com/grayrepo-byte/jev_filter_for_x/blob/main/assets/promo/jevfilterforx-promo-poster.png). Original author material, linked only; not SeeAPI test results.

<!-- case:zh -->

[项目](https://github.com/grayrepo-byte/jev_filter_for_x) · [发现来源](https://x.com/0xLogicrw/status/2100861912590205411)

X 扩展让 Jev 按信息量、可操作性和原创性评分，再由本地权重计算 0–100 分的内容价值；主题和噪声标签另用于过滤及专注模式。

**实现模式：** 帖子文本 → 多维评分与标签 → 加权分数 → 时间线过滤。

**边界：** 侧重时间线评分，与 BlueNoise 的回复过滤及 Jevibe Check 的 Bluesky 标签不同。没有 API 密钥时使用模拟结果；随帖子折叠图片或视频，不代表 Jev 具有相应视觉理解能力。本次未测试评分质量。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

**演示素材：** [作者演示视频](https://github.com/grayrepo-byte/jev_filter_for_x/blob/main/assets/promo/jevfilterforx-promo.mp4) · [封面](https://github.com/grayrepo-byte/jev_filter_for_x/blob/main/assets/promo/jevfilterforx-promo-poster.png)。原作者素材，仅提供外链，不代表 SeeAPI 实测。

