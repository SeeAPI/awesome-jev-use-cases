---
id: valentynkit-jev-commit
category: routing
order: 380
title:
  en: jev-commit — commit-message and diff checks
  zh: jev-commit — 提交信息与差异核查
source_url: https://github.com/valentynkit/jev-commit
legacy_anchors:
  en:
  - 38-jev-commit--commit-message-and-diff-checks
  zh:
  - 38-jev-commit--提交信息与差异核查
---

<!-- case:en -->

[Repository](https://github.com/valentynkit/jev-commit)

A commit-msg hook, installable through the pre-commit framework, sends the staged diff and commit message to Jev for judgments about message quality, consistency, debug leftovers, unmentioned work, and credential-like content. Code applies thresholds and a separate credential check.

**Pattern:** Staged diff and message → typed judgments and credential checks → local warning or blocking policy.

**Scope:** By default, non-secret findings warn while likely credentials can block; strict mode also blocks other findings. Large diffs may require multiple requests. Staged source and messages are submitted to the configured API endpoint; this is not a complete secret-detection boundary. Detection accuracy was not independently validated.

**Reviewed:** 2026-09-19 (author documentation; no execution).

<!-- case:zh -->

[项目来源](https://github.com/valentynkit/jev-commit)

通过 pre-commit 框架安装的 commit-msg 钩子，将暂存区差异和提交信息发送给 Jev，判断信息质量、描述一致性、调试残留、未提及的改动及疑似凭证内容；代码结合阈值与独立凭证检查作出处理。

**实现模式：** 暂存差异与提交信息 → 结构化判断及凭证检查 → 本地警告或阻断策略。

**边界：** 默认对非密钥问题仅警告，疑似凭证可阻止提交；strict 模式也会阻断其他发现。大差异可能分多次请求；暂存源码和提交信息会发送到配置的 API 端点。该工具不是完整的密钥泄漏防线，本次未独立验证检测准确率。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

