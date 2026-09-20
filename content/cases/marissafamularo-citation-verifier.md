---
id: marissafamularo-citation-verifier
category: productivity
order: 560
title:
  en: Paper Trellis Citation Verifier — citation support review
  zh: Paper Trellis Citation Verifier — 论文引文支持度复核
source_url: https://github.com/MarissaFamularo/citation-verifier
legacy_anchors:
  en:
  - 56-paper-trellis-citation-verifier--citation-support-review
  zh:
  - 56-paper-trellis-citation-verifier--论文引文支持度复核
---

<!-- case:en -->

[Source](https://github.com/MarissaFamularo/citation-verifier) · [Implementation / documentation](https://github.com/MarissaFamularo/citation-verifier/blob/f9058642274033e62855d3066988418fefa2e272/src/lib/typesafe.js)

A manuscript-review tool pairs citing sentences with source passages. Claude can locate quotations, code checks quotation presence, and Jev chooses supports, contradicts, or says_nothing for the sentence and selected passage; the reviewer retains the final decision.

**Pattern:** Citation matching → passage selection → three-way support judgment → human review.

**Scope:** Jev reads a bounded passage around a quotation, or the source opening, rather than the entire paper. Passage-selection errors and abstract-only access limit the evidence. The author says thresholds lack biomedical validation; no manuscripts or model calls were tested here.

**Reviewed:** 2026-09-18.

<!-- case:zh -->

[原始来源](https://github.com/MarissaFamularo/citation-verifier) · [实现或文档](https://github.com/MarissaFamularo/citation-verifier/blob/f9058642274033e62855d3066988418fefa2e272/src/lib/typesafe.js)

稿件复核工具将引文句与源论文段落配对。Claude 可定位引用片段，代码核对引文是否存在，Jev 判断该段落支持、反驳还是未涉及该主张，最终由人工裁决。

**实现模式：** 引文匹配 → 片段选择 → 三类支持度判断 → 人工复核。

**边界：** Jev 读取引用附近的有限窗口或源文开头，并非整篇论文；片段选错或只能取得摘要会限制证据。作者说明阈值未经过生物医学标注集验证；本轮未提交稿件或调用模型。

**核查日期：** 2026-09-18。

