# What the evidence establishes

[English](evidence.md) · [Chinese](evidence.zh-CN.md)

A useful implementation can still have untested results. We record what was checked separately from what the author claims. Evidence is task-specific: a text test says nothing about native image understanding.

| Label | Required support | Does not establish |
| --- | --- | --- |
| `source-reviewed` | An identified public source and dated review | Code inspection or execution |
| `docs-reviewed` | Documentation explaining the integration and its decision flow | Runtime correctness or independently measured accuracy |
| `author-demo` | An attributed demonstration with stated limits | Independent reproduction or production readiness |
| `seeapi-tested` | A SeeAPI run report identifying inputs, configuration, returned model and failures | General accuracy beyond that run |
| `independently-benchmarked` | Independent evaluation with public dataset, method, raw results and reproducible procedure | Performance on unrelated workloads |

These are evidence types, not a universal quality ladder. An author video does not outrank clear implementation documentation for a code-level question. Match the task first; prefer relevant, reproducible evidence when comparing like-for-like results. Never rank cases solely by stars.

The initial 12 structured records carry forward the repository's documented reviews. None is newly marked SeeAPI-tested by this restructuring. Entries outside that subset retain their original prose limits until their metadata is reviewed. Author benchmark repositories remain `docs-reviewed` when we have only read their documentation.

Promotion requires a report path; independent benchmarks also require a dataset path. Reports must distinguish human labels, synthetic fixtures, author measurements and independent runs. Record unknown values as unknown rather than inventing them. Keep requested and returned model identifiers, date, input/policy versions, exclusions, failures and sampling conditions.
