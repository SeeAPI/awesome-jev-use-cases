# Transcript Scorecard — incremental call evaluation

[Read the full case](../docs/casebook.md#case-transcript-scorecard) · [阅读完整案例](../docs/casebook.zh-CN.md#case-transcript-scorecard)

Metadata reference; the Casebook is the main reading entry.

A proof of concept replays fictional support-call transcripts incrementally. Each enabled criterion contributes a Score and a Choice selecting an evidence sentence; code normalizes and weights the results, then stores the final evaluation in SQLite.

**Evidence:** `docs-reviewed` · **Reviewed:** 2026-09-18 · **Live-tested by SeeAPI:** no

**Primitive:** choice, score · **Action:** score, review

[Original source](https://github.com/brandonbryant12/transcript-scorecard) · [Full case](../docs/casebook.md#case-transcript-scorecard) · [Data record](../data/cases/transcript-scorecard.json)

## Limits

- This is transcript replay, not verified live audio recognition. Evaluations send the current transcript prefix to TypeSafe; costs can grow with the conversation. The documented local demo has no authentication. Scoring quality and timing were not reproduced.

## 中文

概念验证项目逐句重放虚构客服通话文本。每个启用维度对应一个 Score 和一个选择证据句的 Choice，由代码归一化、加权，并将最终评估存入 SQLite。

- 展示的是文本重放，不能视为已验证的实时语音识别。每次评估发送当前转写前缀，费用可能随对话增长；文档说明本地演示无认证。未复现评分质量或时延。

[完整中文案例](../docs/casebook.zh-CN.md#case-transcript-scorecard) · [证据说明](../docs/evidence.md)
