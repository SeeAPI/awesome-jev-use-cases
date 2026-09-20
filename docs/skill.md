# Use the Jev solution finder

The [Skill](../SKILL.md) helps find cases, compare evidence and design a typed decision workflow. It can find the model-routing recipe; it does not run models or promise a recipe for every task.

## From a checkout

Ask your agent:

> Read SKILL.md in this repository. Find Jev implementations for ranking search snippets. Compare their inputs, primitives and evidence, then cite the records and propose a workflow with a review path.

For deterministic offline discovery:

```sh
python3 scripts/find_cases.py "reranking" --limit 5
python3 scripts/find_cases.py "模型路由" --limit 3
```

All cases have stable IDs and searchable bilingual purpose summaries; documented reusable patterns are also indexed. Small keyword alias groups cover terms such as captions/subtitles/字幕; this is keyword matching, not semantic search. The curated subset has evidence metadata. Index-only matches point to the complete casebook and require reading its scope; they are not silently upgraded to “tested.” Search weights title, summary and documented tags, with curated metadata breaking ties. The agent must assess task fit and evidence itself.

## Portable installation folder

Build a self-contained copy in a new directory:

```sh
python3 scripts/package_skill.py --output /tmp/jev-solution-finder
```

Use your agent's local-skill installation mechanism to install **the entire folder** named `jev-solution-finder`. Its entrypoint is `SKILL.md`. Keep `content/`, `data/`, `cases/`, `docs/`, `recipes/`, and `scripts/` together; copying only the entrypoint loses its evidence and search resources. The packager does not install into agent settings or overwrite an existing directory.

The package supports the same offline command from within its own directory. Live calls remain opt-in and subject to the user's authorization.

中文：可直接让 Agent 读取仓库根目录 SKILL.md。安装时先生成完整的 `jev-solution-finder` 文件夹，再使用 Agent 的本地 Skill 安装方式；不能只复制 SKILL.md。Skill 负责检索、比较和设计，不代表模型已运行或效果已验证。
