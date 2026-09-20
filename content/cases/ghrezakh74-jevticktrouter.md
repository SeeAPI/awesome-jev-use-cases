---
id: ghrezakh74-jevticktrouter
category: productivity
order: 540
title:
  en: JevTicketRouter — bilingual support triage
  zh: JevTicketRouter — 带确定性兜底的双语工单分流
source_url: https://github.com/GhrezaKh74/JevTicktRouter
legacy_anchors:
  en:
  - 54-jevticketrouter--bilingual-support-triage
  zh:
  - 54-jevticketrouter--带确定性兜底的双语工单分流
---

<!-- case:en -->

[Source](https://github.com/GhrezaKh74/JevTicktRouter) · [Implementation / documentation](https://github.com/GhrezaKh74/JevTicktRouter/blob/ee078fcddd85d339b182fb5ba3cce5ae1021d447/backend/JevTicketRouter.Application/Jev/JevTriageQuestions.cs)

A .NET and React application classifies Persian or English support tickets. One request asks Choice questions for category and team, a Score for priority, and Noul questions for sensitive data and human review; local rules handle escalation and redaction.

**Pattern:** Ticket → five typed judgments → local review and redaction rules.

**Scope:** The no-key demo can use deterministic mock answers. Low confidence forces human review rather than correcting category, team, or priority. Routing accuracy and redaction coverage were not tested.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/GhrezaKh74/JevTicktRouter) · [实现或文档](https://github.com/GhrezaKh74/JevTicktRouter/blob/ee078fcddd85d339b182fb5ba3cce5ae1021d447/backend/JevTicketRouter.Application/Jev/JevTriageQuestions.cs)

.NET 与 React 应用对波斯语或英语工单进行分流：一次请求询问类别、团队、优先级、敏感信息和人工复核需求，再由本地规则处理升级与脱敏。

**实现模式：** 工单 → 五项结构化判断 → 本地复核与脱敏规则。

**边界：** 无密钥演示可使用确定性 Mock。低置信度触发人工复核，不会自动纠正类别、团队或优先级；未实测路由准确率与脱敏覆盖。

**核查日期：** 2026-09-18。

