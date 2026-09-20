# 使用 Jev solution finder

[English](skill.md) · [简体中文](skill.zh-CN.md)

这个 [Skill](../SKILL.md) 帮助你查找案例、比较证据，并设计结构化判断工作流。它可以找到仓库中的模型路由配方；查找与设计本身不会运行模型，也不保证每种任务都有现成配方。

## 在仓库中使用

将本仓库放入 Agent 工作目录后，可以直接提出需求：

> 读取本仓库的 SKILL.md。查找适合搜索摘要重排的 Jev 实现，比较它们的输入、判断类型与证据，引用原始案例，并给出带人工复核路径的工作流方案。

也可以使用确定性的离线检索：

```sh
python3 scripts/find_cases.py "搜索重排" --limit 5
python3 scripts/find_cases.py "模型路由" --limit 3
```

全部案例都有固定 ID 和可检索的双语用途摘要，已有的可借鉴点也进入索引。检索支持少量经过整理的双语同义词，例如字幕的不同说法；这是关键词匹配，不是语义搜索。

已整理的部分案例带有结构化证据字段。其余结果链接至完整案例集，需要阅读各自的适用边界，不会自动被标记为“实测”。排序考虑标题、摘要、可借鉴点和标签；分数相同时优先显示带有整理后元数据的案例。Agent 仍需判断任务是否匹配，以及证据是否充分。

## 安装为独立 Skill

在仓库根目录生成一个新的完整文件夹：

```sh
python3 scripts/package_skill.py --output /tmp/jev-solution-finder
```

再通过所用 Agent 的本地 Skill 安装方式，安装**整个 `jev-solution-finder` 文件夹**。入口为 `SKILL.md`，需要保留 `content/`、`data/`、`cases/`、`docs/`、`recipes/` 和 `scripts/`；只复制入口文件会丢失证据和检索资源。

打包脚本不会修改 Agent 设置，也不会覆盖已有目录。安装后的完整文件夹内仍可执行上述离线检索命令。真实 API 调用需要主动开启，并遵守当前会话的授权要求。
