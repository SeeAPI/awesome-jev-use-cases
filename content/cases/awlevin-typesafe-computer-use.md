---
id: awlevin-typesafe-computer-use
category: automation
order: 130
title:
  en: typesafe-computer-use
  zh: typesafe-computer-use
source_url: https://github.com/awlevin/typesafe-computer-use
legacy_anchors:
  en:
  - 13-typesafe-computer-use
  - 9-typesafe-computer-use
  zh:
  - 13-typesafe-computer-use
  - 9-typesafe-computer-use
---

<!-- case:en -->

[Project](https://github.com/awlevin/typesafe-computer-use) · [Discovery post](https://x.com/studio_yebisu/status/2100686990090047569)

A Mac automation loop converts screen information through OCR and deterministic processing, asks Jev to choose an action, and uses a writing model only when free text is needed.

**Pattern:** Screen interpretation → bounded action selection → desktop execution.

**Scope:** OCR and local processing provide perception; Jev does not directly inspect screenshots. Author timing comparisons include task-specific preprocessing and have not been reproduced here.

<!-- case:zh -->

- **场景与做法**：Mac 自动化工具先用 OCR 与确定性处理读取屏幕，再由 Jev 选择动作，需要自由文字时才调用写作模型。
- **可借鉴点**：屏幕信息解析 → 有限动作选择 → 桌面执行。
- **边界**：感知由 OCR 和本地代码完成，不是 Jev 直接看截图；作者的性能比较涉及特定预处理，本次未复现。
- **来源**：[项目](https://github.com/awlevin/typesafe-computer-use) · [发现来源帖子](https://x.com/studio_yebisu/status/2100686990090047569)。

