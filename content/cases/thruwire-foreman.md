---
id: thruwire-foreman
category: routing
order: 360
title:
  en: Foreman — semantic supervision of coding processes
  zh: Foreman — 编码代理运行时的语义监督与生命周期编排
source_url: https://github.com/thruwire/foreman
legacy_anchors:
  en:
  - 36-foreman--semantic-supervision-of-coding-processes
  zh:
  - 36-foreman--编码代理运行时的语义监督与生命周期编排
---

<!-- case:en -->

[Source](https://github.com/thruwire/foreman) · [Implementation / documentation](https://github.com/thruwire/foreman/blob/2c439828b9fe45ee5d40f6f57be81f7ff1f8a140/src/foreman/runtime.py)

An experimental runtime sends bounded task, worker-output, diff, and verification observations to nine Noul questions in one request. A deterministic policy uses those assessments to continue, start, stop, retry, verify, finish, or escalate managed work; assessments are printed for the CLI user.

**Pattern:** Bounded worker observations → semantic assessment → local policy → process lifecycle action.

**Scope:** At the linked commit, the worker interface exposes run and terminate, not a text-steering channel into a running agent. Scores are uncalibrated for this use case; incorrect judgments can stop useful work or accept bad work. Static inspection only: no Foreman, Codex, or Jev execution was performed.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/thruwire/foreman) · [实现或文档](https://github.com/thruwire/foreman/blob/2c439828b9fe45ee5d40f6f57be81f7ff1f8a140/src/foreman/runtime.py)

实验运行时将有界的任务、Worker 输出、差异与验证状态交给一次请求中的九个 Noul 问题。确定性策略据此继续、启动、停止、重试、验证、结束或升级受管工作，并向 CLI 用户打印评估。

**实现模式：** 有界 Worker 观测 → 语义评估 → 本地策略 → 进程生命周期动作。

**边界：** 所链接版本的 Worker 接口只有 run 与 terminate，没有向运行中的 Agent 回传文字 steering 的通道。分数尚未针对该用途校准，误判可能误停或误放；本轮仅静态核查，未运行 Foreman、Codex 或 Jev。

**核查日期：** 2026-09-18。

