---
id: jexp-neo4jev
category: search
order: 400
title:
  en: neo4jev
  zh: neo4jev
source_url: https://github.com/jexp/neo4jev
legacy_anchors:
  en:
  - 40-neo4jev
  - 27-neo4jev
  zh:
  - 40-neo4jev
  - 27-neo4jev
---

<!-- case:en -->

[Repository](https://github.com/jexp/neo4jev)

Navigates a Neo4j graph by presenting outgoing relationships as Choice options, asking a Noul goal-completion question, and exploring candidate paths with beam search.

**Pattern:** model-guided edge selection inside a deterministic search algorithm.

**Scope:** a demo with explicitly labeled stand-in answers when real TypeSafe calls fail. A running demo alone does not prove that every answer came from Jev.

<!-- case:zh -->

- **场景**：在 Neo4j 知识图谱中按目标逐跳选择关系。
- **做法**：将出边转换为 Choice 选项，同时用 Noul 判断是否到达目标，再用 beam search 探索候选路径。
- **可借鉴点**：模型选择候选关系，搜索算法负责路径扩展和排序。
- **边界**：演示项目；缺少有效 API 调用时存在明确标注的替代答案路径，演示运行不等于每一步都来自 Jev。
- **来源**：[项目 README](https://github.com/jexp/neo4jev)。

