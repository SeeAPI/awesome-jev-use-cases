---
id: valentynkit-jev-belay
category: routing
order: 370
title:
  en: jev-belay — completion checks for Claude Code
  zh: jev-belay — Claude Code 完成声明核查
source_url: https://github.com/valentynkit/jev-belay
legacy_anchors:
  en:
  - 37-jev-belay--completion-checks-for-claude-code
  zh:
  - 37-jev-belay--claude-code-完成声明核查
---

<!-- case:en -->

[Repository](https://github.com/valentynkit/jev-belay)

A Claude Code Stop hook inspects the current turn’s transcript for file changes and verification evidence. When changes lack a subsequent passing check, it asks Jev four questions about the closing message; local thresholds and repetition limits determine whether to allow the stop or return feedback.

**Pattern:** Local transcript evidence → conditional Jev judgment → allow stop or request follow-up.

**Scope:** Errors fail open. Turns without detected edits, subagent work in separate transcripts, and unrecognized verification commands can escape the gate. Detection accuracy has not been established by this collection; the published demo uses fake model answers. It is a completion-feedback tool, not proof that work is correct.

**Reviewed:** 2026-09-19 (author documentation; no execution).

<!-- case:zh -->

[项目来源](https://github.com/valentynkit/jev-belay)

Claude Code 的 Stop 钩子先从当前轮次会话记录中识别文件改动与验证证据；有改动且之后没有通过的检查时，再向 Jev 提出四个关于结束消息的问题，由本地阈值及重复阻断限制决定放行或返回反馈。

**实现模式：** 本地会话证据 → 有条件的 Jev 判断 → 允许结束或要求后续检查。

**边界：** 出错时放行。未检测到文件编辑的轮次、独立记录中的子代理工作及无法识别的验证命令可能漏检。本仓库未验证检测准确率，公开演示使用模拟模型回答；该工具提供完成声明反馈，不能证明任务正确完成。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

