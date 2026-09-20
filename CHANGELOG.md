# 更新记录 / Changelog

## 2026-09-20

- Skill、证据、维护、配方目录、评测指南及案例参考页拆分为独立中英文版本；英文 Skill 示例改用英文查询，中文首页链接至中文指南。

- 首页 83 个案例补充关键边界，55 个有原始模式说明的案例展示可借鉴点；完整正文与原始核查证据保留。
- 六个精选补充可借鉴点与作者素材入口；新增工单分流作者截图（外链，明确 Mock 模式），共三个精选有截图，另三个使用固定版本实现说明链接。

- 首页首段与导航突出 Jev solution finder Skill；分类目录前增加能力说明、可复制的任务示例及使用安装入口。

- 分类目录前置并增加用途说明；六个精选覆盖不同任务，全部案例保留紧凑摘要，首页弱化内部数据迁移信息。
- 83 个案例迁为独立双语源文件，固定 ID 与旧锚点保留，分类显式配置、显示编号自动生成；完整 Casebook 为主要详情入口。
- 全量检索加入双语摘要与常用同义词，修复正文用途无法被检索的问题；增加插入案例、分类重排及检索回归检查。
- 增加案例推荐、纠错、PR 模板及只读权限的 PR 检查工作流（本地准备，尚未上线运行）。

- 将完整的 83 条双语案例移至 Casebook，首页展示六个精选案例、两张原有截图及全部案例用途摘要；保留原编号锚点、旧中文入口、全部案例正文与素材链接。
- 首批 12 条案例建立双语 JSON 与证据字段，增加 Schema、生成脚本、检索脚本、迁移保留检查和本地链接检查。
- 新增模型路由 Recipe、默认离线的请求脚本、合成返回值与业务分支测试；未调用真实模型，不新增实测或 Benchmark 结论。本轮不涉及文本 NSFW 测试。
- 新增可打包的 Jev solution finder Skill、llms.txt、证据与维护说明。改动不包含部署、发布或流量增长承诺。
- Preserved all 83 bilingual case narratives in the Casebook; added six expanded featured cases, two attributed screenshots, and purpose summaries for every case on the homepage. Added 12 structured records, schema/generation checks, an offline-tested model-routing recipe, and a portable discovery Skill. No new live-model measurements or independent benchmark results.

## 2026-09-19

- Added five community contributions from [PR #2](https://github.com/SeeAPI/awesome-jev-use-cases/pull/2): jev-skip, jev-belay, jev-commit, jev.nvim, and jev-plays-pokemon-red (83 projects total), with corrected evidence limits in both languages.
- 收录 PR #2 的 5 个社区项目，中英文共 83 条；补充字幕依赖、模拟演示、钩子策略及尚未公布校准结果等边界。

- Added BlueNoise, JevFilterForX, JevScout, and Jev Gomoku (78 projects total), with bilingual descriptions and demo links. Added a related trading implementation and a discovery directory.
- 新增 BlueNoise、JevFilterForX、JevScout 和 Jev Gomoku，中英文案例共 78 个；补充演示链接、交易相关实现及发现目录。

## 2026-09-18

- 按收集视图完整返回的 63 条记录核对，44 条已收录，新增 19 条；保留视图外的 11 条原有案例，中英文共 74 条。新增条目按现有七类组织，保留实现模式、证据边界与核查日期，同步导航数量；未转载内部附件或执行案例。
- Compared all 63 records returned by the supplied collection view: 44 already included, 19 added, and 11 existing cases outside that view retained (74 total). Updated both languages and category counts; preserved evidence limits and review dates without redistributing internal attachments or executing projects. See the [review record](docs/reviews/2026-09-18-case-update.md).

- 首批收录 16 个 Jev 应用项目，中文首页优先，并提供英文版。
- 覆盖内容审核、自动化、工具集成、模型路由、代码审查、语义搜索、知识图谱与垂直实验。
- 根据当前实现，将 typesafe-on-neon 更新为安全审核网关，注明其独立的视觉描述步骤。
- 补充来源、核查范围和贡献规范。
- 扩充模型介绍，区分 Jev、官方 SDK 与第三方 MCP，并加入官方来源和 Python 调用示例。

Initial collection of 16 projects with a Chinese-first homepage, English translation, evidence boundaries, and contribution guidelines.

- 增加中英文语言徽章、文档 CC BY 4.0 与代码 MIT 许可，以及适用范围和第三方声明。

- 默认首页调整为英文 README.md，中文移至 README_zh.md；同步语言徽章与贡献指南。
- Switched the default README to English, with Simplified Chinese in README_zh.md.

- 从 7 条提供的帖子核查补充 11 个项目，案例总数更新为 27；增加 Vercel 与 Cloudflare 接入资源，平台渠道不计入案例数量。
- Reviewed seven supplied posts; added 11 projects (27 total) and two separate access-channel resources, with source attribution and implementation limits.

- 按官方直连、第三方平台和 Agent/MCP 工具重组接入资源，补充适用情况与收录标准；项目总数仍为 27。
- Reorganized access resources into direct TypeSafe access, third-party platforms, and agent/MCP tools, with selection criteria; project count remains 27.

- 为 7 个案例补充素材：2 张保留上游 MIT 许可的截图，以及 5 组原作者演示链接；增加素材来源与署名记录。
- Added media to seven cases: two upstream MIT-licensed screenshots and five sets of original demo links, with attribution and media provenance.

- 核对新增来源中的 42 条记录，跳过 14 个已收录项目，补充 28 个应用、集成与评测研究；中英文同步更新为 55 条，研究类独立分类，并保留模拟模式与证据限制。
- Compared 42 source records with the collection, skipped 14 existing projects, and added 28 applications, integrations and studies (55 total). Updated both languages and separated benchmarks from application cases.

- 核查全部 55 个案例的 README 与文件树，新增 9 张保留上游 MIT 许可的图片，补充原作者演示、GIF、回放和评测图表入口，并记录逐案例素材覆盖情况。
- Reviewed READMEs and repository trees for all 55 cases; added nine MIT-licensed images, original demo/GIF/replay/chart links, and a per-case media coverage audit.
