---
id: sufianetaouil-every
category: search
order: 420
title:
  en: Every — function-level semantic search
  zh: Every — 逐函数语义代码检索
source_url: https://github.com/sufianetaouil/every
legacy_anchors:
  en:
  - 42-every--function-level-semantic-search
  - 29-every--function-level-semantic-search
  zh:
  - 42-every--逐函数语义代码检索
  - 29-every--逐函数语义代码检索
---

<!-- case:en -->

[Project](https://github.com/sufianetaouil/every)

Parses source into functions and asks Jev a yes/no question for each, returning ranked matches with cached scores.

**Scope:** Function-local judgments do not establish whole-program dataflow; scanned source is sent to TypeSafe.

<!-- case:zh -->

[项目来源](https://github.com/sufianetaouil/every)

把源码拆成函数，对每个函数提出是非问题，返回按概率排序的匹配结果并缓存评分。

**边界:** 逐函数判断不等于全程序数据流分析；扫描的源码会发送给 TypeSafe。

