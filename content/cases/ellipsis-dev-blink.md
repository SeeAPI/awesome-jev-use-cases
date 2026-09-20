---
id: ellipsis-dev-blink
category: search
order: 390
title:
  en: Blink
  zh: Blink
source_url: https://github.com/ellipsis-dev/blink
legacy_anchors:
  en:
  - 39-blink
  - 26-blink
  zh:
  - 39-blink
  - 26-blink
---

<!-- case:en -->

[Repository](https://github.com/ellipsis-dev/blink)

Finds files from natural-language queries by having Jev score file and folder names, allocating walkers along likely paths.

**Pattern:** narrow a search space through repeated semantic choices.

**Scope:** result percentages represent the share of walkers reaching a file, not file correctness probabilities. This is not a full source-code semantic index.

<!-- case:zh -->

- **场景**：根据自然语言问题在代码目录中查找相关文件。
- **做法**：Jev 对文件和目录名称进行判断，多个 walker 按路径倾向继续探索。
- **可借鉴点**：将语义判断用于逐层缩小搜索空间。
- **边界**：结果百分比是到达该文件的 walker 占比，不能直接当成文件正确率；这也不是完整源码语义索引。
- **来源**：[项目 README](https://github.com/ellipsis-dev/blink)。

