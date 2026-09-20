---
id: valentynkit-jev-nvim
category: search
order: 440
title:
  en: jev.nvim — semantic function search in Neovim
  zh: jev.nvim — Neovim 函数级语义检索
source_url: https://github.com/valentynkit/jev.nvim
legacy_anchors:
  en:
  - 44-jevnvim--semantic-function-search-in-neovim
  zh:
  - 44-jevnvim--neovim-函数级语义检索
---

<!-- case:en -->

[Repository](https://github.com/valentynkit/jev.nvim)

A Neovim plugin uses Treesitter to split buffer code into functions and asks Jev whether each function matches a natural-language question. Results appear as probabilities in virtual text and a ranked quickfix list, integrating semantic search into the editor.

**Pattern:** Buffer or selected files → function extraction → per-function judgments → ranked editor results.

**Scope:** Functions are judged separately, without cross-function context; matches are search leads rather than confirmed defects. Source snippets are sent to the configured API endpoint. The published demo uses fixture probabilities, not measured model results. Ranking quality was not independently evaluated.

**Reviewed:** 2026-09-19 (author documentation; no execution).

<!-- case:zh -->

[项目来源](https://github.com/valentynkit/jev.nvim)

Neovim 插件通过 Treesitter 将缓冲区代码拆成函数，让 Jev 判断各函数是否符合自然语言问题，并将概率显示为虚拟文本、将匹配项排序放入 quickfix 列表，把语义搜索接入编辑器操作流程。

**实现模式：** 缓冲区或选定文件 → 函数提取 → 逐函数判断 → 编辑器内排序结果。

**边界：** 各函数独立判断，不包含跨函数上下文；匹配项是检索线索，不是已确认缺陷。源码片段会发送到配置的 API 端点。公开演示的概率来自固定样例，并非模型实测；本次未独立评估排序效果。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

