---
id: jkudish-jev-mcp
category: moderation
order: 40
title:
  en: Jev MCP — jkudish
  zh: Jev MCP（jkudish）
source_url: https://github.com/jkudish/jev-mcp
legacy_anchors:
  en:
  - 4-jev-mcp--jkudish
  zh:
  - 4-jev-mcpjkudish
---

<!-- case:en -->

[Repository](https://github.com/jkudish/jev-mcp)

Exposes `jev_verify`, `jev_screen`, and `jev_find` to agents for evidence-based claim checking, input screening, and semantic candidate ranking.

**Pattern:** package narrow judgments as reusable agent tools.

**Scope:** verification depends on the supplied evidence; individual successful examples do not establish general accuracy.

<!-- case:zh -->

- **场景**：Agent 读取外部资料时核验事实、筛查输入、排列候选项。
- **做法**：提供 `jev_verify`、`jev_screen`、`jev_find` 三类 MCP 工具，返回结构化判断及概率信息。
- **可借鉴点**：把重复的小判断封装成其他 Agent 可复用的工具。
- **边界**：事实核验依赖传入证据；作者给出的个别成功案例不能证明整体准确率。
- **来源**：[项目 README](https://github.com/jkudish/jev-mcp)。

