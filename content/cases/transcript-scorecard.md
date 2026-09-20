---
id: transcript-scorecard
category: productivity
order: 550
title:
  en: Transcript Scorecard — incremental call evaluation
  zh: Transcript Scorecard — 实时客服通话质检
source_url: https://github.com/brandonbryant12/transcript-scorecard
legacy_anchors:
  en:
  - 55-transcript-scorecard--incremental-call-evaluation
  zh:
  - 55-transcript-scorecard--实时客服通话质检
---

<!-- case:en -->

[Source](https://github.com/brandonbryant12/transcript-scorecard) · [Implementation / documentation](https://github.com/brandonbryant12/transcript-scorecard/blob/c9232fffbf8bf23b7cf5402dd02ebc54b19eb9cf/apps/api/src/classifier.ts)

A proof of concept replays fictional support-call transcripts incrementally. Each enabled criterion contributes a Score and a Choice selecting an evidence sentence; code normalizes and weights the results, then stores the final evaluation in SQLite.

**Pattern:** Growing transcript → criterion scores and evidence selection → weighted score history.

**Scope:** This is transcript replay, not verified live audio recognition. Evaluations send the current transcript prefix to TypeSafe; costs can grow with the conversation. The documented local demo has no authentication. Scoring quality and timing were not reproduced.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/brandonbryant12/transcript-scorecard) · [实现或文档](https://github.com/brandonbryant12/transcript-scorecard/blob/c9232fffbf8bf23b7cf5402dd02ebc54b19eb9cf/apps/api/src/classifier.ts)

概念验证项目逐句重放虚构客服通话文本。每个启用维度对应一个 Score 和一个选择证据句的 Choice，由代码归一化、加权，并将最终评估存入 SQLite。

**实现模式：** 逐步增长的转写文本 → 维度评分与证据句 → 加权评分历史。

**边界：** 展示的是文本重放，不能视为已验证的实时语音识别。每次评估发送当前转写前缀，费用可能随对话增长；文档说明本地演示无认证。未复现评分质量或时延。

**核查日期：** 2026-09-18。

