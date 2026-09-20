---
id: hqman-jevscout
category: productivity
order: 590
title:
  en: JevScout — career-page navigation and job matching
  zh: JevScout — 招聘页面导航与岗位匹配
source_url: https://github.com/hqman/JevScout
legacy_anchors:
  en:
  - 59-jevscout--career-page-navigation-and-job-matching
  zh:
  - 59-jevscout--招聘页面导航与岗位匹配
---

<!-- case:en -->

[Project](https://github.com/hqman/JevScout) · [Discovery source](https://x.com/0xLogicrw/status/2100861912590205411)

A coding-agent skill starts from a company website, uses Chrome through CDP to observe and navigate pages, and asks Jev to judge links and rank jobs against a job-seeker profile.

**Pattern:** Company website → career-link judgments → job discovery → profile-based ranking.

**Scope:** A demo MVP with mock and fixture-based workflows. Those demonstrations must not be presented as real Jev results. This is job-seeker assistance, distinct from employer-side CV screening; matching quality and end-to-end reliability were not tested.

**Reviewed:** 2026-09-19 (author documentation; no execution).

<!-- case:zh -->

[项目](https://github.com/hqman/JevScout) · [发现来源](https://x.com/0xLogicrw/status/2100861912590205411)

面向编程 Agent 的技能从公司官网出发，通过 CDP 观察并操作 Chrome，让 Jev 判断链接、寻找招聘入口，并按求职者资料对岗位排序。

**实现模式：** 公司官网 → 招聘链接判断 → 岗位发现 → 按求职资料排序。

**边界：** 目前为演示型 MVP，包含 mock 和固定样例流程，不能把这些演示当作真实 Jev 结果。用途是协助求职者寻找岗位，与雇主侧简历筛选不同；本次未测试匹配效果或端到端可靠性。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

