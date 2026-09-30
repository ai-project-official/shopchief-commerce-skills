# ShopChief Commerce Skills

面向独立站和 DTC 卖家的 **40 个开源 AI 技能**，覆盖选品、商品页优化、SEO/GEO、利润分析、Shopify 运营和营销内容。

[English](README.md) · [完整目录](docs/catalog.md) · [完整案例](examples/README.md) · [ShopChief 官网](https://shopchief.ai/?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=readme_zh)

## 从具体任务开始

| 商家任务 | 推荐技能 | 完整案例 |
|---|---|---|
| 算清订单贡献利润 | [利润分析](skills/profit-margin-analyzer/SKILL.zh-CN.md) | [输入表 → 计算结果 → 经营判断](skills/profit-margin-analyzer/assets/worked-example.md) |
| 改善商品页信息 | [商品页优化](skills/shopify-product-page-cro/SKILL.zh-CN.md) | [原文 → 问题清单 → 替换文案](skills/shopify-product-page-cro/assets/worked-review.md) |
| 验证选品机会 | [选品研究](skills/product-opportunity-research/SKILL.zh-CN.md) | 候选、证据与验证建议 |
| 排查店铺搜索问题 | [全站 SEO 审查](skills/site-seo-audit/SKILL.zh-CN.md) | 问题证据与修复顺序 |
| 筹备新品营销 | [DTC 发布计划](skills/dtc-launch-marketing/SKILL.md) | 准备事项、渠道、素材与衡量方法 |

## 安装与首次运行

需要 Node.js 和支持 Agent Skills 的客户端：

```sh
npx skills add ai-project-official/shopchief-commerce-skills --list
npx skills add ai-project-official/shopchief-commerce-skills --skill profit-margin-analyzer
```

按安装器提示选择客户端。技能包包含参考文件与许可证，共有 40 份英文入口、33 份中文说明。无需 ShopChief 账号。

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

可以使用 [ShopChief 利润计算器](https://shopchief.ai/tools/profit-margin-calculator?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=profit_example_zh)检查成本假设，或查看 [Shopify 商品文案工作流](https://shopchief.ai/solutions/shopify-product-descriptions?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=product_page_example_zh)。本地技能和案例仍可独立使用。

## 工具与授权

基础分析可使用商家文件和公开资料。Shopify 写入、付费查询、图片生成分别需要相应工具与授权；缺少工具时交付可完成的文件或审查结果。技能不会自动授权发布、发送消息、花费预算或修改店铺。详见[运行条件](docs/runtime.md)和[验证记录](VALIDATION.md)。

## 贡献与许可

欢迎提交可复现问题和具体任务改进，请使用虚构或已授权脱敏资料。采用 [MIT](LICENSE)，第三方署名与许可见 [NOTICE](NOTICE.md)。

维护完整仓库时执行：

```sh
git clone https://github.com/ai-project-official/shopchief-commerce-skills.git
cd shopchief-commerce-skills
python3 scripts/validate.py
```
