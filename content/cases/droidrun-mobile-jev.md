---
id: droidrun-mobile-jev
category: automation
order: 150
title:
  en: Mobile Jev
  zh: Mobile Jev
source_url: https://github.com/droidrun/mobile-jev
legacy_anchors:
  en:
  - 15-mobile-jev
  - 11-mobile-jev
  zh:
  - 15-mobile-jev
  - 11-mobile-jev
---

<!-- case:en -->

[Project](https://github.com/droidrun/mobile-jev) · [Discovery post](https://x.com/studio_yebisu/status/2100686990090047569)

A mobile agent uses Jev to select actions on a real Android device through Mobilerun, with a studio, CLI, and execution traces.

**Pattern:** Goal → mobile state → action selection → device execution.

**Scope:** The documented Uber demo reaches payment selection, not a completed booking. The reported 21 seconds for nine actions is one recorded task, not a general latency guarantee.

**Demo material**: [Android demo: Uber route to payment selection](https://github.com/droidrun/mobile-jev/blob/main/docs/media/uber-demo.mp4)

<img src="../../assets/cases/droidrun__mobile-jev.jpg" alt="Android Uber demonstration" width="720" />

Original author material: Android Uber demonstration. Measurements shown are author-reported, not SeeAPI tests. MIT · [Source](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/docs/media/uber-demo.jpg) · [License and attribution](../../THIRD_PARTY_NOTICES.md)

<!-- case:zh -->

- **场景与做法**：通过 Mobilerun 在真实 Android 设备上运行，由 Jev 选择操作，提供可视化工作台、CLI 和执行轨迹。
- **可借鉴点**：目标 → 手机状态 → 动作选择 → 设备执行。
- **边界**：README 中的 Uber 演示到达支付方式选择，未展示完成叫车；约 21 秒、9 个动作是单次演示数据。
- **来源**：[项目](https://github.com/droidrun/mobile-jev) · [发现来源帖子](https://x.com/studio_yebisu/status/2100686990090047569)。

**演示素材**: [Android 演示：Uber 路线输入至支付方式选择](https://github.com/droidrun/mobile-jev/blob/main/docs/media/uber-demo.mp4)

<img src="../../assets/cases/droidrun__mobile-jev.jpg" alt="Android Uber 演示" width="720" />

原作者素材：Android Uber 演示；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/docs/media/uber-demo.jpg) · [许可与署名](../../THIRD_PARTY_NOTICES.md)

