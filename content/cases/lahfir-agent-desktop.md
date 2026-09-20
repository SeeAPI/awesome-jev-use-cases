---
id: lahfir-agent-desktop
category: automation
order: 100
title:
  en: Jev desktop control in agent-desktop
  zh: agent-desktop 中的 Jev 桌面控制
source_url: https://github.com/lahfir/agent-desktop
legacy_anchors:
  en:
  - 10-jev-desktop-control-in-agent-desktop
  - 6-jev-desktop-control-in-agent-desktop
  zh:
  - 10-agent-desktop-中的-jev-桌面控制
  - 6-agent-desktop-中的-jev-桌面控制
---

<!-- case:en -->

[Repository](https://github.com/lahfir/agent-desktop) · [Jev loop](https://github.com/lahfir/agent-desktop/blob/main/scripts/jev/run.mjs)

A Jev integration reads an operating-system accessibility tree, selects an operation and target, and hands the result to a local desktop executor.

**Pattern:** separate interface observation, model decisions, and execution.

**Scope:** agent-desktop is a broader desktop tool with a specific Jev integration, not an exclusively Jev-based project.

**Demo material**: [Original desktop demonstration](https://github.com/user-attachments/assets/9b2c9f8c-a49d-4b69-b6cf-11d9e0d40ceb)

<!-- case:zh -->

- **场景**：通过桌面应用的 Accessibility Tree 选择控件和动作。
- **做法**：观察当前界面结构，将操作及目标作为受限选项交给 Jev，再由本地执行器执行并重新观察。
- **可借鉴点**：界面状态、模型决策、本地执行各自承担明确职责。
- **边界**：`agent-desktop` 是通用桌面工具，Jev 是其中的具体集成；不能把整个仓库都称为 Jev 专属项目。
- **来源**：[项目](https://github.com/lahfir/agent-desktop)、[Jev 运行循环](https://github.com/lahfir/agent-desktop/blob/main/scripts/jev/run.mjs)。

**演示素材**: [原作者桌面操作演示](https://github.com/user-attachments/assets/9b2c9f8c-a49d-4b69-b6cf-11d9e0d40ceb)

