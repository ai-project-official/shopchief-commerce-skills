# ShopChief Commerce Skills

面向独立站和 DTC 卖家的 **300+ 开源 AI 技能**。从选品、建站、搜索与广告，到客户留存、利润、库存和售后，把具体经营任务变成有依据、可审核的交付物。

[English](README.md) · [按任务查找](docs/catalog.md) · [组合工作流](docs/playbooks.md) · [完整案例](examples/README.md) · [ShopChief 官网](https://shopchief.ai/?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=readme_zh)

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

需要 Node.js 和支持 Agent Skills 的客户端：

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

欢迎提交可复现问题和具体任务改进，请使用虚构或已授权脱敏资料。ShopChief 原创贡献采用 [MIT](LICENSE)，改编包保留适用的上游许可与声明。各包 `LICENSE` 和 [NOTICE](NOTICE.md) 列明许可与必要署名。

维护完整仓库时执行：

```sh
git clone https://github.com/ai-project-official/shopchief-commerce-skills.git
cd shopchief-commerce-skills
python3 scripts/validate.py
```
