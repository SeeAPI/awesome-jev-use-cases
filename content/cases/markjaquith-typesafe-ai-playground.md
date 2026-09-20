---
id: markjaquith-typesafe-ai-playground
category: experiments
order: 600
title:
  en: TypeSafe AI Playground
  zh: TypeSafe AI Playground
source_url: https://github.com/markjaquith/typesafe-ai-playground
legacy_anchors:
  en:
  - 60-typesafe-ai-playground
  - 39-typesafe-ai-playground
  zh:
  - 60-typesafe-ai-playground
  - 39-typesafe-ai-playground
---

<!-- case:en -->

[Repository](https://github.com/markjaquith/typesafe-ai-playground)

A Rust CLI exploring tasks such as protected health information detection and code-comment review through typed questions and scores.

**Pattern:** reuse decision primitives across clearly defined application criteria.

**Scope:** experimental tooling, not a privacy-compliance certification. Rubric scores and confidence probabilities should not be conflated.

<!-- case:zh -->

- **场景**：通过 Rust CLI 探索 PHI（可识别个人的健康信息）检测、代码注释审核等小型判断任务。
- **做法**：向 Jev 提交明确的分类或评分问题，展示概率或评分结果。
- **可借鉴点**：一个模型接口可以针对不同业务标准构建小工具。
- **边界**：实验工具不构成医疗隐私合规认证；评分与置信概率也不能混用。
- **来源**：[项目 README](https://github.com/markjaquith/typesafe-ai-playground)。

