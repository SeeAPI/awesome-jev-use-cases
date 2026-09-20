# Transcript Scorecard — 实时客服通话质检

[English](transcript-scorecard.md) · [简体中文](transcript-scorecard.zh-CN.md)

[阅读完整案例](../docs/casebook.zh-CN.md#case-transcript-scorecard)

本页为元数据参考，完整案例集是主要阅读入口。

概念验证项目逐句重放虚构客服通话文本。每个启用维度对应一个 Score 和一个选择证据句的 Choice，由代码归一化、加权，并将最终评估存入 SQLite。

**证据类型:** `docs-reviewed` · **核查日期:** 2026-09-18 · **SeeAPI 实测:** 否

**判断类型:** choice, score · **后续动作:** score, review

[原始来源](https://github.com/brandonbryant12/transcript-scorecard) · [数据记录](../data/cases/transcript-scorecard.json)

## 适用边界

- 展示的是文本重放，不能视为已验证的实时语音识别。每次评估发送当前转写前缀，费用可能随对话增长；文档说明本地演示无认证。未复现评分质量或时延。

[证据定义](../docs/evidence.zh-CN.md)
