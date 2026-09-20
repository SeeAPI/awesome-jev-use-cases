---
id: jarrodwatts-jev-trader
category: experiments
order: 630
title:
  en: jev-trader
  zh: jev-trader
source_url: https://github.com/jarrodwatts/jev-trader
legacy_anchors:
  en:
  - 63-jev-trader
  - 42-jev-trader
  zh:
  - 63-jev-trader
  - 42-jev-trader
---

<!-- case:en -->

[Project](https://github.com/jarrodwatts/jev-trader) · [Discovery post](https://x.com/studio_yebisu/status/2100686990090047569)

A trading experiment asks Jev for buy/sell judgments from the Kuru MON-USDC order book on Monad, with code handling quotes, limits, and execution.

**Pattern:** Order-book state → directional judgment → program-controlled order handling.

**Scope:** The default model is a mock momentum heuristic; Jev requires explicit configuration. Without a private key the app dry-runs, and the linked deployment is documented as dry-run/mock. No profitability claim is established.

<a id="43-typesafe-mario"></a>

**Related implementation:** [aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade) adapts this project to Hyperliquid with separate coin portfolios and Jev position decisions. It defaults to mock decisions and dry-runs without a private key; real Jev use needs explicit configuration. Recorded as a derivative rather than a separate case. No trading or profitability validation was performed. [Author submission](https://github.com/logicrw/awesome-jev-projects/issues/1). Reviewed: 2026-09-19.

<!-- case:zh -->

- **场景与做法**：读取 Monad 上 Kuru MON-USDC 订单簿，用 Jev 判断买卖方向，由程序处理报价、限额与执行。
- **可借鉴点**：订单簿状态 → 方向判断 → 程序处理订单。
- **边界**：默认模型为 mock 动量启发式，需显式配置才能调用 Jev；无私钥时模拟执行，README 中的部署也标注为 dry-run/mock。不能据此证明盈利。
- **来源**：[项目](https://github.com/jarrodwatts/jev-trader) · [发现来源帖子](https://x.com/studio_yebisu/status/2100686990090047569)。

<a id="43-typesafe-mario"></a>

**相关实现：** [aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade) 基于该项目改为 Hyperliquid 多币种独立组合，由 Jev 判断仓位动作。默认使用 mock 判断，无私钥时模拟执行；真实 Jev 调用需要显式配置。作为衍生实现补充，不另计案例；本次未执行交易或验证盈利能力。[作者投稿](https://github.com/logicrw/awesome-jev-projects/issues/1)。核查日期：2026-09-19。

