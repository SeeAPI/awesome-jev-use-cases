# Transcript Scorecard — incremental call evaluation

[English](transcript-scorecard.md) · [Chinese](transcript-scorecard.zh-CN.md)

[Read the full case](../docs/casebook.md#case-transcript-scorecard)

Metadata reference; the Casebook is the main reading entry.

A proof of concept replays fictional support-call transcripts incrementally. Each enabled criterion contributes a Score and a Choice selecting an evidence sentence; code normalizes and weights the results, then stores the final evaluation in SQLite.

**Evidence:** `docs-reviewed` · **Reviewed:** 2026-09-18 · **Live-tested by SeeAPI:** no

**Primitive:** choice, score · **Action:** score, review

[Original source](https://github.com/brandonbryant12/transcript-scorecard) · [Data record](../data/cases/transcript-scorecard.json)

## Limits

- This is transcript replay, not verified live audio recognition. Evaluations send the current transcript prefix to TypeSafe; costs can grow with the conversation. The documented local demo has no authentication. Scoring quality and timing were not reproduced.

[Evidence definitions](../docs/evidence.md)

<a id="中文"></a>[Read this page in Chinese](transcript-scorecard.zh-CN.md)
