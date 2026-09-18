# September 18 case update / 9 月 18 日案例更新

## Coverage / 覆盖范围

- The user-supplied collection view returned 63 records with `has_more=false`. This establishes coverage of that view, not of hidden rows or other tables.
- Compared original source URLs with both READMEs: 44 records already included, 19 added. Retained all 55 existing cases, including 11 outside the supplied view; the collection now has 74 cases.
- Read-only collection access through lark-cli. No collection records were changed. Internal notes, attachment tokens, and private workflow fields are not reproduced here.
- 本轮完整读取指定视图返回的 63 条记录，分页结束；不声称覆盖隐藏记录或其他表。按原始来源去重，44 条已收录、19 条新增；保留全部原有 55 条，其中 11 条不在该视图中，总数为 74。

## Evidence / 证据

Original summaries in both READMEs cite public project sources. Fixed revisions are linked where supplied and checked. Current-branch documents can change. No project, model request, benchmark, or deployment was executed. Public author demos are explicitly distinguished from source-backed integrations; prior collection notes are not claimed as new runtime verification.

中英文使用原创摘要并链接公开来源；有固定版本且已核查的条目链接固定版本。未运行项目、模型请求、基准或部署。作者演示与源码可查项目分别说明，收集库既有核查记录不写成本轮运行验证。

| Added case / 新增案例 | Evidence checked / 本轮核查 |
| --- | --- |
| [JevTicketRouter｜带确定性兜底的双语工单分流](https://github.com/GhrezaKh74/JevTicktRouter) | Pinned README and question builder / 固定版本说明与问题构造 |
| [Transcript Scorecard｜实时客服通话质检](https://github.com/brandonbryant12/transcript-scorecard) | Pinned README and classifier / 固定版本说明与分类器 |
| [triage-guard｜支持、告警与部署风险的判断管线](https://github.com/shivam2003-dev/typesafe-triage-guard) | Pinned README and risk battery / 固定版本说明与风险问题组 |
| [typesafe-jev-workflow｜LangGraph 邮件意图分流](https://github.com/GiesN/typesafe-jev-workflow) | Pinned README and workflow / 固定版本说明与工作流 |
| [Paper Trellis Citation Verifier｜论文引文支持度复核](https://github.com/MarissaFamularo/citation-verifier) | Pinned README and Jev adapter / 固定版本说明与 Jev 适配器 |
| [Pi Jev Auto Mode｜工具调用概率门控](https://github.com/jomatsu/pi-jev-auto-mode) | Current README, settings, decision code; conflicting uncertainty defaults / 当前说明、设置与决策代码，不确定性默认值存在冲突 |
| [Capbroker｜权限边界之外的Jev风险提示](https://github.com/suryanshu-singh/capbroker) | Pinned README and HTTP adapter / 固定版本说明与 HTTP 适配器 |
| [LLM Chess Jev Player｜合法棋步选择评测](https://github.com/maxim-saplin/llm_chess) | Pinned branch README and request shape / 固定分支说明与请求结构 |
| [Every Judgment Lab｜写作与知识工作检查](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) | Author article, experiment counts and limitations / 作者文章、实验数量与限制 |
| [Pi Warden｜规则检查与代理行为提醒](https://github.com/DevMortimer/pi-warden) | Current author README including reported benchmark limitations / 当前作者说明及其自报评测限制 |
| [Jev Maze Lookahead｜并行多步规划负向实验](https://github.com/Bud-ro/jev-demos) | Package README distinguishing mock and real runs / 子包说明，区分模拟与真实运行 |
| [Jev JFK Simulation｜机场语音调度演示](https://www.reddit.com/r/AgentZero/comments/1wj6li0/i_tested_typesafes_jev_model_and_made_it_run_a/) | Author Reddit post and description / 作者 Reddit 帖与说明；未取得源码 |
| [Research Desk｜新闻与公司多阶段判断](https://github.com/0xnairb/research_desk) | Root and application READMEs / 根目录与应用说明 |
| [Openroom｜可改规则的实时聊天审核](https://openroom-ivory.vercel.app) | Author post read; backend not verified / 已读作者帖，未验证后端 |
| [JEVScan｜Etherscan地址与交易风险提示](https://x.com/theRaz0r/status/2100898307186864593) | Author post read; implementation and performance not verified / 已读作者帖，未验证实现或效果 |
| [Jev Canvas｜语音与手势操作画布](https://x.com/jackcheng/status/2100729670991802386) | Collection demo notes and original post; full video could not be replayed in this pass / 收集库演示摘要与原帖，本轮未能完整重放视频 |
| [Jev Search｜自然语言搜索意图识别与结果重排](https://github.com/superagents-lab/jev-search) | Pinned README, TypeSafe adapter and pipeline / 固定版本说明、TypeSafe 适配器与管线 |
| [commit-miner｜Git 提交差异分类与安全修复线索](https://github.com/devanshbatham/commit-miner) | Pinned README, miner and request client / 固定版本说明、提交审阅与请求客户端 |
| [Foreman｜编码代理运行时的语义监督与生命周期编排](https://github.com/thruwire/foreman) | Pinned README, model adapter, runtime, terminal and worker interfaces / 固定版本说明、模型适配器、运行时、终端及 Worker 接口 |

## Structure and media / 结构与素材

- Existing seven categories now contain **7, 15, 12, 5, 13, 13, and 9** cases. Both READMEs have the same order and totals.
- Banner placement, browse-first navigation, and the integration guide after the cases are retained. Existing case bodies and media remain unchanged; numbering is updated, with legacy heading anchors retained for existing incoming links.
- No third-party image or video was newly copied into the repository. Author posts remain external links. The earlier 55-case media-tree audit is preserved as a dated snapshot rather than extended without evidence.
- 保留七类导航、Banner 位置和案例后置接入指南；既有案例正文与素材不变，连续编号更新，同时保留原编号锚点。新增条目仅链接作者来源，未公开转载内部附件；此前素材核查表保持历史快照。

## Validation / 验证

Checked bilingual case counts and source order, category totals, all view source links, preservation of the 55 existing case bodies, local links and image paths, legacy anchors, and diff whitespace. These are document checks, not independent validation of the projects' results.

核对双语数量与来源顺序、分类统计、视图来源覆盖、原有 55 条正文保留、本地链接及图片、旧锚点和差异格式。这些是文档检查，不是案例效果的独立复现。
