---
id: openroom
category: moderation
order: 60
title:
  en: Openroom — editable chat-moderation rules
  zh: Openroom — 可改规则的实时聊天审核
source_url: https://openroom-ivory.vercel.app
legacy_anchors:
  en:
  - 6-openroom--editable-chat-moderation-rules
  zh:
  - 6-openroom--可改规则的实时聊天审核
---

<!-- case:en -->

[Source](https://openroom-ivory.vercel.app) · [Implementation / documentation](https://x.com/stoufax/status/2100899469843673218)

The author describes a chat application using Jev, Convex, and Vercel to review messages before display. Natural-language room rules can be edited to trigger re-evaluation, with uncertain messages held for human review.

**Pattern:** Message and room rules → moderation judgment → display or human-review queue.

**Scope:** This entry is based on the author’s public description, not a verified backend implementation. No messages were submitted or rules saved during this review; thresholds and moderation accuracy remain unverified.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://openroom-ivory.vercel.app) · [实现或文档](https://x.com/stoufax/status/2100899469843673218)

作者介绍的聊天应用使用 Jev、Convex 与 Vercel，在消息展示前审核；自然语言房间规则修改后可重新判断，不确定消息转交人工。

**实现模式：** 消息与房间规则 → 审核判断 → 展示或人工复核队列。

**边界：** 依据作者公开说明收录，未验证后端实现；本轮未发送消息或保存规则，阈值与审核准确率未经验证。

**核查日期：** 2026-09-18。

