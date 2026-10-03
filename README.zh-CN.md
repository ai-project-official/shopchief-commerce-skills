# ShopChief Commerce Skills

面向独立站和 DTC 卖家的 **300+ 开源 AI 技能**。从选品、建站、搜索与广告，到客户留存、利润、库存和售后，把具体经营任务变成有依据、可审核的交付物。

[English](README.md) · [复制安装指令](#一键复制安装) · [按任务查找](docs/catalog.md) · [组合工作流](docs/playbooks.md) · [完整案例](examples/README.md) · [ShopChief 官网](https://shopchief.ai/?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=readme_zh)

## 一键复制安装

在当前项目中打开**能执行本地终端的 Codex 或 Claude Code**。点击对应代码块的复制按钮，把整段文字粘贴给 Agent 并发送，即可让它完成项目内安装。当前 [skills CLI](https://github.com/vercel-labs/skills) 需要 **Node.js 22.20+**、npm/npx 和 Git。

**复制给 Codex：**

```text
请在当前项目中为 Codex 安装全部 ShopChief Commerce Skills。
先检查 Node.js 22.20+、npx 和 Git，并读取仓库的技能列表。
保留 .agents/skills 中已有的同名目录或链接。
有同名项时，用明确的 --skill 名称列表只安装缺失技能，报告跳过的名称。
如果没有缺失项，跳过安装并报告已全部存在。
没有冲突时执行：
npx --yes skills@latest add ai-project-official/shopchief-commerce-skills --agent codex --skill '*' --copy --yes
安装后核对 SKILL.md 和随包参考文件，报告新增数、跳过数、目录和失败项。
如需重新加载 Agent，请说明操作。此次只安装，不运行店铺任务。
```

**复制给 Claude Code：**

```text
请在当前项目中为 Claude Code 安装全部 ShopChief Commerce Skills。
先检查 Node.js 22.20+、npx 和 Git，并读取仓库的技能列表。
保留 .claude/skills 中已有的同名目录或链接。
有同名项时，用明确的 --skill 名称列表只安装缺失技能，报告跳过的名称。
如果没有缺失项，跳过安装并报告已全部存在。
没有冲突时执行：
npx --yes skills@latest add ai-project-official/shopchief-commerce-skills --agent claude-code --skill '*' --copy --yes
安装后核对 SKILL.md 和随包参考文件，报告新增数、跳过数、目录和失败项。
如需重新加载 Agent，请说明操作。此次只安装，不运行店铺任务。
```

以上默认安装整个技能库：Codex 安装到项目的 `.agents/skills/`，Claude Code 安装到 `.claude/skills/`。如只需要部分技能，把“全部”改成指定名称，并将 `--skill '*'` 改为例如 `--skill profit-margin-analyzer shopify-product-page-cro`。[完整目录](docs/catalog.md)列出了所有可安装名称。使用技能和随包案例无需 ShopChief 账号。

<!-- skill-overview:start -->
## 技能分类与数量

**共 348 个技能，分为 8 类。** 每个技能包只计一次，中文说明和参考文件不重复计数。

| 分类 | 数量 | 典型任务 |
|---|---:|---|
| [研究与定位](docs/catalog.md#research-and-positioning) | 32 | 选品机会、竞品分析、顾客研究与品牌定位 |
| [店铺与转化](docs/catalog.md#storefront-and-conversion) | 36 | Shopify 建站、商品页、结账流程与商品目录质量 |
| [SEO、GEO 与商品 Feed](docs/catalog.md#search-visibility-and-product-feeds) | 29 | SEO 审查、AI 搜索可见性、结构化数据与购物 Feed |
| [内容与创意](docs/catalog.md#content-and-creative) | 73 | 商品文案、图片、视频、UGC 简报与本地化 |
| [广告与合作](docs/catalog.md#advertising-and-partnerships) | 26 | 广告规划、预算进度、达人合作与联盟营销 |
| [邮件与客户留存](docs/catalog.md#email-and-retention) | 25 | 欢迎邮件、弃购挽回、短信、会员与复购 |
| [经营分析与利润](docs/catalog.md#measurement-and-unit-economics) | 58 | 利润、ROAS、归因、定价与财务对账 |
| [库存、履约与客服](docs/catalog.md#inventory-fulfillment-and-support) | 69 | 补货、采购、物流、退换货与客户服务 |
| **合计** | **348** | |
<!-- skill-overview:end -->

## 从具体任务开始

| 商家任务 | 推荐技能 | 完整案例 |
|---|---|---|
| 算清订单贡献利润 | [利润分析](skills/profit-margin-analyzer/SKILL.zh-CN.md) | [输入表 → 计算结果 → 经营判断](skills/profit-margin-analyzer/assets/worked-example.md) |
| 改善商品页信息 | [商品页优化](skills/shopify-product-page-cro/SKILL.zh-CN.md) | [原文 → 问题清单 → 替换文案](skills/shopify-product-page-cro/assets/worked-review.md) |
| 验证选品机会 | [选品研究](skills/product-opportunity-research/SKILL.zh-CN.md) | 候选、证据与验证建议 |
| 排查店铺搜索问题 | [全站 SEO 审查](skills/site-seo-audit/SKILL.zh-CN.md) | 问题证据与修复顺序 |
| 筹备新品营销 | [DTC 发布计划](skills/dtc-launch-marketing/SKILL.md) | 准备事项、渠道、素材与衡量方法 |
| 判断打折是否划算 | [折扣利润测算](skills/discount-profitability/SKILL.md) | 每单贡献与保住利润所需的订单增量 |
| 减少缺货与库存占款 | [补货规划](skills/inventory-replenishment-planning/SKILL.md) | 库存位置、交期需求与采购建议 |
| 准备新订阅者欢迎邮件 | [欢迎邮件流程](skills/email-welcome-series/SKILL.md) | 触发条件、排除条件、邮件稿与核对项 |
| 排查购买事件漏记 | [GA4 电商衡量](skills/ga4-ecommerce-measurement/SKILL.md) | 事件契约、重复检查和验证步骤 |
| 找出退货原因 | [退货原因分析](skills/returns-reason-analysis/SKILL.md) | 可比较的退货原因占比与证据对应的改进项 |
| 核对商品批量导入 | [商品导入预检](skills/catalog-import-change-preflight/SKILL.md) | [变更行、状态冲突与保留字段](skills/catalog-import-change-preflight/assets/worked-example.md) |
| 解释支付结算差额 | [支付到账核对](skills/payment-payout-reconciliation/SKILL.md) | [交易明细、到账金额与未确认关联](skills/payment-payout-reconciliation/assets/worked-example.md) |
| 判断达人素材能否投广告 | [达人素材付费投放](skills/creator-paid-amplification/SKILL.md) | [使用授权、日期、活动条件与投放判断](skills/creator-paid-amplification/assets/worked-example.md) |

目录按研究定位、店铺转化、搜索与 Feed、内容创意、广告合作、邮件留存、经营衡量和库存售后分组。按当前任务安装即可。

## 安装与首次运行

如需在终端按需安装（需要 Node.js 22.20+、npm/npx 和 Git）：

```sh
npx skills add ai-project-official/shopchief-commerce-skills --list
npx skills add ai-project-official/shopchief-commerce-skills --skill profit-margin-analyzer
```

按安装器提示选择客户端。每个技能包包含参考文件与许可证。入口以英文为主，部分技能附中文说明；可直接要求代理用中文交付。无需 ShopChief 账号。

利润与商品页案例会随对应技能一起安装。安装后可以直接对代理说：

> 使用 profit-margin-analyzer，定位它的安装目录，在该目录运行 scripts/profit_report.py --demo，再对照 assets/worked-example.md 解释计算结果与缺失成本，不要修改价格或广告预算。

使用 **Codex 项目级安装**时，可在项目目录执行以下完整命令（需要 Python 3.10+）：

```sh
npx skills add ai-project-official/shopchief-commerce-skills --skill profit-margin-analyzer --agent codex -y --copy
python3 .agents/skills/profit-margin-analyzer/scripts/profit_report.py --demo
```

预期广告后贡献利润：DEMO-POUCH 为 USD 150，DEMO-BOTTLE 为 USD 80。脚本自动定位随包 CSV。数据为虚构演示，不是客户业绩；其他客户端的安装目录可能不同。

商品页技能安装后，可要求代理读取该技能目录下的 `assets/source-page.md` 和 `assets/product-facts.md`，完成审查和替换文案，再对照 `assets/worked-review.md`。

## 继续处理同一个任务

已经使用 AI 客户端、愿意提供数据导出和配置工具的卖家，适合本地安装。希望在一个工作区里使用内置电商流程、店铺上下文和已支持连接操作的团队，可以使用 [ShopChief](https://shopchief.ai/?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=hosted_workflows_zh)。开源库与产品内技能目录分别发布，实际可用流程与连接器以产品内为准。

可以使用 [ShopChief 利润计算器](https://shopchief.ai/tools/profit-margin-calculator?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=profit_example_zh)检查成本假设，或查看 [Shopify 商品文案工作流](https://shopchief.ai/solutions/shopify-product-descriptions?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=product_page_example_zh)。本地技能和案例仍可独立使用。

## 工具与授权

基础分析可使用商家文件和公开资料。Shopify 写入、付费查询、图片生成分别需要相应工具与授权；缺少工具时交付可完成的文件或审查结果。技能不会自动授权发布、发送消息、花费预算或修改店铺。详见[运行条件](docs/runtime.md)和[验证记录](VALIDATION.md)。

## 贡献与许可

欢迎提交可复现问题和具体任务改进，请使用虚构或已授权脱敏资料。维护方法见[贡献指南](CONTRIBUTING.md)。

ShopChief 原创贡献采用 [MIT](LICENSE)，改编包保留适用的上游许可与声明。各包 `LICENSE` 和 [NOTICE](NOTICE.md) 列明许可与必要署名。
