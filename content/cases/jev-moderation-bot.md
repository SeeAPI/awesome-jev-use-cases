---
id: jev-moderation-bot
category: moderation
order: 20
title:
  en: Jev Moderation Bot
  zh: Jev Moderation Bot
source_url: https://github.com/brainstormity/Jev-Moderation-Bot
legacy_anchors:
  en:
  - 2-jev-moderation-bot
  zh:
  - 2-jev-moderation-bot
---

<!-- case:en -->

[Repository](https://github.com/brainstormity/Jev-Moderation-Bot)

A Discord moderation bot that evaluates messages and context for phishing, spam, and social engineering. Code applies escalating actions, and moderator corrections become safe precedents in later judgment context.

**Pattern:** contextual message classification → moderation action → feedback.

**Scope:** a text-message moderation project, not an image or video NSFW benchmark. False-positive performance has not been independently verified here.

<!-- case:zh -->

- **场景**：Discord 社区中的钓鱼、垃圾信息及社交工程消息审核。
- **做法**：结合消息正文、账号与频道等上下文判断风险，由程序执行分级处置；管理员纠正的误报作为后续判断的上下文。
- **可借鉴点**：检测、处置、申诉、反馈样本形成完整流程。
- **边界**：这里核实的是文字消息审核方案，不是图片或视频 NSFW 模型；未独立测量误报率。
- **来源**：[项目 README](https://github.com/brainstormity/Jev-Moderation-Bot)。

