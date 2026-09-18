# Awesome Jev Use Cases — Jev 应用场景与案例

简体中文 | [English](README_en.md)

由 [SeeAPI](https://github.com/SeeAPI) 整理。最近核查：2026-09-18。

Jev 是 TypeSafe AI 面向软件决策的 System One 模型。应用将当前状态与明确的问题交给它，取得可供程序使用的选择、评分或概率，再由代码控制后续流程。[官方介绍](https://typesafe.ai/)

本清单收录 16 个公开项目：原帖中的 14 个项目，以及补充的 2 个内容审核项目。已阅读各项目当前 README，对图片审核、桌面自动化和交易判断补查了实现代码；未运行项目或调用付费 API。项目存在、作者报告的效果、实际生产可用性是不同层次的证据。

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

## 自动化与开发工具接入

### 5. Jev Ultrafast

- **场景**：浏览器中逐步完成查询、点击与表单输入。
- **做法**：将可见页面控件整理成带索引的候选集合，Jev 选择操作与目标；需要输入文字时再调用文字生成模型。
- **可借鉴点**：把“选择动作”和“生成文字”拆开，缩小每次决策范围。
- **边界**：作者报告的约 7.1 秒航班搜索是特定任务演示，计时从首次页面观察之后开始，不是任意网页任务的速度保证。
- **来源**：[项目与测量边界](https://github.com/browser-use/jev-ultrafast)。

### 6. agent-desktop 中的 Jev 桌面控制

- **场景**：通过桌面应用的 Accessibility Tree 选择控件和动作。
- **做法**：观察当前界面结构，将操作及目标作为受限选项交给 Jev，再由本地执行器执行并重新观察。
- **可借鉴点**：界面状态、模型决策、本地执行各自承担明确职责。
- **边界**：`agent-desktop` 是通用桌面工具，Jev 是其中的具体集成；不能把整个仓库都称为 Jev 专属项目。
- **来源**：[项目](https://github.com/lahfir/agent-desktop)、[Jev 运行循环](https://github.com/lahfir/agent-desktop/blob/main/scripts/jev/run.mjs)。

### 7. Typesafe MCP（itsmostafa）

- **场景**：让 Claude Code、Claude Desktop、Codex 调用 Jev 进行工单分流等判断。
- **做法**：通过 `evaluate` 接收状态与问题，支持 Noul、Choice、Score，并返回 TypeSafe 响应。
- **可借鉴点**：一次调用可以对同一状态提出多个独立问题。
- **边界**：它是接入工具，不应把可配置的示例场景全部写成已上线客户案例。
- **来源**：[项目 README](https://github.com/itsmostafa/typesafe-mcp)。

### 8. SemDecide

- **场景**：在命令行、CI 或数据流水线中做语义判断、路由、评分与过滤。
- **做法**：提供 `is`、`choose`、`score`、`filter` 和 `guard` 命令，将不确定性、阈值与进程退出码纳入接口。
- **可借鉴点**：既输出判断结果，也明确表示“不确定”和“调用失败”。
- **边界**：模型判断不是权限系统；自动执行仍由调用方流程决定。
- **来源**：[项目 README](https://github.com/sharziki/semdecide)。

## 模型成本与代码工作流

### 9. Jev Codex Router

- **场景**：按编程任务难度选择模型与推理深度。
- **做法**：每轮先由 Jev 分类，再按策略路由到不同模型，记录结果并处理低置信度或错误。
- **可借鉴点**：在质量、延迟和费用之间建立可观察的路由策略。
- **边界**：约 60% 成本下降来自作者对 237 个真实 turn 的回放自测，不是 SeeAPI 实测或普遍承诺。
- **来源**：[项目及回测入口](https://github.com/0xNatoshi/jev-codex-router)。

### 10. Winnow

- **场景**：压缩进入 Claude Code 上下文的长工具输出。
- **做法**：Jev 判断分块内容是否与当前任务有关；高置信度无关内容替换为摘要或占位说明，原文缓存并支持按需恢复。不确定内容保留。
- **可借鉴点**：保留召回机制的上下文筛选，而非直接删除信息。
- **边界**：筛选判断与摘要生成是不同步骤；配置其他判断适配器时不能把结果一概归为 Jev 效果。
- **来源**：[项目 README](https://github.com/GhalebDweikat/winnow)。

### 11. Jev Review

- **场景**：对 Git diff 或代码库进行结构化风险审查。
- **做法**：依次判断风险、文件特征、证据位置、机制和严重性，并按条件路由后续审查。
- **可借鉴点**：用一系列小判断定位值得深入检查的代码片段。
- **边界**：作者将其定位为实验；当前不集成编译器诊断或静态分析，结果是审查线索而非缺陷证明。
- **来源**：[项目 README](https://github.com/devagrawal09/jev-review)。

## 语义搜索与知识导航

### 12. Blink

- **场景**：根据自然语言问题在代码目录中查找相关文件。
- **做法**：Jev 对文件和目录名称进行判断，多个 walker 按路径倾向继续探索。
- **可借鉴点**：将语义判断用于逐层缩小搜索空间。
- **边界**：结果百分比是到达该文件的 walker 占比，不能直接当成文件正确率；这也不是完整源码语义索引。
- **来源**：[项目 README](https://github.com/ellipsis-dev/blink)。

### 13. neo4jev

- **场景**：在 Neo4j 知识图谱中按目标逐跳选择关系。
- **做法**：将出边转换为 Choice 选项，同时用 Noul 判断是否到达目标，再用 beam search 探索候选路径。
- **可借鉴点**：模型选择候选关系，搜索算法负责路径扩展和排序。
- **边界**：演示项目；缺少有效 API 调用时存在明确标注的替代答案路径，演示运行不等于每一步都来自 Jev。
- **来源**：[项目 README](https://github.com/jexp/neo4jev)。

## 实验与垂直场景

### 14. TypeSafe AI Playground

- **场景**：通过 Rust CLI 探索 PHI（可识别个人的健康信息）检测、代码注释审核等小型判断任务。
- **做法**：向 Jev 提交明确的分类或评分问题，展示概率或评分结果。
- **可借鉴点**：一个模型接口可以针对不同业务标准构建小工具。
- **边界**：实验工具不构成医疗隐私合规认证；评分与置信概率也不能混用。
- **来源**：[项目 README](https://github.com/markjaquith/typesafe-ai-playground)。

### 15. Prism 的 Jev 判断服务

- **场景**：对流动性策略中的分布方式、有害交易流、恢复持有与市场压力给出辅助判断。
- **做法**：`engine/jev-service.ts` 将窄问题映射到 Choice 与 Noul，与既有启发式判断对应。
- **可借鉴点**：先以 shadow/advisory 方式记录与对照模型意见，再评估是否适合进入执行流程。
- **边界**：所核查 Jev 模块明确为 shadow/advisory，不能宣传为 Jev 自动交易或盈利案例。
- **来源**：[项目](https://github.com/irfndi/prism-liquidity-agent)、[Jev 服务实现](https://github.com/irfndi/prism-liquidity-agent/blob/main/engine/jev-service.ts)。

### 16. 1v1 Jev — Quickscope Arena

- **场景**：浏览器 FPS 游戏中控制对手移动、瞄准、射击等动作。
- **做法**：服务端将结构化游戏状态转换为 Choice/Noul 问题；README 描述决策频率约为 9 Hz，并提供模型不可用时的启发式回退。
- **可借鉴点**：展示连续小决策组成实时交互的方式。
- **边界**：9 Hz 是该项目的决策循环描述，不是所有 Jev 请求的通用性能指标；不是纯视觉游戏控制证据。
- **来源**：[项目 README](https://github.com/emrickgarrett/OneVOneJev)。

## 发现来源与更新方式

案例线索来自[思维怪怪的原帖](https://x.com/0xLogicrw/status/2100478725393686556)，并参考社区目录 [yibie/awesome-jev](https://github.com/yibie/awesome-jev)、[hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) 和 [rhc98/awesome-jev](https://github.com/rhc98/awesome-jev)。条目描述以项目自己的 README 或实现代码为核查依据，使用独立撰写的中文摘要。

后续条目至少保留：项目、场景、Jev 的具体职责、可借鉴点、边界、公开来源及核查日期。作者报告的数据注明来源和样本条件；没有运行验证的项目不标记为“SeeAPI 实测”。
