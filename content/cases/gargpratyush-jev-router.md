---
id: gargpratyush-jev-router
category: routing
order: 280
title:
  en: jev-router — gargpratyush
  zh: jev-router — gargpratyush
source_url: https://github.com/gargpratyush/jev-router
legacy_anchors:
  en:
  - 28-jev-router--gargpratyush
  - 20-jev-router--gargpratyush
  zh:
  - 28-jev-router--gargpratyush
  - 20-jev-router--gargpratyush
---

<!-- case:en -->

[Project](https://github.com/gargpratyush/jev-router) · [Discovery post](https://x.com/studio_yebisu/status/2100686990090047569)

Routes fresh user turns in Claude Code and Codex to fast or strong model tiers while launching the original CLIs.

**Pattern:** Classify a turn and select a model without replacing the CLI.

**Scope:** A separate project from Jev Codex Router by 0xNatoshi. Its README describes per-user-turn routing, not a fresh model choice for every internal tool step.

<img src="../../assets/cases/gargpratyush__jev-router.png" alt="Model selection interface" width="720" />

Original author material: Model selection interface. Measurements shown are author-reported, not SeeAPI tests. MIT · [Source](https://github.com/gargpratyush/jev-router/blob/86660a0248eba0e4523f81645ac2925e9808c000/docs/model-picker.png) · [License and attribution](../../THIRD_PARTY_NOTICES.md)

<!-- case:zh -->

- **场景与做法**：启动原生 Claude Code 或 Codex CLI，并在新用户轮次开始时按任务难度选择快速或强能力模型。
- **可借鉴点**：判断当前轮次的任务，再选择执行模型。
- **边界**：与 0xNatoshi 的 Jev Codex Router 是不同项目；README 描述的是按新用户轮次路由，不是每个内部工具步骤重新选择。
- **来源**：[项目](https://github.com/gargpratyush/jev-router) · [发现来源帖子](https://x.com/studio_yebisu/status/2100686990090047569)。

<img src="../../assets/cases/gargpratyush__jev-router.png" alt="模型选择界面" width="720" />

原作者素材：模型选择界面；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/gargpratyush/jev-router/blob/86660a0248eba0e4523f81645ac2925e9808c000/docs/model-picker.png) · [许可与署名](../../THIRD_PARTY_NOTICES.md)

