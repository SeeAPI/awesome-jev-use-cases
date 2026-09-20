---
id: itsmostafa-typesafe-mcp
category: automation
order: 110
title:
  en: Typesafe MCP — itsmostafa
  zh: Typesafe MCP（itsmostafa）
source_url: https://github.com/itsmostafa/typesafe-mcp
legacy_anchors:
  en:
  - 11-typesafe-mcp--itsmostafa
  - 7-typesafe-mcp--itsmostafa
  zh:
  - 11-typesafe-mcpitsmostafa
  - 7-typesafe-mcpitsmostafa
---

<!-- case:en -->

[Repository](https://github.com/itsmostafa/typesafe-mcp)

An MCP server connecting Claude Code, Claude Desktop, and Codex to Jev. Its `evaluate` tool accepts state and Noul, Choice, or Score questions for tasks such as ticket triage.

**Pattern:** ask several independent typed questions about the same state.

**Scope:** an integration tool; configurable examples should not all be counted as deployed customer use cases.

<!-- case:zh -->

- **场景**：让 Claude Code、Claude Desktop、Codex 调用 Jev 进行工单分流等判断。
- **做法**：通过 `evaluate` 接收状态与问题，支持 Noul、Choice、Score，并返回 TypeSafe 响应。
- **可借鉴点**：一次调用可以对同一状态提出多个独立问题。
- **边界**：它是接入工具，不应把可配置的示例场景全部写成已上线客户案例。
- **来源**：[项目 README](https://github.com/itsmostafa/typesafe-mcp)。

