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

收录的渠道应明确提供 TypeSafe Jev，具有可用的公开接入文档与服务方信息，并能说明具体的集成价值。条目记录用途、来源与核查范围，不追求穷尽全部服务商。未来若收录 SeeAPI，也必须满足相同标准，并披露 SeeAPI 是本仓库维护方。详见[贡献要求](../../CONTRIBUTING.md)。

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

案例中的截图与视频来自对应项目作者，用于展示原项目，不是 SeeAPI 实测结果。已转载素材保留原始署名与许可；外链素材仍由原站托管，不因收录而适用本仓库的文档许可证。详见[素材来源表](../../assets/cases/README.md)。

各条目依据作者 README、项目文档、实现代码或明确标注的作者演示核查；仅有公开说明或演示的条目单独注明限制。代码核查仅覆盖选定文件，不是完整代码审计；未运行项目或调用付费 API。作者报告的效果不等同于独立验证或生产可用性证明。

9 月 18 日追加更新对照指定收集视图返回的全部 63 条记录与仓库已有 55 条案例，补充 19 条，并保留未出现在该视图的原有案例。覆盖范围与验证限制见[本轮更新核查](../../docs/reviews/2026-09-18-case-update.md)。

本轮新增线索来自 [StudioYebisu 的项目合集](https://x.com/studio_yebisu/status/2100686990090047569)、[yibie 的案例介绍](https://x.com/yibie/status/2100619188062523695)及 [Nader Dabit 的预测式表格演示](https://x.com/dabit3/status/2100780008193020049)。同一项目只计一次；社区仿制模型不作为官方 Jev 的应用案例收录。

案例线索来自[思维怪怪的原帖](https://x.com/0xLogicrw/status/2100478725393686556)，并参考社区目录 [yibie/awesome-jev](https://github.com/yibie/awesome-jev)、[hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) 和 [rhc98/awesome-jev](https://github.com/rhc98/awesome-jev)。条目描述以项目自己的 README 或实现代码为核查依据，使用独立撰写的中文摘要。

- [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)


后续条目至少保留：项目、场景、Jev 的具体职责、可借鉴点、边界、公开来源及核查日期。作者报告的数据注明来源和样本条件；没有运行验证的项目不标记为“SeeAPI 实测”。

## 许可证

本仓库原创文档采用 [CC BY 4.0](../../LICENSE)，代码示例采用 [MIT](../../LICENSE-CODE)。转载文档时请署名 SeeAPI contributors、链接来源与许可证，并注明修改。第三方项目及引用材料保留各自权利和许可；详见[授权范围说明](../../NOTICE.md)与[第三方许可声明](../../THIRD_PARTY_NOTICES.md)。
