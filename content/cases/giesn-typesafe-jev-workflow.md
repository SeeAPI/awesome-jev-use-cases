---
id: giesn-typesafe-jev-workflow
category: automation
order: 220
title:
  en: typesafe-jev-workflow — LangGraph email routing
  zh: typesafe-jev-workflow — LangGraph 邮件意图分流
source_url: https://github.com/GiesN/typesafe-jev-workflow
legacy_anchors:
  en:
  - 22-typesafe-jev-workflow--langgraph-email-routing
  zh:
  - 22-typesafe-jev-workflow--langgraph-邮件意图分流
---

<!-- case:en -->

[Source](https://github.com/GiesN/typesafe-jev-workflow) · [Implementation / documentation](https://github.com/GiesN/typesafe-jev-workflow/blob/251019670ebc3bf95870e924740d5876c1cd56b5/src/typesafe_ai_langgraph/typesafe_ai_langgraph_workflow.py)

An asynchronous LangGraph example sends email sender, subject, and body to a Choice question for invoice or general intent. Handlers set accounts_payable or general_inbox in graph state.

**Pattern:** Mock email → Jev intent classification → graph branch and destination label.

**Scope:** Handlers do not send email or make payments. Ten labeled mock emails are a smoke check, not an accuracy benchmark. The graph records confidence but has no low-confidence routing threshold; this collection did not execute it.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/GiesN/typesafe-jev-workflow) · [实现或文档](https://github.com/GiesN/typesafe-jev-workflow/blob/251019670ebc3bf95870e924740d5876c1cd56b5/src/typesafe_ai_langgraph/typesafe_ai_langgraph_workflow.py)

异步 LangGraph 示例将邮件发件人、主题与正文交给 Choice，区分 invoice 和 general，再由处理节点设置 accounts_payable 或 general_inbox。

**实现模式：** 模拟邮件 → Jev 意图分类 → 图分支与目标队列标签。

**边界：** 处理节点不发送邮件或付款。十封有标签的模拟邮件只用于冒烟检查；图记录置信度但没有低置信度分流阈值。本仓库未执行示例。

**核查日期：** 2026-09-18。

