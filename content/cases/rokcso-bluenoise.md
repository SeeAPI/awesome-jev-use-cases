---
id: rokcso-bluenoise
category: moderation
order: 80
title:
  en: BlueNoise — X reply noise filtering
  zh: BlueNoise — X 评论区噪声过滤
source_url: https://github.com/rokcso/bluenoise
legacy_anchors:
  en:
  - 8-bluenoise--x-reply-noise-filtering
  zh:
  - 8-bluenoise--x-评论区噪声过滤
---

<!-- case:en -->

[Project](https://github.com/rokcso/bluenoise) · [Discovery source](https://github.com/logicrw/awesome-jev-projects/issues/3)

A browser extension combines local keyword and account rules with an optional Jev noise assessment for replies that local rules do not match. Code uses the judgment to filter replies on X.

**Pattern:** Local rules → remaining reply text and context → noise probability → display policy.

**Scope:** The Jev option is experimental and disabled by default. Enabling it sends reply text to TypeSafe; the default local-only behavior does not describe that mode. Filtering quality was not independently tested.

**Reviewed:** 2026-09-19 (author documentation; no execution).

**Demo material:** [Author screenshots and feature description](https://x.com/rokcso/status/2100876608340910548). Original author material, linked only; not SeeAPI test results.

<!-- case:zh -->

[项目](https://github.com/rokcso/bluenoise) · [发现来源](https://github.com/logicrw/awesome-jev-projects/issues/3)

浏览器扩展先使用本地关键词和账号规则，再通过可选的 Jev 功能，对未匹配规则的 X 回复进行噪声判断，由代码据此过滤回复。

**实现模式：** 本地规则 → 剩余回复文本及上下文 → 噪声概率 → 展示策略。

**边界：** Jev 功能仍属实验选项，默认关闭；启用后会将回复文本发送给 TypeSafe，因此默认模式的纯本地处理说明不适用于该模式。本次未独立测试过滤效果。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

**演示素材：** [作者截图与功能介绍](https://x.com/rokcso/status/2100876608340910548)。原作者素材，仅提供外链，不代表 SeeAPI 实测。

