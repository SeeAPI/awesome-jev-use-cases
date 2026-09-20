## What is Jev?

**Jev is TypeSafe AI’s System One model for software automation, focused on fast, structured judgments.** Founder Diogo Almeida previously worked at OpenAI on instruction following and conversational capabilities, contributing to the research behind ChatGPT. Jev focuses on decisions within applications: it takes content or application state, evaluates predefined questions and criteria, and returns choices, scores, or probabilities that business logic uses to determine the next action. [Official introduction and founder background](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

Examples include assigning support tickets to teams, filtering relevant context for an agent, choosing the next action, screening external inputs, or classifying a task before routing it to another model. The common pattern is turning repeated, bounded judgments into callable software components.

**Choice** selects among candidates, **Noul** returns the probability that a condition holds, and **Score** rates an input against ordered criteria. Compared with chat models primarily used to generate language, Jev focuses on decisions for branching, ranking, and filtering. Applications still need thresholds, review paths, and fallbacks; probability outputs do not guarantee correct judgments.

## Model origin & access options

**Jev is provided by TypeSafe AI.** Choose an access route based on where your application runs and whether you need direct API calls or tools for an existing agent. The resources below serve different roles; platform access channels are not counted as additional application cases.

### TypeSafe official direct access

For a standalone application or your first integration, start with TypeSafe's documentation and official SDKs. They provide the baseline API interface used by the Python example below.

| Resource | Purpose | Source |
| --- | --- | --- |
| TypeSafe documentation | Model concepts and API usage | [Introduction](https://docs.typesafe.ai/introduction) |
| Official Python SDK | Call the TypeSafe API from Python | [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) |
| Official JavaScript / TypeScript SDK | Call the TypeSafe API from JS / TS | [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) |
| Official GitHub organization | Find resources maintained by TypeSafe | [typesafe-ai](https://github.com/typesafe-ai) |

Our review found SDKs and developer tools in the official organization, but no official public Jev model-weight repository. Open-source SDKs do not establish that model weights are open; community reproductions are separate projects.

### Third-party platform access

“Third-party” here means a platform other than TypeSafe. Both entries below have documentation published by the platform itself. They can be useful when your application already uses that platform's runtime or model-access interface.

| Platform | When it fits | Documented integration | Sources |
| --- | --- | --- | --- |
| Vercel AI Gateway | An application using the AI SDK evaluation interface | `typesafe-ai/jev` through the evaluation API | [Vercel documentation](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway) · [Announcement](https://x.com/vercel_dev/status/2100378959653507175) |
| Cloudflare | An application using the Cloudflare AI binding | `env.AI.run('typesafe/jev', ...)` with state and typed questions | [Cloudflare documentation](https://developers.cloudflare.com/ai/models/typesafe/jev/) · [Discovery post](https://x.com/yusukebe/status/2100750454393348237) |

Model IDs, authentication, request schemas, and billing depend on the chosen provider. Follow its documentation rather than mixing examples across platforms. These entries were checked against provider documentation, not tested through paid API calls. Inclusion is not a ranking or a guarantee of cost, speed, or availability.

### Agent tools & MCP integrations

Use these when an existing agent needs to call Jev judgments as tools. They are software integrations, not separate model-hosting providers or the Jev model itself.

| Tool | Role | Source |
| --- | --- | --- |
| Jev MCP by jkudish | Claim verification, input screening, and semantic candidate ranking | [Repository](https://github.com/jkudish/jev-mcp) |
| Typesafe MCP by itsmostafa | An `evaluate` tool exposing typed questions to supported agent clients | [Repository](https://github.com/itsmostafa/typesafe-mcp) |

Both projects document TypeSafe API-key requirements. Their fuller entries appear in the project collection above and are counted only once. An MCP integration is optional when calling Jev directly from your own code.

### How access resources are selected

We list a channel when it identifies the TypeSafe Jev model, publishes usable integration documentation and provider information, and offers a clear integration benefit. We record its purpose, source, and verification limits rather than maintaining an exhaustive provider directory. Any future listing of SeeAPI must meet the same criteria and disclose that SeeAPI maintains this collection. See [contribution requirements](../../CONTRIBUTING.md).

### Three typical judgments

- **Choice:** select a candidate, such as billing, technical, or another ticket queue.
- **Noul:** estimate whether a condition holds, such as whether a message is spam.
- **Score:** rate against ordered criteria, such as answer quality or risk severity.

Application code connects these judgments to actions. You can use an official SDK directly or expose judgments to an agent through an MCP integration; `jkudish/jev-mcp` is not a required intermediary.

### Python example: ticket classification

Install the official SDK:

```bash
uv add typesafe-sdk
```

Set `TYPESAFE_API_KEY` in the runtime environment, then call the API:

```python
from typesafe_sdk import Choice, TypeSafeClient

with TypeSafeClient() as client:
    response = client.system_one(
        state={"document": "I was charged twice for the same order. Please help."},
        questions={
            "category": Choice(
                instructions="Which category should receive this ticket?",
                criteria={
                    "billing": "Billing, charges, or refunds",
                    "technical": "Technical failures or integration issues",
                    "other": "Other issues",
                },
            ),
        },
    )

print(response.choices["category"].choice)
```

Adapted from the [official Python SDK quickstart](https://github.com/typesafe-ai/typesafe-sdk-python#quickstart), with different ticket text and classification criteria. This API request has not been executed for the collection; no example output is fabricated.

## Evidence & scope

Project entries were reviewed against author READMEs, project documentation, implementation files, or explicitly identified author demonstrations. Entries supported only by public descriptions or demos state that limitation. Selected implementation files were inspected; this is not a full code audit. No project was installed, benchmarked, or tested through paid model calls for this collection.

- **Project evidence:** the linked author documentation or implementation describes a concrete Jev integration.
- **Reported measurements:** attributed to their authors, with important conditions retained.
- **Independent validation:** not performed by SeeAPI for this initial collection.

An entry does not imply an official partnership, availability through SeeAPI, production readiness, or endorsement of every claim in its source. Links to default branches may change after the review date.

## Sources & contributions

Initial discovery: [0xLogicrw's Jev project roundup](https://x.com/0xLogicrw/status/2100478725393686556).

Additional case discovery: [StudioYebisu’s project roundup](https://x.com/studio_yebisu/status/2100686990090047569), [yibie’s roundup](https://x.com/yibie/status/2100619188062523695), and [Nader Dabit’s predictive spreadsheet demo](https://x.com/dabit3/status/2100780008193020049). Repeated projects are counted once; community model reproductions are not counted as integrations of the official Jev model.

Additional discovery directories:

- [yibie/awesome-jev](https://github.com/yibie/awesome-jev)
- [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev)
- [rhc98/awesome-jev](https://github.com/rhc98/awesome-jev)

- [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)


Entries are independently summarized from their linked project sources. Screenshots and demo links show the original authors’ work, not SeeAPI test results. Selected screenshots are reproduced with upstream license and attribution notices; other media remain hosted at their source. Third-party materials retain their own licenses and are not relicensed under our documentation license. See the [media source register](../../assets/cases/README.md).

The September 18 follow-up added 19 cases after comparing all 63 records returned by the supplied collection view with the 55 existing entries. It retained existing cases outside that view. See the [update review](../../docs/reviews/2026-09-18-case-update.md) for coverage and verification limits.

See [CONTRIBUTING.md](../../CONTRIBUTING.md) to suggest a concrete project or correction. Please update both language versions and preserve source attribution and evidence boundaries.

## License

Original documentation is licensed under [CC BY 4.0](../../LICENSE); code examples are licensed under [MIT](../../LICENSE-CODE). Attribute SeeAPI contributors, link to the source and documentation license, and indicate changes when reusing the documentation. Third-party projects and materials retain their own rights and licenses. See [licensing scope](../../NOTICE.md) and [third-party notices](../../THIRD_PARTY_NOTICES.md).
