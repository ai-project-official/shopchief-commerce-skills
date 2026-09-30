# ShopChief Commerce Skills

面向独立站和 DTC 卖家的 **40 个开源 AI 技能**，覆盖选品、商品页优化、SEO/GEO、利润分析、Shopify 运营和营销内容。

[English](README.md) · [完整目录](docs/catalog.md) · [使用示例](examples/README.md) · [ShopChief 官网](https://shopchief.ai/?utm_source=github&utm_medium=opensource&utm_campaign=commerce_skills&utm_content=readme_zh)

## 安装与使用

```sh
npx skills add ai-project-official/shopchief-commerce-skills --list
npx skills add ai-project-official/shopchief-commerce-skills --skill profit-margin-analyzer
```

按安装器提示选择你的客户端。安装后描述具体商家任务并提供必要资料，例如：“用这份订单和成本表算出投放前后贡献利润，说明缺失费用，不要修改价格或广告预算。”

## 从实际任务开始

- 选品验证：`product-opportunity-research`。
- 商品页转化改进：`shopify-product-page-cro`。
- 店铺搜索问题：`site-seo-audit`。
- SKU 与渠道利润：`profit-margin-analyzer`。
- 新品营销计划：`dtc-launch-marketing`。
- 社交内容脚本：`dtc-social-content`。


## 运行条件

本仓库提供方法、执行边界与交付要求，不附带 API 账号或连接器。商家文件和公开资料可支持基础分析；Shopify 写入、付费查询、图片生成分别需要相应工具和授权。缺少工具时交付可完成的文件或方案，不能声称已经修改店铺。

Theme Studio 可用于本地主题开发和已授权的草稿主题上传，不包含 ShopChief 的托管项目状态服务。使用技能不需要注册 ShopChief。

```sh
python3 scripts/profit_report.py examples/profit-check/orders.csv
python3 scripts/validate.py
```

示例数据为虚构演示数据，不是客户业绩。详见[运行与验证范围](docs/runtime.md)。

## 许可与贡献

采用 [MIT](LICENSE)，第三方署名见 [NOTICE](NOTICE.md)。欢迎提交可复现问题、具体商家案例和有来源的改进；请勿上传客户隐私、密钥或未经许可的资料。
