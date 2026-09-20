# Benchmarks and test evidence

[English](README.md) · [Chinese](README.zh-CN.md)

Browse the existing [author-reported studies](../docs/casebook.md#benchmarks--behavior-studies).

**No new independent benchmark results are published by this restructuring.** Offline recipe fixtures test our parsing and routing logic, not Jev accuracy. Existing study results remain attributed to their authors.

A future reproducible report needs:

- A versioned, publishable dataset with labeling rules and ambiguous cases.
- Exact policy, questions, model requested/returned, provider and date.
- Raw responses, failed requests, timing definition and usage; cost only when billing evidence is available.
- Per-class mistakes, coverage, abstentions and test conditions, not just successful examples.
- A runnable evaluation procedure that separates offline validation from paid API execution.

See [evidence requirements](../docs/evidence.md). No execution or publication is authorized merely by adding a dataset or a protocol.
