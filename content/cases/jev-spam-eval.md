---
id: jev-spam-eval
category: moderation
order: 30
title:
  en: jev-spam-eval
  zh: jev-spam-eval
source_url: https://github.com/bitnovus/jev-spam-eval
legacy_anchors:
  en:
  - 3-jev-spam-eval
  zh:
  - 3-jev-spam-eval
---

<!-- case:en -->

[Repository and evaluation](https://github.com/bitnovus/jev-spam-eval)

Email classification experiments comparing natural-language Jev decision criteria with TF-IDF classifiers and combined scores, including tests across different mail sources and time periods.

**Pattern:** written classification criteria → probability → threshold or ensemble.

**Scope:** exploratory author-reported experiments. The criteria were refined after inspecting labeled errors, so “no task-specific training” should not be confused with “no supervision.” We have not reproduced the results.

<!-- case:zh -->

- **场景**：垃圾邮件及钓鱼邮件分类评估。
- **做法**：用自然语言定义分类标准，取得 Jev 概率，与 TF-IDF 分类器及组合方案比较；同时考察不同年代、来源数据的分布变化。
- **可借鉴点**：分类标准、误报和漏报、跨数据集表现，比单独展示准确率更有参考价值。
- **边界**：作者明确标注为探索性实验；分类标准在查看部分标注样本错误后调整，不能描述为完全没有人工监督。未复现实验。
- **来源**：[项目与评估说明](https://github.com/bitnovus/jev-spam-eval)。

