# Benchmarks and test evidence

Browse the existing [author-reported studies](../docs/casebook.md#benchmarks--behavior-studies) or [中文研究案例](../docs/casebook.zh-CN.md#评测与行为研究).

**No new independent benchmark results are published by this restructuring.** Offline recipe fixtures test our parsing and routing logic, not Jev accuracy. Existing study results remain attributed to their authors.

A future reproducible report needs:

- A versioned, publishable dataset with labeling rules and ambiguous cases.
- Exact policy, questions, model requested/returned, provider and date.
- Raw responses, failed requests, timing definition and usage; cost only when billing evidence is available.
- Per-class mistakes, coverage, abstentions and test conditions, not just successful examples.
- A runnable evaluation procedure that separates offline validation from paid API execution.

See [evidence requirements](../docs/evidence.md). No execution or publication is authorized merely by adding a dataset or a protocol.

本次只建立证据入口，未发布新的独立评测结果。离线样例不属于模型实测；后续报告须保留数据、方法、原始结果、失败与边界案例。
