# Awesome Jev Use Cases — Jev 应用场景与案例

[![English](https://img.shields.io/badge/Language-English-blue)](README.md) [![简体中文](https://img.shields.io/badge/语言-简体中文-lightgrey)](README_zh.md)
[![Docs: CC BY 4.0](https://img.shields.io/badge/Docs-CC_BY_4.0-blue)](LICENSE) [![Code: MIT](https://img.shields.io/badge/Code-MIT-green)](LICENSE-CODE)

探索 **[Jev](https://typesafe.ai/)** 在内容审核、自动化、模型路由和语义搜索中的真实用法，了解每个项目中 Jev 负责哪一步判断、如何接入软件流程，以及值得借鉴的实现方式。

![Awesome Jev Use Cases — 真实项目与结构化判断，由 SeeAPI 整理的独立社区案例集。](assets/banner.png)

**83 个项目 · 最近更新：2026-09-19**

**[浏览案例](#按场景浏览) · [了解 Jev](#jev-是什么) · [接入指南](#模型来源与接入方式) · [提交案例](CONTRIBUTING.md)**

Jev 是 TypeSafe AI 面向结构化判断推出的 System One 模型，返回选择、评分或概率，由应用代码据此决定下一步动作。

由 [SeeAPI](https://github.com/SeeAPI) 整理的独立社区案例集，非 TypeSafe 官方项目。详见[核查范围与来源](#发现来源与更新方式)。

## 按场景浏览

| 分类 | 项目数 | 可以找到什么 |
| --- | ---: | --- |
| [内容审核与安全](#内容审核与安全) | 8 | 内容筛查、风险判断与审核处置 |
| [自动化与开发工具接入](#自动化与开发工具接入) | 16 | 桌面、浏览器、移动端及工作流集成 |
| [模型成本与代码工作流](#模型成本与代码工作流) | 14 | 模型选择、代码审查与 Agent 任务分配 |
| [语义搜索与知识导航](#语义搜索与知识导航) | 6 | 图谱导航、语义搜索与结果重排序 |
| [数据分类与办公效率](#数据分类与办公效率) | 15 | 表格、文档分析与工单分类 |
| [实验与垂直场景](#实验与垂直场景) | 15 | 游戏、控制系统及垂直领域应用 |
| [评测与行为研究](#评测与行为研究) | 9 | 作者报告的评测与模型行为研究 |

## 内容审核与安全

### 1. Safer with Jev（原 TypeSafe on Neon）

- **场景**：在内容转发或上传前检查提示词注入、图片风险及模型回复风险。
- **做法**：HTTP 网关接收内容，输出放行、复核或拦截结果；通过后可转发到指定上游。
- **图片链路**：当前实现用 `gemini-3-flash` 生成结构化图片描述，再由 Jev 对描述中的性内容、血腥暴力等风险进行判断。Jev 在这里承担描述审核与决策环节。
- **可借鉴点**：将检测结果连接到上传拦截、人工复核与下游调用流程。
- **边界**：不是 Jev 原生视觉 NSFW 检测的证据，也没有在本次核查中验证识别效果。原帖的“模型 Router”介绍已不符合当前 README。
- **来源**：[项目](https://github.com/andrelandgraf/typesafe-on-neon)、[视觉描述实现](https://github.com/andrelandgraf/typesafe-on-neon/blob/main/src/lib/vision.ts)、[Jev 判断实现](https://github.com/andrelandgraf/typesafe-on-neon/blob/main/src/lib/judge.ts)。

### 2. Jev Moderation Bot

- **场景**：Discord 社区中的钓鱼、垃圾信息及社交工程消息审核。
- **做法**：结合消息正文、账号与频道等上下文判断风险，由程序执行分级处置；管理员纠正的误报作为后续判断的上下文。
- **可借鉴点**：检测、处置、申诉、反馈样本形成完整流程。
- **边界**：这里核实的是文字消息审核方案，不是图片或视频 NSFW 模型；未独立测量误报率。
- **来源**：[项目 README](https://github.com/brainstormity/Jev-Moderation-Bot)。

### 3. jev-spam-eval

- **场景**：垃圾邮件及钓鱼邮件分类评估。
- **做法**：用自然语言定义分类标准，取得 Jev 概率，与 TF-IDF 分类器及组合方案比较；同时考察不同年代、来源数据的分布变化。
- **可借鉴点**：分类标准、误报和漏报、跨数据集表现，比单独展示准确率更有参考价值。
- **边界**：作者明确标注为探索性实验；分类标准在查看部分标注样本错误后调整，不能描述为完全没有人工监督。未复现实验。
- **来源**：[项目与评估说明](https://github.com/bitnovus/jev-spam-eval)。

### 4. Jev MCP（jkudish）

- **场景**：Agent 读取外部资料时核验事实、筛查输入、排列候选项。
- **做法**：提供 `jev_verify`、`jev_screen`、`jev_find` 三类 MCP 工具，返回结构化判断及概率信息。
- **可借鉴点**：把重复的小判断封装成其他 Agent 可复用的工具。
- **边界**：事实核验依赖传入证据；作者给出的个别成功案例不能证明整体准确率。
- **来源**：[项目 README](https://github.com/jkudish/jev-mcp)。

### 5. Capbroker — 权限边界之外的Jev风险提示

[原始来源](https://github.com/suryanshu-singh/capbroker) · [实现或文档](https://github.com/suryanshu-singh/capbroker/blob/f7532aa83e376ad9fbc0bfbb92ada2a2a53c1999/README.md#jev-powered-defense-in-depth-advisory-only--read-this-carefully)

能力权限代理可选用 Jev 标注可疑 MCP 工具输出，并在人工审批提示中展示风险建议。确定性权限校验与人工审批独立于模型建议。

**实现模式：** 能力权限校验 → 可选内容警告或风险建议 → 必要时人工裁决。

**边界：** Jev 只提供建议，不决定代理的权限放行。作者攻击演示使用假上游及测试凭据；没有警告不代表安全，权限范围内的动作仍可能被滥用。本轮未执行。

**核查日期：** 2026-09-18。

### 6. Openroom — 可改规则的实时聊天审核

[原始来源](https://openroom-ivory.vercel.app) · [实现或文档](https://x.com/stoufax/status/2100899469843673218)

作者介绍的聊天应用使用 Jev、Convex 与 Vercel，在消息展示前审核；自然语言房间规则修改后可重新判断，不确定消息转交人工。

**实现模式：** 消息与房间规则 → 审核判断 → 展示或人工复核队列。

**边界：** 依据作者公开说明收录，未验证后端实现；本轮未发送消息或保存规则，阈值与审核准确率未经验证。

**核查日期：** 2026-09-18。

### 7. JEVScan — Etherscan地址与交易风险提示

[原始来源](https://x.com/theRaz0r/status/2100898307186864593)

作者展示的 Chrome 扩展称使用 Jev 为 Etherscan 地址与交易提示潜在风险；本仓库将其作为作者演示的风险提示界面收录。

**实现模式：** 区块链浏览器上下文 → 风险判断 → 页面内提示供人工检查。

**边界：** 原帖支持作者的集成声明，不证明准确率。未核实公开实现、输入特征、阈值或请求记录；风险标签不是欺诈事实证明，本轮未运行扩展或调用模型。

**核查日期：** 2026-09-18。

### 8. BlueNoise — X 评论区噪声过滤

[项目](https://github.com/rokcso/bluenoise) · [发现来源](https://github.com/logicrw/awesome-jev-projects/issues/3)

浏览器扩展先使用本地关键词和账号规则，再通过可选的 Jev 功能，对未匹配规则的 X 回复进行噪声判断，由代码据此过滤回复。

**实现模式：** 本地规则 → 剩余回复文本及上下文 → 噪声概率 → 展示策略。

**边界：** Jev 功能仍属实验选项，默认关闭；启用后会将回复文本发送给 TypeSafe，因此默认模式的纯本地处理说明不适用于该模式。本次未独立测试过滤效果。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

**演示素材：** [作者截图与功能介绍](https://x.com/rokcso/status/2100876608340910548)。原作者素材，仅提供外链，不代表 SeeAPI 实测。

## 自动化与开发工具接入

<a id="5-jev-ultrafast"></a>

### 9. Jev Ultrafast

- **场景**：浏览器中逐步完成查询、点击与表单输入。
- **做法**：将可见页面控件整理成带索引的候选集合，Jev 选择操作与目标；需要输入文字时再调用文字生成模型。
- **可借鉴点**：把“选择动作”和“生成文字”拆开，缩小每次决策范围。
- **边界**：作者报告的约 7.1 秒航班搜索是特定任务演示，计时从首次页面观察之后开始，不是任意网页任务的速度保证。
- **来源**：[项目与测量边界](https://github.com/browser-use/jev-ultrafast)。

**演示素材**: [原作者航班搜索演示](https://github.com/browser-use/jev-ultrafast/blob/main/docs/demo.mp4)

<img src="assets/cases/browser-use__jev-ultrafast.png" alt="航班搜索结果" width="720" />

原作者素材：航班搜索结果；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/docs/flights-result.png) · [许可与署名](THIRD_PARTY_NOTICES.md)

<a id="6-agent-desktop-中的-jev-桌面控制"></a>

### 10. agent-desktop 中的 Jev 桌面控制

- **场景**：通过桌面应用的 Accessibility Tree 选择控件和动作。
- **做法**：观察当前界面结构，将操作及目标作为受限选项交给 Jev，再由本地执行器执行并重新观察。
- **可借鉴点**：界面状态、模型决策、本地执行各自承担明确职责。
- **边界**：`agent-desktop` 是通用桌面工具，Jev 是其中的具体集成；不能把整个仓库都称为 Jev 专属项目。
- **来源**：[项目](https://github.com/lahfir/agent-desktop)、[Jev 运行循环](https://github.com/lahfir/agent-desktop/blob/main/scripts/jev/run.mjs)。

**演示素材**: [原作者桌面操作演示](https://github.com/user-attachments/assets/9b2c9f8c-a49d-4b69-b6cf-11d9e0d40ceb)

<a id="7-typesafe-mcpitsmostafa"></a>

### 11. Typesafe MCP（itsmostafa）

- **场景**：让 Claude Code、Claude Desktop、Codex 调用 Jev 进行工单分流等判断。
- **做法**：通过 `evaluate` 接收状态与问题，支持 Noul、Choice、Score，并返回 TypeSafe 响应。
- **可借鉴点**：一次调用可以对同一状态提出多个独立问题。
- **边界**：它是接入工具，不应把可配置的示例场景全部写成已上线客户案例。
- **来源**：[项目 README](https://github.com/itsmostafa/typesafe-mcp)。

<a id="8-semdecide"></a>

### 12. SemDecide

- **场景**：在命令行、CI 或数据流水线中做语义判断、路由、评分与过滤。
- **做法**：提供 `is`、`choose`、`score`、`filter` 和 `guard` 命令，将不确定性、阈值与进程退出码纳入接口。
- **可借鉴点**：既输出判断结果，也明确表示“不确定”和“调用失败”。
- **边界**：模型判断不是权限系统；自动执行仍由调用方流程决定。
- **来源**：[项目 README](https://github.com/sharziki/semdecide)。

<a id="9-typesafe-computer-use"></a>

### 13. typesafe-computer-use

- **场景与做法**：Mac 自动化工具先用 OCR 与确定性处理读取屏幕，再由 Jev 选择动作，需要自由文字时才调用写作模型。
- **可借鉴点**：屏幕信息解析 → 有限动作选择 → 桌面执行。
- **边界**：感知由 OCR 和本地代码完成，不是 Jev 直接看截图；作者的性能比较涉及特定预处理，本次未复现。
- **来源**：[项目](https://github.com/awlevin/typesafe-computer-use) · [发现来源帖子](https://x.com/studio_yebisu/status/2100686990090047569)。

<a id="10-jev-browser"></a>

### 14. Jev Browser

- **场景与做法**：通过已有浏览器工具持续观察、操作和验证；规划 Agent 提供目标与导航方向，Jev 选择实际观察到的页面元素。
- **可借鉴点**：一次规划，循环执行有限范围内的浏览器判断。
- **边界**：非官方集成，需要兼容的浏览器工具；与 browser-use/jev-ultrafast 是不同项目，并非独立浏览器服务。
- **来源**：[项目](https://github.com/vlad-terin/jev-browser) · [发现来源帖子](https://x.com/studio_yebisu/status/2100686990090047569)。

**演示素材**: [原作者浏览器演示](https://github.com/user-attachments/assets/2e456743-96d5-4ad9-8ca3-97f7b6ed11f2)

<a id="11-mobile-jev"></a>

### 15. Mobile Jev

- **场景与做法**：通过 Mobilerun 在真实 Android 设备上运行，由 Jev 选择操作，提供可视化工作台、CLI 和执行轨迹。
- **可借鉴点**：目标 → 手机状态 → 动作选择 → 设备执行。
- **边界**：README 中的 Uber 演示到达支付方式选择，未展示完成叫车；约 21 秒、9 个动作是单次演示数据。
- **来源**：[项目](https://github.com/droidrun/mobile-jev) · [发现来源帖子](https://x.com/studio_yebisu/status/2100686990090047569)。

**演示素材**: [Android 演示：Uber 路线输入至支付方式选择](https://github.com/droidrun/mobile-jev/blob/main/docs/media/uber-demo.mp4)

<img src="assets/cases/droidrun__mobile-jev.jpg" alt="Android Uber 演示" width="720" />

原作者素材：Android Uber 演示；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/docs/media/uber-demo.jpg) · [许可与署名](THIRD_PARTY_NOTICES.md)

<a id="12-zod-jev--表单语义校验"></a>

### 16. zod-jev — 表单语义校验

[项目来源](https://github.com/jomatsu/zod-jev)

在 Zod 格式校验之上加入 Jev 语义判断，将概率转为校验结果，适合检查内容含义、分类与描述是否匹配。

**边界:** 需要处理不确定和服务不可用的结果；通过校验不代表事实一定正确。

<a id="13-ha-jev--家庭状态判断"></a>

### 17. HA-Jev — 家庭状态判断

[项目来源](https://github.com/AboveColin/HA-Jev)

把 Home Assistant 设备状态交给 Jev 判断，将概率、选项和评分转为传感器或自动化动作返回值。

**边界:** 效果依赖设备状态质量和自动化规则；本仓库未安装联调。

<a id="14-n8n-typesafe-节点--工作流判断"></a>

### 18. n8n TypeSafe 节点 — 工作流判断

[项目来源](https://github.com/DomMonte/n8n-nodes-typesafe-ai)

通过 n8n 社区节点调用 TypeSafe 的结构化判断，让后续工作流按结果分支处理。

**边界:** 属于社区集成；安装条件与重试处理取决于 n8n 环境和工作流配置。

<a id="15-unclutter--网页杂乱元素分类与隐藏"></a>

### 19. Unclutter — 网页杂乱元素分类与隐藏

[项目来源](https://github.com/kitze/unclutter)

浏览器扩展用 Jev 对网页元素分类，再按可复用规则隐藏选定的杂乱内容。

**边界:** 需保留不确定元素；隐藏同意弹窗不等于替用户作出同意或拒绝选择。

<a id="16-jev-mobile--android设置导航poc"></a>

### 20. jev-mobile — Android设置导航PoC

[项目来源](https://github.com/Friedjof/jev-mobile)

基于语义 UI 状态、稳定性检查及有限动作选项，构建 Android 观察、决策与执行循环。

**边界:** 作者主要验证 Android 设置导航，不是通用手机 Agent；与 droidrun/mobile-jev 是不同项目。

### 21. triage-guard — 支持、告警与部署风险的判断管线

[原始来源](https://github.com/shivam2003-dev/typesafe-triage-guard) · [实现或文档](https://github.com/shivam2003-dev/typesafe-triage-guard/blob/9dea2e2c82eb0acb8b9bac8e366ad9112fa770fd/src/triage/battery.py)

Python 研究示例在支持工单、运维告警和部署风险中复用判断引擎。批量 Noul 风险信号与严重度 Score 交给代码策略表；工单流程另加入部门及紧急度判断。

**实现模式：** 输入 → 风险问题组 → 策略阈值 → 放行、复核、阻断或支持分流。

**边界：** 作者定位为研发示例；离线关键词 Mock 用于验证组合逻辑，不能作为 Jev 效果。未验证阈值校准或真实部署结果。

**核查日期：** 2026-09-18。

### 22. typesafe-jev-workflow — LangGraph 邮件意图分流

[原始来源](https://github.com/GiesN/typesafe-jev-workflow) · [实现或文档](https://github.com/GiesN/typesafe-jev-workflow/blob/251019670ebc3bf95870e924740d5876c1cd56b5/src/typesafe_ai_langgraph/typesafe_ai_langgraph_workflow.py)

异步 LangGraph 示例将邮件发件人、主题与正文交给 Choice，区分 invoice 和 general，再由处理节点设置 accounts_payable 或 general_inbox。

**实现模式：** 模拟邮件 → Jev 意图分类 → 图分支与目标队列标签。

**边界：** 处理节点不发送邮件或付款。十封有标签的模拟邮件只用于冒烟检查；图记录置信度但没有低置信度分流阈值。本仓库未执行示例。

**核查日期：** 2026-09-18。

### 23. Pi Jev Auto Mode — 工具调用概率门控

[原始来源](https://github.com/jomatsu/pi-jev-auto-mode) · [实现或文档](https://github.com/jomatsu/pi-jev-auto-mode/blob/main/src/settings.ts)

Pi 扩展在 bash、write、edit 调用前组合确定性规则与 Jev 语义判断，由代码将条件概率与阈值比较，得到允许、拒绝或不确定的决策。

**实现模式：** 工具调用 → 确定性检查 → 语义条件判断 → 本地执行门控。

**边界：** 核查时 README 称不确定结果会被阻止，但 src/settings.ts 默认 uncertain 为 allow，src/jev/decide.ts 将 hazard 模式的不确定条件按满足处理。需核对实际版本与策略，不能默认失败关闭；本轮未运行，也不构成安全保证。

**核查日期：** 2026-09-18。

### 24. jev-skip — 基于字幕的 YouTube 赞助片段识别

[项目来源](https://github.com/valentynkit/jev-skip)

浏览器扩展读取视频字幕轨道，在片头结束前就为每个片段标出赞助概率，直接画在 YouTube 进度条上，不依赖众包时间戳数据库。

**实现模式：** 字幕轨道 → 逐片段 Jev 判断 → 进度条叠加显示，无需服务端查询。

**边界：** 作者报告在 23 个视频、每个视频 0.0008 美元成本下，识别出 SponsorBlock 赞助时长的 77%，对照的是 SponsorBlock 自己的社区时间戳，这是作者自测数据，不是独立评测。

**核查日期：** 2026-09-19。

## 模型成本与代码工作流

<a id="17-jev-codex-router"></a>

### 25. Jev Codex Router

- **场景**：按编程任务难度选择模型与推理深度。
- **做法**：每轮先由 Jev 分类，再按策略路由到不同模型，记录结果并处理低置信度或错误。
- **可借鉴点**：在质量、延迟和费用之间建立可观察的路由策略。
- **边界**：约 60% 成本下降来自作者对 237 个真实 turn 的回放自测，不是 SeeAPI 实测或普遍承诺。
- **来源**：[项目及回测入口](https://github.com/0xNatoshi/jev-codex-router)。

<a id="18-winnow"></a>

### 26. Winnow

- **场景**：压缩进入 Claude Code 上下文的长工具输出。
- **做法**：Jev 判断分块内容是否与当前任务有关；高置信度无关内容替换为摘要或占位说明，原文缓存并支持按需恢复。不确定内容保留。
- **可借鉴点**：保留召回机制的上下文筛选，而非直接删除信息。
- **边界**：筛选判断与摘要生成是不同步骤；配置其他判断适配器时不能把结果一概归为 Jev 效果。
- **来源**：[项目 README](https://github.com/GhalebDweikat/winnow)。

<a id="19-jev-review"></a>

### 27. Jev Review

- **场景**：对 Git diff 或代码库进行结构化风险审查。
- **做法**：依次判断风险、文件特征、证据位置、机制和严重性，并按条件路由后续审查。
- **可借鉴点**：用一系列小判断定位值得深入检查的代码片段。
- **边界**：作者将其定位为实验；当前不集成编译器诊断或静态分析，结果是审查线索而非缺陷证明。
- **来源**：[项目 README](https://github.com/devagrawal09/jev-review)。

<img src="assets/cases/jev-review-dashboard.png" alt="Jev Review dashboard" width="720" />

原作者素材：Dev Agrawal · MIT · 未修改 · [来源](https://github.com/devagrawal09/jev-review/blob/31f89602797fb7bea007f8a480bf368bf564954e/docs/dashboard.png) · [许可与署名](THIRD_PARTY_NOTICES.md)

<a id="20-jev-router--gargpratyush"></a>

### 28. jev-router — gargpratyush

- **场景与做法**：启动原生 Claude Code 或 Codex CLI，并在新用户轮次开始时按任务难度选择快速或强能力模型。
- **可借鉴点**：判断当前轮次的任务，再选择执行模型。
- **边界**：与 0xNatoshi 的 Jev Codex Router 是不同项目；README 描述的是按新用户轮次路由，不是每个内部工具步骤重新选择。
- **来源**：[项目](https://github.com/gargpratyush/jev-router) · [发现来源帖子](https://x.com/studio_yebisu/status/2100686990090047569)。

<img src="assets/cases/gargpratyush__jev-router.png" alt="模型选择界面" width="720" />

原作者素材：模型选择界面；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/gargpratyush/jev-router/blob/86660a0248eba0e4523f81645ac2925e9808c000/docs/model-picker.png) · [许可与署名](THIRD_PARTY_NOTICES.md)

<a id="21-eve--typed-evaluation-and-model-selection"></a>

### 29. eve — typed evaluation and model selection

- **场景与做法**：Agent 框架默认使用 Jev 做自动模型选择和结构化评估，文档还展示了工具执行审批中的判断与人工复核。
- **可借鉴点**：将结构化评估接入模型路由、工具和审批流程。
- **边界**：Jev 是评估器，不是 eve 的唯一运行模型；底层 AI SDK evaluation 规范仍为实验性。
- **来源**：[项目](https://github.com/vercel/eve) · [发现来源帖子](https://x.com/yibie/status/2100619188062523695) · [Implementation / 文档](https://github.com/vercel/eve/blob/main/docs/guides/evaluate.md)。

<a id="22-dspy-typesafeify--混合推理"></a>

### 30. DSPy typesafeify — 混合推理

[项目来源](https://github.com/typesafeainate/dspy-typesafeify)

概念验证装饰器将 DSPy 中的布尔、枚举及指定评分字段交给 Jev，自由文本仍交给生成模型。

**边界:** 作者对照仅使用三个示例，不能推导普遍的成本或速度提升。

**演示素材**: [作者三个示例对照图](https://github.com/typesafeainate/dspy-typesafeify/blob/708f1d109fc9316bdbb5674bdb10cf18b55be137/examples/typesafe_dspy_ticket_triage/benchmark.svg)

<a id="23-jevlogs--运维日志语义分流"></a>

### 31. jevlogs — 运维日志语义分流

[项目来源](https://github.com/reachjalil/jevlogs)

在高成本分析前，用 Jev 判断 OpenTelemetry 日志的诊断价值和优先级，同时保留日志归档。

**边界:** 仅标注不会跳过后续分析；是否节省开销取决于转发模式与策略。

<a id="24-swarmrouter--任务分配给专长agent"></a>

### 32. SwarmRouter — 任务分配给专长Agent

[项目来源](https://github.com/ndolinschi/swarmrouter) · [实现代码](https://github.com/ndolinschi/swarmrouter/blob/37a895b82633fc1964577c89dfee8b87f6914cc2/src/lib/product.ts)

通过结构化问题选择专长 Agent，并判断任务歧义和协作需求。

**边界:** 路由建议不等于已执行的多 Agent 工作流；无 key 演示使用本地规则。

<a id="25-jev-axi--agent判断工具与构建日志分诊"></a>

### 33. jev-axi — Agent判断工具与构建日志分诊

[项目来源](https://github.com/shiftynick/jev-axi)

为 Agent 提供防护判断、构建日志分诊、差异审查及批量过滤命令，复用固定问题方案。

**边界:** 作者 Agent 实验减少了文件读取但未降低成本；判断不能替代源码阅读或完整安全边界。

### 34. Pi Warden — 规则检查与代理行为提醒

[原始来源](https://github.com/DevMortimer/pi-warden) · [实现或文档](https://github.com/DevMortimer/pi-warden/blob/main/README.md)

Pi 扩展将修改与项目规则对照，把反馈加入 Agent 上下文；其他检查覆盖任务偏离、缺少证据的完成声明及风险动作，由确定性模式和模型判断共同触发代码策略。

**实现模式：** Agent 上下文与拟议修改 → 规则及风险检查 → 反馈或特定拦截。

**边界：** 很多问题只提醒或引导，不会阻断。作者的 150 组配对运行报告规则违规减少，但其他指标改善有限或没有改善，未独立复现；该扩展不是沙箱或完整权限边界。

**核查日期：** 2026-09-18。

### 35. commit-miner — Git 提交差异分类与安全修复线索

[原始来源](https://github.com/devanshbatham/commit-miner) · [实现或文档](https://github.com/devanshbatham/commit-miner/blob/977617ebce07c56b965253a68577b1d92b93fdf1/src/miner.rs)

Rust CLI 通过 Noul 判断 Git 变更中的缺陷修复、安全修复、变更类型和 CWE 线索；长输入先分段审阅，再选择证据完成最终判断，由本地阈值贴标签。

**实现模式：** 提交差异 → 分段判断 → 选中证据复核 → 阈值标签。

**边界：** 标签是模型信号，不是漏洞证明。文件策略排除部分内容，长差异的最终审阅使用选中证据而非全量变更；差异与元数据会发往 TypeSafe。未完成扫描保留已完成结果，本轮未执行扫描。

**核查日期：** 2026-09-18。

### 36. Foreman — 编码代理运行时的语义监督与生命周期编排

[原始来源](https://github.com/thruwire/foreman) · [实现或文档](https://github.com/thruwire/foreman/blob/2c439828b9fe45ee5d40f6f57be81f7ff1f8a140/src/foreman/runtime.py)

实验运行时将有界的任务、Worker 输出、差异与验证状态交给一次请求中的九个 Noul 问题。确定性策略据此继续、启动、停止、重试、验证、结束或升级受管工作，并向 CLI 用户打印评估。

**实现模式：** 有界 Worker 观测 → 语义评估 → 本地策略 → 进程生命周期动作。

**边界：** 所链接版本的 Worker 接口只有 run 与 terminate，没有向运行中的 Agent 回传文字 steering 的通道。分数尚未针对该用途校准，误判可能误停或误放；本轮仅静态核查，未运行 Foreman、Codex 或 Jev。

**核查日期：** 2026-09-18。

### 37. jev-belay — Claude Code 的"完成"核验 Stop 钩子

[项目来源](https://github.com/valentynkit/jev-belay)

Claude Code 的 Stop 钩子，在 Agent 的"已完成"被采信前先读取会话记录寻找证据。只有当文件在最近一次通过的检查之后发生变更时，才会花一次 Jev 调用，提出四个问题；任何出错路径都直接放行，避免 Jev 故障挡住 Agent。

**实现模式：** 会话记录证据核查 → 有条件的 Jev 判断 → 放行或阻止 Stop。

**边界：** 作者本人的钩子，阻止/放行的准确率本轮未做独立核验。

**核查日期：** 2026-09-19。

### 38. jev-commit — 提交信息与改动匹配度检查

[项目来源](https://github.com/valentynkit/jev-commit)

pre-commit 钩子把暂存区差异和提交信息一起交给一次 Jev 调用，判断提交信息是否匹配改动，并标记调试残留或未提及的改动。另有一个凭证检查与之并行运行，发现疑似密钥就直接阻止提交，其余情况只提示警告。

**实现模式：** 暂存差异与提交信息 → Jev 判断 → 提示警告，检测到密钥时硬性阻止。

**边界：** 作者本人的钩子，判断准确率本轮未做独立核验。

**核查日期：** 2026-09-19。

## 语义搜索与知识导航

<a id="26-blink"></a>

### 39. Blink

- **场景**：根据自然语言问题在代码目录中查找相关文件。
- **做法**：Jev 对文件和目录名称进行判断，多个 walker 按路径倾向继续探索。
- **可借鉴点**：将语义判断用于逐层缩小搜索空间。
- **边界**：结果百分比是到达该文件的 walker 占比，不能直接当成文件正确率；这也不是完整源码语义索引。
- **来源**：[项目 README](https://github.com/ellipsis-dev/blink)。

<a id="27-neo4jev"></a>

### 40. neo4jev

- **场景**：在 Neo4j 知识图谱中按目标逐跳选择关系。
- **做法**：将出边转换为 Choice 选项，同时用 Noul 判断是否到达目标，再用 beam search 探索候选路径。
- **可借鉴点**：模型选择候选关系，搜索算法负责路径扩展和排序。
- **边界**：演示项目；缺少有效 API 调用时存在明确标注的替代答案路径，演示运行不等于每一步都来自 Jev。
- **来源**：[项目 README](https://github.com/jexp/neo4jev)。

<a id="28-sift--搜索结果重排"></a>

### 41. Sift — 搜索结果重排

[项目来源](https://github.com/tylergibbs1/sift)

Chrome 扩展使用 Jev 判断搜索结果的相关性、推广倾向和信息深度，再由代码重排 Google 搜索结果。

**边界:** 依据搜索摘要而非网页全文；过滤策略会考虑搜索意图。

<a id="29-every--逐函数语义代码检索"></a>

### 42. Every — 逐函数语义代码检索

[项目来源](https://github.com/sufianetaouil/every)

把源码拆成函数，对每个函数提出是非问题，返回按概率排序的匹配结果并缓存评分。

**边界:** 逐函数判断不等于全程序数据流分析；扫描的源码会发送给 TypeSafe。

### 43. Jev Search — 自然语言搜索意图识别与结果重排

[原始来源](https://github.com/superagents-lab/jev-search) · [实现或文档](https://github.com/superagents-lab/jev-search/blob/369b282489f72e58298ba1abc8b0144b1bc15c59/src/lib/typesafe.ts)

TypeScript 应用先让 Jev 选择搜索源、时间范围与检索词候选，经 Search1API 获取结果后，批量判断标题及摘要相关性；代码合并 URL，按相关性、引擎一致性与原始名次排序。

**实现模式：** 搜索意图 → 外部检索 → 逐结果判断 → 合并并流式返回排名。

**边界：** 相关性分数不验证网页事实，摘要可能不完整或过时；一次搜索可能触发多次供应商调用。本轮查阅了接口与排序管线代码，未测量检索质量、时延或费用。

**核查日期：** 2026-09-18。

### 44. jev.nvim — Neovim 中按 Treesitter 函数划分的语义代码搜索

[项目来源](https://github.com/valentynkit/jev.nvim)

Neovim 插件接收对当前缓冲区的一句自然语言提问，用 Treesitter 把代码拆成函数，让 Jev 为每个函数打相关性分。匹配结果按概率排序进入 quickfix 列表。

**实现模式：** 缓冲区 → Treesitter 函数拆分 → 逐函数 Jev 打分 → quickfix 排序结果。

**边界：** 作者本人的插件，排序质量本轮未做独立核验。

**核查日期：** 2026-09-19。

## 数据分类与办公效率

<a id="30-judge-sheets--predictive-spreadsheets"></a>

### 45. Judge Sheets — predictive spreadsheets

- **场景与做法**：输入 Urgency 等列标题后，Jev 推断预测类型；确认后通过 JUDGE、PICK、RATE 函数填充各行，同一文本的问题合并请求，结果流式返回并触发表格重算。
- **可借鉴点**：表头意图 → 判断类型 → 逐行评估 → 表格重算。
- **边界**：独立表格演示，并非 Google Sheets 插件；约 100 毫秒指单次判断或表头解析，不是整列处理时间。速度为作者报告，也有 mock 模式。
- **来源**：[项目](https://github.com/dabit3/jev-experiments/tree/main/judge-sheets) · [发现来源帖子](https://x.com/dabit3/status/2100780008193020049)。

**演示素材**: [原作者界面截图与动态演示](https://github.com/dabit3/jev-experiments/tree/main/judge-sheets#judge-sheets--predictive-spreadsheets)

<a id="31-notra--typed-evaluation-in-analytics"></a>

### 46. Notra — typed evaluation in analytics

- **场景与做法**：代码提供通过 Vercel AI Gateway 调用 Jev 的评估客户端、NOTRA_JEV_CLASSIFIERS 开关，并在品牌提及分析中接入可选的结构化评估。
- **可借鉴点**：在已有分析工作流中加入结构化判断，并保留 LLM 回退。
- **边界**：代码能证明接入路径，不能独立证明线上启用状态或延迟；所查流程仍由 LLM 提供竞争对手信息与引用片段。
- **来源**：[项目](https://github.com/usenotra/notra) · [发现来源帖子](https://x.com/yibie/status/2100619188062523695) · [Implementation / 文档](https://github.com/usenotra/notra/blob/main/packages/ai/src/evaluation/client.ts)。

<a id="32-human-compiler--文字质量诊断"></a>

### 47. human-compiler — 文字质量诊断

[项目来源](https://github.com/asfarsadewa/human-compiler)

本地代码分句与查词，Jev 判断清晰度、意图和语气，再由固定规则生成文字诊断报告。

**边界:** 结果依赖评分标准与阈值，不是客观写作质量，也不是模型自由生成的解释。

<a id="33-kill-my-idea--产品想法多维评分"></a>

### 48. Kill My Idea — 产品想法多维评分

[项目来源](https://github.com/monteduro/killmyidea)

Jev 按多个维度为产品想法评分，本地加权规则将结果组合为建议。

**边界:** 属于启发式反馈，未经商业成功预测验证；项目也支持模拟数据。

<a id="34-jev-cv-screening--简历证据与本地策略评分"></a>

### 49. Jev CV Screening — 简历证据与本地策略评分

[项目来源](https://github.com/gtaras7/typesafe-jev/tree/main/cv-screen)

把简历结构化判断与本地评分规则分开存储，已有回答支持的策略调整可直接重算。

**边界:** 新增问题仍需重新判断。示例策略含年龄和兵役条件，不代表推荐招聘政策，也未验证公平性。

<a id="35-jevibe-check--社交帖子与草稿语气标签"></a>

### 50. Jevibe Check — 社交帖子与草稿语气标签

[项目来源](https://github.com/sriganesh/jevibe-check)

用 Jev 为 Bluesky 帖子和草稿标注语气，支持自定义分类与过滤。

**边界:** 仅分析文本，不含图片、视频和完整对话语境，可能误判讽刺表达。

<img src="assets/cases/sriganesh__jevibe-check.png" alt="语气标签与帖子过滤" width="720" />

原作者素材：语气标签与帖子过滤；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/sriganesh/jevibe-check/blob/8c6ab8837265b762699dc6b4a130f9a9a369fd89/docs/screenshots/post-filter.png) · [许可与署名](THIRD_PARTY_NOTICES.md)

**演示素材**: [动态演示](https://github.com/sriganesh/jevibe-check/blob/8c6ab8837265b762699dc6b4a130f9a9a369fd89/docs/jevibecheck.gif)

<a id="36-jev-resume-analyzer--可追溯简历自查"></a>

### 51. JEV Resume Analyzer — 可追溯简历自查

[项目来源](https://github.com/awun8191/jev-resume-analyzer)

按明确标准与可选职位要求检查简历文本，展示每项问题和答案分布。

**边界:** 区分缺失、不适用和无法判断；不提供经过验证的录用预测或 ATS 分数。

<a id="37-lanebreak--客服工单分组与优先级"></a>

### 52. LaneBreak — 客服工单分组与优先级

[项目来源](https://github.com/ndolinschi/lanebreak) · [实现代码](https://github.com/ndolinschi/lanebreak/blob/acf11293f36597c8fb706ae492a9468455b69928/src/lib/product.ts)

用 Choice 分配客服团队、Score 判断优先级、Noul 识别退款意图、流失信号与转人工需求。

**边界:** 未配置 API key 时使用本地规则模拟，模拟结果不属于 Jev 实测。

<a id="38-jev-column-race--千条用户评论多列标注"></a>

### 53. Jev Column Race — 千条用户评论多列标注

[项目来源](https://github.com/goodrahstar/jev-column-race)

批量标注应用评论的情绪、主题、缺陷与流失信号，再支持本地重排，并与 Gemini 对照。

**边界:** 发布耗时来自一组记录运行；模型间一致率或与星级的一致性不等于真实准确率。

<img src="assets/cases/goodrahstar__jev-column-race.png" alt="作者记录的对照运行" width="720" />

原作者素材：作者记录的对照运行；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/goodrahstar/jev-column-race/blob/d9ee360ccd84462f4eab9493a7c2c617d0dab9df/docs/verdict.png) · [许可与署名](THIRD_PARTY_NOTICES.md)

### 54. JevTicketRouter — 带确定性兜底的双语工单分流

[原始来源](https://github.com/GhrezaKh74/JevTicktRouter) · [实现或文档](https://github.com/GhrezaKh74/JevTicktRouter/blob/ee078fcddd85d339b182fb5ba3cce5ae1021d447/backend/JevTicketRouter.Application/Jev/JevTriageQuestions.cs)

.NET 与 React 应用对波斯语或英语工单进行分流：一次请求询问类别、团队、优先级、敏感信息和人工复核需求，再由本地规则处理升级与脱敏。

**实现模式：** 工单 → 五项结构化判断 → 本地复核与脱敏规则。

**边界：** 无密钥演示可使用确定性 Mock。低置信度触发人工复核，不会自动纠正类别、团队或优先级；未实测路由准确率与脱敏覆盖。

**核查日期：** 2026-09-18。

### 55. Transcript Scorecard — 实时客服通话质检

[原始来源](https://github.com/brandonbryant12/transcript-scorecard) · [实现或文档](https://github.com/brandonbryant12/transcript-scorecard/blob/c9232fffbf8bf23b7cf5402dd02ebc54b19eb9cf/apps/api/src/classifier.ts)

概念验证项目逐句重放虚构客服通话文本。每个启用维度对应一个 Score 和一个选择证据句的 Choice，由代码归一化、加权，并将最终评估存入 SQLite。

**实现模式：** 逐步增长的转写文本 → 维度评分与证据句 → 加权评分历史。

**边界：** 展示的是文本重放，不能视为已验证的实时语音识别。每次评估发送当前转写前缀，费用可能随对话增长；文档说明本地演示无认证。未复现评分质量或时延。

**核查日期：** 2026-09-18。

### 56. Paper Trellis Citation Verifier — 论文引文支持度复核

[原始来源](https://github.com/MarissaFamularo/citation-verifier) · [实现或文档](https://github.com/MarissaFamularo/citation-verifier/blob/f9058642274033e62855d3066988418fefa2e272/src/lib/typesafe.js)

稿件复核工具将引文句与源论文段落配对。Claude 可定位引用片段，代码核对引文是否存在，Jev 判断该段落支持、反驳还是未涉及该主张，最终由人工裁决。

**实现模式：** 引文匹配 → 片段选择 → 三类支持度判断 → 人工复核。

**边界：** Jev 读取引用附近的有限窗口或源文开头，并非整篇论文；片段选错或只能取得摘要会限制证据。作者说明阈值未经过生物医学标注集验证；本轮未提交稿件或调用模型。

**核查日期：** 2026-09-18。

### 57. Research Desk — 新闻与公司多阶段判断

[原始来源](https://github.com/0xnairb/research_desk) · [实现或文档](https://github.com/0xnairb/research_desk/blob/main/app/README.md)

演示项目将 yfinance 公司资料与新闻送入分阶段 Jev 管线，完成相关性筛选、排序及机制匹配；请求视图展示各项判断对应的 state 与结构化问题。

**实现模式：** 公司与新闻输入 → 分阶段判断 → 代码筛选与可追溯结果。

**边界：** 作者明确阈值是初始猜测，并非根据实际结果拟合；可查看请求不代表预测准确或投资有效。本轮未验证交易效果、作者报告的费用或时延。

**核查日期：** 2026-09-18。

### 58. JevFilterForX — 时间线内容价值评分

[项目](https://github.com/grayrepo-byte/jev_filter_for_x) · [发现来源](https://x.com/0xLogicrw/status/2100861912590205411)

X 扩展让 Jev 按信息量、可操作性和原创性评分，再由本地权重计算 0–100 分的内容价值；主题和噪声标签另用于过滤及专注模式。

**实现模式：** 帖子文本 → 多维评分与标签 → 加权分数 → 时间线过滤。

**边界：** 侧重时间线评分，与 BlueNoise 的回复过滤及 Jevibe Check 的 Bluesky 标签不同。没有 API 密钥时使用模拟结果；随帖子折叠图片或视频，不代表 Jev 具有相应视觉理解能力。本次未测试评分质量。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

**演示素材：** [作者演示视频](https://github.com/grayrepo-byte/jev_filter_for_x/blob/main/assets/promo/jevfilterforx-promo.mp4) · [封面](https://github.com/grayrepo-byte/jev_filter_for_x/blob/main/assets/promo/jevfilterforx-promo-poster.png)。原作者素材，仅提供外链，不代表 SeeAPI 实测。

### 59. JevScout — 招聘页面导航与岗位匹配

[项目](https://github.com/hqman/JevScout) · [发现来源](https://x.com/0xLogicrw/status/2100861912590205411)

面向编程 Agent 的技能从公司官网出发，通过 CDP 观察并操作 Chrome，让 Jev 判断链接、寻找招聘入口，并按求职者资料对岗位排序。

**实现模式：** 公司官网 → 招聘链接判断 → 岗位发现 → 按求职资料排序。

**边界：** 目前为演示型 MVP，包含 mock 和固定样例流程，不能把这些演示当作真实 Jev 结果。用途是协助求职者寻找岗位，与雇主侧简历筛选不同；本次未测试匹配效果或端到端可靠性。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

## 实验与垂直场景

<a id="39-typesafe-ai-playground"></a>

### 60. TypeSafe AI Playground

- **场景**：通过 Rust CLI 探索 PHI（可识别个人的健康信息）检测、代码注释审核等小型判断任务。
- **做法**：向 Jev 提交明确的分类或评分问题，展示概率或评分结果。
- **可借鉴点**：一个模型接口可以针对不同业务标准构建小工具。
- **边界**：实验工具不构成医疗隐私合规认证；评分与置信概率也不能混用。
- **来源**：[项目 README](https://github.com/markjaquith/typesafe-ai-playground)。

<a id="40-prism-的-jev-判断服务"></a>

### 61. Prism 的 Jev 判断服务

- **场景**：对流动性策略中的分布方式、有害交易流、恢复持有与市场压力给出辅助判断。
- **做法**：`engine/jev-service.ts` 将窄问题映射到 Choice 与 Noul，与既有启发式判断对应。
- **可借鉴点**：先以 shadow/advisory 方式记录与对照模型意见，再评估是否适合进入执行流程。
- **边界**：所核查 Jev 模块明确为 shadow/advisory，不能宣传为 Jev 自动交易或盈利案例。
- **来源**：[项目](https://github.com/irfndi/prism-liquidity-agent)、[Jev 服务实现](https://github.com/irfndi/prism-liquidity-agent/blob/main/engine/jev-service.ts)。

<a id="41-1v1-jev--quickscope-arena"></a>

### 62. 1v1 Jev — Quickscope Arena

- **场景**：浏览器 FPS 游戏中控制对手移动、瞄准、射击等动作。
- **做法**：服务端将结构化游戏状态转换为 Choice/Noul 问题；README 描述决策频率约为 9 Hz，并提供模型不可用时的启发式回退。
- **可借鉴点**：展示连续小决策组成实时交互的方式。
- **边界**：9 Hz 是该项目的决策循环描述，不是所有 Jev 请求的通用性能指标；不是纯视觉游戏控制证据。
- **来源**：[项目 README](https://github.com/emrickgarrett/OneVOneJev)。

<a id="42-jev-trader"></a>

### 63. jev-trader

- **场景与做法**：读取 Monad 上 Kuru MON-USDC 订单簿，用 Jev 判断买卖方向，由程序处理报价、限额与执行。
- **可借鉴点**：订单簿状态 → 方向判断 → 程序处理订单。
- **边界**：默认模型为 mock 动量启发式，需显式配置才能调用 Jev；无私钥时模拟执行，README 中的部署也标注为 dry-run/mock。不能据此证明盈利。
- **来源**：[项目](https://github.com/jarrodwatts/jev-trader) · [发现来源帖子](https://x.com/studio_yebisu/status/2100686990090047569)。

<a id="43-typesafe-mario"></a>

**相关实现：** [aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade) 基于该项目改为 Hyperliquid 多币种独立组合，由 Jev 判断仓位动作。默认使用 mock 判断，无私钥时模拟执行；真实 Jev 调用需要显式配置。作为衍生实现补充，不另计案例；本次未执行交易或验证盈利能力。[作者投稿](https://github.com/logicrw/awesome-jev-projects/issues/1)。核查日期：2026-09-19。

### 64. TypeSafe Mario

- **场景与做法**：将模拟器遥测与内存状态转换为结构化信息，Jev 选择 NES 手柄动作，并给出跳跃和危险程度判断。
- **可借鉴点**：结构化游戏状态 → Choice/Noul/Score → 手柄输入。
- **边界**：模型不接收截图；这是实验性控制器，不能作为通用视觉游戏能力的证据。
- **来源**：[项目](https://github.com/fhshaik/typesafe-mario) · [发现来源帖子](https://x.com/yibie/status/2100619188062523695)。

<a id="44-jev-drone"></a>

### 65. jev-drone

- **场景与做法**：MuJoCo 四旋翼模拟器将相机深度与分割结果转换为场景数据，由 Jev 建议机动动作和风险，普通代码负责飞控与安全。
- **可借鉴点**：代码感知 → 战术判断 → 受约束的控制。
- **边界**：模拟飞行而非真实无人机飞行；Jev 接收 JSON 而非图像，仅提供建议。作者报告单次成功路线，同时明确运行结果存在较大波动。
- **来源**：[项目](https://github.com/RomanSlack/jev-drone) · [发现来源帖子](https://x.com/yibie/status/2100619188062523695)。

<img src="assets/cases/jev-drone-climb.png" alt="MuJoCo drone simulation and Jev tactical judgments" width="720" />

原作者素材：the jev-drone authors · MIT · 未修改 · [来源](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/docs/climb.png) · [许可与署名](THIRD_PARTY_NOTICES.md)

<a id="45-tsai-sc--starcraft-strongarm"></a>

### 66. tsai-sc — StarCraft Strongarm

- **场景与做法**：读取星际争霸试玩版 Strongarm 任务的结构化游戏状态，由 Jev 选择指令，再以鼠标键盘执行。
- **可借鉴点**：结构化策略游戏状态 → 指令选择 → 输入执行。
- **边界**：读取状态和推理时游戏会暂停；作者提供了限定任务的完成证据，并非实时竞技评测，也不是纯像素输入 Agent。
- **来源**：[项目](https://github.com/phyous/tsai-sc) · [发现来源帖子](https://x.com/yibie/status/2100619188062523695)。

**演示素材**: [原作者视频与证据包（含原速及 8 倍速）](https://github.com/phyous/tsai-sc/releases/tag/v0.1.0)

<a id="46-heist-one--潜行游戏守卫判断"></a>

### 67. HEIST ONE — 潜行游戏守卫判断

[项目来源](https://github.com/AbdelStark/heist-one)

Jev 为潜行游戏守卫判断威胁、怀疑程度与意图，服务器代码负责合法动作、物理规则和回退。

**边界:** 项目也有脚本模式；作者记录的一次真实运行不能证明重复成功率。

<img src="assets/cases/AbdelStark__heist-one.jpg" alt="游戏演示画面" width="720" />

原作者素材：游戏演示画面；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/AbdelStark/heist-one/blob/632c9a55a1e5eb2cbf0b9f87db575f0b5eb36e8c/apps/video/public/extraction.jpg) · [许可与署名](THIRD_PARTY_NOTICES.md)

**演示素材**: [原作者 37 秒演示视频](https://github.com/AbdelStark/heist-one/releases/download/v0.1.0/heist-one-launch.mp4)

<a id="47-typesafe-minecraft--游戏动作实验"></a>

### 68. TypeSafe Minecraft — 游戏动作实验

[项目来源](https://github.com/ellistev/typesafe-minecraft-demo)

Jev 根据结构化 Minecraft 状态选择动作，Mineflayer 执行，代码提供候选位置和动作检查。

**边界:** 早期视频采用高层控制，新版直接动作控制是独立实验，不能混用效果证据；不是截图视觉控制。

<a id="48-jev-for-engineers--工程判断示例集"></a>

### 69. Jev for Engineers — 工程判断示例集

[项目来源](https://github.com/Foadsf/jev-for-engineers)

八个 Python 示例将结构化判断用于 CAD、物料清单和变更管理等工程流程，由代码完成后续决策。

**边界:** 小规模合成示例与未充分校准的阈值不能证明适用于实际工程决策。

<a id="49-jev-synergy-screening--文献标题摘要初筛"></a>

### 70. jev-synergy-screening — 文献标题摘要初筛

[项目来源](https://github.com/PistachioAIHQ/jev-synergy-screening)

把纳入选项与原子资格判断组合，用于文献标题和摘要初筛，并对照作者说明的综述标准。

**边界:** 当前 README 评测的是 Cohen ADHD 摘要初筛；摘要信息与过滤规则可能漏掉合格文献，属于研究流程案例。

### 71. Jev JFK Simulation — 机场语音调度演示

[原始来源](https://www.reddit.com/r/AgentZero/comments/1wj6li0/i_tested_typesafes_jev_model_and_made_it_run_a/)

作者演示将 JFK 机场仿真、负责无线电交互的实时语音模型，以及负责运行判断的 Jev 组合起来，展示语音交互与有限决策循环的分工。

**实现模式：** 仿真机场状态与无线电交互 → Jev 判断 → 仿真响应。

**边界：** 证据为作者公开帖与演示，未核实公开实现或完整请求记录；仅为仿真，不能作为真实空管能力证据。本轮未测量时延或判断质量。

**核查日期：** 2026-09-18。

### 72. Jev Canvas — 语音与手势操作画布

[原始来源](https://x.com/jackcheng/status/2100729670991802386)

Jack Cheng 的作者演示结合语音、指向与画布状态，展示 Jev 对图形操作动作和目标的判断，属于创作工具交互案例。

**实现模式：** 语音及指向输入与画布对象 → 动作及目标判断 → 画布操作。

**边界：** 依据收集库留存的作者演示信息；本轮重新打开原帖，但未独立完整重放视频。未核实源码或请求记录，感知依赖与端到端时延仍不明确。

**核查日期：** 2026-09-18。

### 73. Jev Gomoku — 五子棋候选落点选择

[项目](https://github.com/XieChengYuan/jev-gomoku) · [发现来源](https://x.com/fakeWow_/status/2100889184861110572)

九棋盘五子棋实验将文本棋盘及代码生成的候选落点交给 Jev，每步使用一个 Choice 问题；通过五种输入配置探索战术事实、坐标、方向棋线及短程前瞻的影响。

**实现模式：** 棋盘状态 → 确定性候选生成 → Choice 选择 → 合法落子执行。

**边界：** Jev 从启发式候选中选择，而非考虑全部空位；Choice 概率不等于最终获胜概率。在线演示重放已记录的判断，实时对弈需要 API 接入；小规模实验不能证明普遍棋力或某种输入格式更优。

**核查日期：** 2026-09-19（作者文档核查，未运行项目）。

**演示素材：** [作者已录制对局回放](https://xiechengyuan.github.io/jev-gomoku/)。原作者素材，仅提供外链，不代表 SeeAPI 实测。

### 74. jev-plays-pokemon-red — PyBoy 上的宝可梦红，Jev 只在分支点判断

[项目来源](https://github.com/valentynkit/jev-plays-pokemon-red)

确定性代码负责 PyBoy 模拟器里的路线与战斗数值运算，Jev 只在分支点被调用做选择。每个对战回合都会记录一次濒死概率预测，并用 Brier 分数与模拟器 RAM 中的实际结果核对。

**实现模式：** 代码驱动的路线与运算 → 仅在分支点调用 Jev → 逐回合 Brier 分数核对 RAM 实际结果。

**边界：** 作者本人的项目，Brier 分数是作者用自己的测试框架自报的结果，本轮未独立复现。

**核查日期：** 2026-09-19。

## 评测与行为研究

<a id="50-jev-sec-bench--安全判断评测"></a>

### 75. jev-sec-bench — 安全判断评测

[项目来源](https://github.com/Gaurav-Gosain/jev-sec-bench)

用公开数据与逐条结果评测提示注入检测和代码漏洞判断。

**边界:** 作者报告的结果受上下文与阈值影响；不是 NSFW 评测，也不构成完整安全边界。

<img src="assets/cases/Gaurav-Gosain__jev-sec-bench.png" alt="作者安全评测仪表盘" width="720" />

原作者素材：作者安全评测仪表盘；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/Gaurav-Gosain/jev-sec-bench/blob/fdb16b94d37535db9bad77f8ef0faa971bd7d69a/docs/overview.png) · [许可与署名](THIRD_PARTY_NOTICES.md)

<a id="51-jev-behavior-study--能力与失败边界"></a>

### 76. Jev Behavior Study — 能力与失败边界

[项目来源](https://github.com/RINNECODER/jev-behavior-study)

通过文本任务、贪吃蛇和 3D 城市实验研究问题表述及失败边界，提供报告与运行记录。

**边界:** 属于合成、特定任务观察；重复调用不等于独立问题，代码辅助控制与直接控制需区分。

<img src="assets/cases/RINNECODER__jev-behavior-study.png" alt="贪吃蛇研究界面" width="720" />

原作者素材：贪吃蛇研究界面；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/RINNECODER/jev-behavior-study/blob/e4a1d7ec691a91f33d3b5879a780e6f27328f173/snake_demo/research/preview.png) · [许可与署名](THIRD_PARTY_NOTICES.md)

**演示素材**: [城市实验回放](https://rinnecoder.github.io/jev-behavior-study/city_demo/) · [无辅助贪吃蛇运行记录](https://rinnecoder.github.io/jev-behavior-study/snake_demo/web/unassisted.html)

<a id="52-jev-rerank-bench--检索重排对照评测"></a>

### 77. jev-rerank-bench — 检索重排对照评测

[项目来源](https://github.com/anessbelbati/jev-rerank-bench)

基于相同 BM25 候选，对比 Jev 相关性评分与其他重排模型，公开保存的响应和评分代码。

**边界:** 汇总均值不足以确定胜者；按数据集或按查询加权会改变比较结果。

<img src="assets/cases/anessbelbati__jev-rerank-bench.png" alt="作者检索评测图表" width="720" />

原作者素材：作者检索评测图表；图中数据为作者记录，并非 SeeAPI 实测。 MIT · [来源](https://github.com/anessbelbati/jev-rerank-bench/blob/cd9a35b22aeb4187334f7018a0ee1960a7470586/results/quality.png) · [许可与署名](THIRD_PARTY_NOTICES.md)

<a id="53-jev-phishing-bench--钓鱼邮件与原子信号"></a>

### 78. jev-phishing-bench — 钓鱼邮件与原子信号

[项目来源](https://github.com/anisselbd/jev-phishing-bench)

比较直接钓鱼邮件判断与原子信号方案，后者由 Jev 提供信号、本地分类器组合。

**边界:** 合成邮件可能存在模板捷径；直接判断与留出实验测试集不同，不能直接相减作为提升幅度。

**演示素材**: [作者评测图表](https://github.com/anisselbd/jev-phishing-bench/blob/1d56e8c64d029a9554a0874e2ef2901ed196e230/results/chart.png)

<a id="54-jev-headline-bench--标题ab胜负预测"></a>

### 79. jev-headline-bench — 标题A/B胜负预测

[项目来源](https://github.com/Gaurav-Gosain/jev-headline-bench)

让 Jev 在历史 Upworthy 标题之间选择，再与记录的点击结果比较。

**边界:** 历史同篇文章标题配对不能替代面向新网站用户的随机 A/B 测试。

<a id="55-jev司法文本标注--葡语文档多字段研究"></a>

### 80. Jev司法文本标注 — 葡语文档多字段研究

[项目来源](https://github.com/lab-dados/jev-anotacao-sentencas)

将 120 份葡语司法文书的 12 个变量交给 Jev 标注，与生成模型的结构化输出比较。

**边界:** 参考标签流程含模型标注与仲裁，报告准确率并非完全基于人工金标准；不是法律意见工具。

**演示素材**: [作者分字段评测图表](https://github.com/lab-dados/jev-anotacao-sentencas/blob/fe10f3347ed7220d11321aab94f9206fdc21eddf/docs/relatorio_files/figure-typst/fig-campos-output-1.png)

### 81. LLM Chess Jev Player — 合法棋步选择评测

[原始来源](https://github.com/maxim-saplin/llm_chess) · [实现或文档](https://github.com/maxim-saplin/llm_chess/blob/29b5bdaf9dd844134f2c89588642bb4d61703e73/README.md#typesafe-jev-request--response)

适配器将 Jev 接入既有国际象棋评测框架。每一步由代码提供 FEN 棋局、行棋方和合法 UCI 候选，Choice 的答案转为 make_move 动作。

**实现模式：** 棋局与合法候选 → Choice → 执行棋步并记录对局。

**边界：** 合法候选由代码提供，协议成功不等于棋力。Jev 与对话模型使用不同交互协议，排名不能证明通用推理能力；本轮未复跑对局或复现作者数据。

**核查日期：** 2026-09-18。

### 82. Every Judgment Lab — 写作与知识工作检查

[原始来源](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds)

Mike Taylor 的实验集将写作检查、上下文检索与业务分诊拆成有限判断。写作实验用 21 项标准检查 37 份文本；本仓库将整套实验计为一个案例，不把其中 11 个实验拆开计数。

**实现模式：** 文本或任务状态 → 并行量表判断 → 提示进一步复核。

**边界：** 777 项判断少于 0.7 秒是作者报告，非本仓库基准。另一组 12 段合成文本对照漏掉了七个预设缺陷中的一个；文风标签不能证明文本由 AI 撰写。本轮未复现实验。

**核查日期：** 2026-09-18。

### 83. Jev Maze Lookahead — 并行多步规划负向实验

[原始来源](https://github.com/Bud-ro/jev-demos) · [实现或文档](https://github.com/Bud-ro/jev-demos/blob/main/packages/maze_lookahead/README.md)

迷宫实验对比并行询问未来多步与单步决策，并测试相邻格提示；项目明确区分确定性 BFS Mock 与真实 API 运行。

**实现模式：** 迷宫状态 → 候选动作判断 → 环境检查 → 记录成功与失败。

**边界：** 作者报告 quick 多步配置未解出迷宫；加入邻格提示且只问下一步后，十个 5×5 迷宫解出六个。这是特定配置下的作者结果，本轮未复跑，不能泛化为所有空间推理任务。

**核查日期：** 2026-09-18。

## Jev 是什么？

**Jev 是 TypeSafe AI 面向软件自动化推出的 System One 模型，专注于快速、结构化的判断。** 公司创始人 Diogo Almeida 曾在 OpenAI 参与指令遵循与对话能力相关研究，这些工作构成了 ChatGPT 背后研究基础的一部分。Jev 将重点放在程序中的决策环节：接收待处理内容或应用状态，根据预设问题与标准返回选择、评分或概率，再由业务代码决定后续动作。[官方介绍与创始人背景](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

例如，客服系统可以用它判断工单应分给哪个团队；AI Agent 可以用它筛选相关资料、选择下一步操作或检查外部输入；模型网关可以用它判断任务类型，再选择适合的模型执行。它的核心用途是把工作流中反复出现的小判断变成可调用的组件。

Jev 的接口围绕三类判断展开：**Choice** 从候选项中选择，**Noul** 返回条件成立的概率，**Score** 按有序标准评分。与主要生成自然语言的聊天模型相比，Jev 更侧重提供程序可以据此分支、排序和筛选的决策结果。应用仍需设置阈值，并为不确定的结果安排复核或回退流程；概率输出不代表判断一定正确。

## 模型来源与接入方式

**Jev 由 TypeSafe AI 提供。** 可以根据应用运行环境，以及需要直接调用 API 还是让现有 Agent 使用工具，选择合适的接入方式。下面三类资源承担不同职责，平台接入渠道不额外计入应用案例数量。

### TypeSafe 官方直连

独立开发应用或首次接入时，可以先参考 TypeSafe 官方文档和 SDK，了解基础接口。下方的 Python 示例也使用这条接入路径。

| 资源 | 用途 | 来源 |
| --- | --- | --- |
| TypeSafe 官方文档 | 了解模型概念与 API 用法 | [Introduction](https://docs.typesafe.ai/introduction) |
| 官方 Python SDK | 在 Python 程序中调用 TypeSafe API | [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) |
| 官方 JavaScript / TypeScript SDK | 在 JS / TS 程序中调用 TypeSafe API | [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) |
| 官方 GitHub 组织 | 查找 TypeSafe 维护的开发资源 | [typesafe-ai](https://github.com/typesafe-ai) |

本次在官方 GitHub 组织中查到的是 SDK 与开发工具，未找到官方公开的 Jev 模型权重仓库。SDK 开源不等于模型权重开源；社区复现属于独立项目。

### 第三方平台接入

这里的“第三方”是相对于 TypeSafe 而言。以下两个渠道均有平台自己发布的接入文档，适合已经使用对应运行环境或模型调用接口的应用。

| 平台 | 适用情况 | 文档中的接入方式 | 来源 |
| --- | --- | --- | --- |
| Vercel AI Gateway | 应用使用 AI SDK evaluation 接口 | 通过 evaluation API 调用 `typesafe-ai/jev` | [Vercel 文档](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway) · [发布帖](https://x.com/vercel_dev/status/2100378959653507175) |
| Cloudflare | 应用使用 Cloudflare AI binding | 通过 `env.AI.run('typesafe/jev', ...)` 传入状态与问题 | [Cloudflare 文档](https://developers.cloudflare.com/ai/models/typesafe/jev/) · [发现来源帖子](https://x.com/yusukebe/status/2100750454393348237) |

模型标识、认证、请求格式与计费以所选平台为准，不能直接混用不同平台的示例。当前条目已对照平台文档核查，未调用付费 API 实测；收录不代表价格、速度或可用性排名与保证。

### Agent 工具与 MCP 集成

这类工具适合让现有 Agent 调用 Jev 完成判断，属于软件集成，不是独立的模型托管渠道，也不是 Jev 模型本体。

| 工具 | 用途 | 来源 |
| --- | --- | --- |
| Jev MCP（jkudish） | 事实核验、输入筛查与语义候选排序 | [项目仓库](https://github.com/jkudish/jev-mcp) |
| Typesafe MCP（itsmostafa） | 通过 `evaluate` 工具向支持的 Agent 客户端提供结构化判断 | [项目仓库](https://github.com/itsmostafa/typesafe-mcp) |

两个项目均在文档中要求 TypeSafe API 密钥。上方案例清单保留其详细介绍，每个项目只计一次；在自己的程序中直接调用 Jev 时，无需经过 MCP。

### 接入资源收录标准

收录的渠道应明确提供 TypeSafe Jev，具有可用的公开接入文档与服务方信息，并能说明具体的集成价值。条目记录用途、来源与核查范围，不追求穷尽全部服务商。未来若收录 SeeAPI，也必须满足相同标准，并披露 SeeAPI 是本仓库维护方。详见[贡献要求](CONTRIBUTING.md)。

### 三类典型判断

- **Choice**：从候选项中选择，例如把工单分配给账单、技术或其他队列。
- **Noul**：对一个条件成立的可能性给出概率，例如判断消息是否包含垃圾信息。
- **Score**：根据有序标准评分，例如评估回答质量或风险等级。

这些判断由应用代码连接到后续动作。接入时可以直接使用官方 SDK，也可以通过第三方 MCP 工具交给 Agent 调用；不需要经过 `jkudish/jev-mcp` 才能使用 Jev。

### Python 接入示例：工单分类

先安装官方 SDK：

```bash
uv add typesafe-sdk
```

将 `TYPESAFE_API_KEY` 设置在运行环境中，再调用接口：

```python
from typesafe_sdk import Choice, TypeSafeClient

with TypeSafeClient() as client:
    response = client.system_one(
        state={"document": "同一笔订单被扣款两次，请帮我处理。"},
        questions={
            "category": Choice(
                instructions="这条工单应归入哪个类别？",
                criteria={
                    "billing": "账单、扣款或退款问题",
                    "technical": "技术故障或集成问题",
                    "other": "其他问题",
                },
            ),
        },
    )

print(response.choices["category"].choice)
```

示例根据[官方 Python SDK 快速入门](https://github.com/typesafe-ai/typesafe-sdk-python#quickstart)调整工单文本和分类标准，展示真实接口结构；本仓库未执行该 API 请求，不提供虚构的运行结果。

## 发现来源与更新方式

案例中的截图与视频来自对应项目作者，用于展示原项目，不是 SeeAPI 实测结果。已转载素材保留原始署名与许可；外链素材仍由原站托管，不因收录而适用本仓库的文档许可证。详见[素材来源表](assets/cases/README.md)。

各条目依据作者 README、项目文档、实现代码或明确标注的作者演示核查；仅有公开说明或演示的条目单独注明限制。代码核查仅覆盖选定文件，不是完整代码审计；未运行项目或调用付费 API。作者报告的效果不等同于独立验证或生产可用性证明。

9 月 18 日追加更新对照指定收集视图返回的全部 63 条记录与仓库已有 55 条案例，补充 19 条，并保留未出现在该视图的原有案例。覆盖范围与验证限制见[本轮更新核查](docs/reviews/2026-09-18-case-update.md)。

本轮新增线索来自 [StudioYebisu 的项目合集](https://x.com/studio_yebisu/status/2100686990090047569)、[yibie 的案例介绍](https://x.com/yibie/status/2100619188062523695)及 [Nader Dabit 的预测式表格演示](https://x.com/dabit3/status/2100780008193020049)。同一项目只计一次；社区仿制模型不作为官方 Jev 的应用案例收录。

案例线索来自[思维怪怪的原帖](https://x.com/0xLogicrw/status/2100478725393686556)，并参考社区目录 [yibie/awesome-jev](https://github.com/yibie/awesome-jev)、[hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) 和 [rhc98/awesome-jev](https://github.com/rhc98/awesome-jev)。条目描述以项目自己的 README 或实现代码为核查依据，使用独立撰写的中文摘要。

- [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)


后续条目至少保留：项目、场景、Jev 的具体职责、可借鉴点、边界、公开来源及核查日期。作者报告的数据注明来源和样本条件；没有运行验证的项目不标记为“SeeAPI 实测”。

## 许可证

本仓库原创文档采用 [CC BY 4.0](LICENSE)，代码示例采用 [MIT](LICENSE-CODE)。转载文档时请署名 SeeAPI contributors、链接来源与许可证，并注明修改。第三方项目及引用材料保留各自权利和许可；详见[授权范围说明](NOTICE.md)与[第三方许可声明](THIRD_PARTY_NOTICES.md)。
