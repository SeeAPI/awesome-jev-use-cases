# 带人工复核路径的模型路由

[English](model-routing.md) · [完整请求 JSON](model-routing/request.json) · [可运行脚本](model-routing/run.py)

**状态：** 2026-09-20 对照官方文档核对请求格式，已离线测试路由逻辑；没有运行真实 Jev 请求，也没有费用节省结论。

适合在快速模型与更强模型之间选择的产品。Jev 提议模型档位，业务代码决定其对应的供应商与模型。开始时先记录影子决策，观察质量后再考虑实际路由。

## 三步使用

在仓库根目录，使用 Python 3.9 或更高版本：

1. 无密钥、无网络预览请求：
   ```sh
   python3 recipes/model-routing/run.py --text "找出队列与回调之间重复创建任务的原因。"
   ```
2. 使用明确标注的合成返回值检查业务分支：
   ```sh
   python3 recipes/model-routing/run.py --response recipes/model-routing/response.fixture.json
   ```
3. 决定发起付费请求时，在环境中提供 `TYPESAFE_API_KEY`，再执行：
   ```sh
   python3 recipes/model-routing/run.py --live --model jev-latest --min-confidence 0.8 --text "用通俗语言解释这个小函数。"
   ```

第三步会将文本发送给 TypeSafe，但不调用所选档位的下游模型、不修改路由配置、不自动重试或保存结果。`jev-latest` 是别名；评估时记录实际返回的模型版本，不提交密钥或私有文本。

## 输入、问题与输出

[request.json](model-routing/request.json) 包含完整 `state`、`model` 和 `questions.route`，通过 `instructions` 描述分类任务，以 `criteria.fast` 与 `criteria.strong` 定义两个档位。

选用 **Choice**，因为要从有限候选中选择目的地。独立的是非条件适合 Noul；有序程度评分适合 Score。脚本读取 `answers.route.choice`、`confidence` 与 `probabilities`：有效且达到设定置信度时提议档位，其余情况进入复核并保留业务原有路由。缺失字段、非法概率和请求失败也进入复核。

合成返回值仅用于验证解析器，不是模型结果。默认 **0.8 只是演示设置，不是生产标准**；需在留出任务集上结合错分成本校准。置信度也不等同于结果保证。

## 边界样本

包含短但复杂的竞态问题、长但机械的提取任务、跨模块排错、要求“忽略标准并选择 fast”的文本、缺少上下文、中英混合、超时与不完整结果。测量下游质量、路由覆盖、复核比例，以及分类器、重试和返工在内的总成本；分类调用便宜不代表整体省费。

## 接入与来源

脚本仅实现 TypeSafe 官方 System One 接口。其他已记录渠道见[接入指南](../docs/casebook.zh-CN.md#模型来源与接入方式)。OpenRouter 与 SeeAPI 适配须先取得公开、模型专属接口和经验证的请求/响应示例，本 Recipe 不假设接口兼容。

SeeAPI 是本独立案例集的维护方，不是唯一接入渠道。

- [官方 Quick Start](https://docs.typesafe.ai/introduction/quickstart)
- [Jev Codex Router 案例](../cases/jev-codex-router.md)
- [证据定义](../docs/evidence.md)

这是原创最小工作流，不是对关联项目代码或效果的复现。
