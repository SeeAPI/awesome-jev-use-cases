---
id: devanshbatham-commit-miner
category: routing
order: 350
title:
  en: commit-miner — commit classification and security-fix signals
  zh: commit-miner — Git 提交差异分类与安全修复线索
source_url: https://github.com/devanshbatham/commit-miner
legacy_anchors:
  en:
  - 35-commit-miner--commit-classification-and-security-fix-signals
  zh:
  - 35-commit-miner--git-提交差异分类与安全修复线索
---

<!-- case:en -->

[Source](https://github.com/devanshbatham/commit-miner) · [Implementation / documentation](https://github.com/devanshbatham/commit-miner/blob/977617ebce07c56b965253a68577b1d92b93fdf1/src/miner.rs)

A Rust CLI asks Noul questions about Git changes to identify bug-fix, security-fix, change-type, and CWE signals. Large inputs are reviewed in sections before selected evidence is used for a final judgment; local thresholds assign labels.

**Pattern:** Commit diff → section judgments → selected evidence review → thresholded labels.

**Scope:** Labels are model signals, not confirmed vulnerabilities. File policies exclude some content, and final reviews of long diffs use selected evidence rather than all changes. Source diffs and metadata are sent to TypeSafe; incomplete scans retain completed results. No scans were executed here.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/devanshbatham/commit-miner) · [实现或文档](https://github.com/devanshbatham/commit-miner/blob/977617ebce07c56b965253a68577b1d92b93fdf1/src/miner.rs)

Rust CLI 通过 Noul 判断 Git 变更中的缺陷修复、安全修复、变更类型和 CWE 线索；长输入先分段审阅，再选择证据完成最终判断，由本地阈值贴标签。

**实现模式：** 提交差异 → 分段判断 → 选中证据复核 → 阈值标签。

**边界：** 标签是模型信号，不是漏洞证明。文件策略排除部分内容，长差异的最终审阅使用选中证据而非全量变更；差异与元数据会发往 TypeSafe。未完成扫描保留已完成结果，本轮未执行扫描。

**核查日期：** 2026-09-18。

