# 商品生图与视频制作

[English](media-production.md) · [复制安装指令](../README.zh-CN.md#一键复制安装)

从要交付的素材选择技能。制作流程会查看商品参考图，编写具体生成或编辑请求，使用当前可用工具执行，再检查和导出结果。没有媒体工具时，会明确交付制作说明，不能把提示词当作已经生成的图片或视频。

## 图片制作

| 卖家任务 | 技能 | 交付内容 |
|---|---|---|
| 制作商品详情页整套图片 | [详情页图组](../skills/product-detail-page-image-production/SKILL.zh-CN.md) | 卖点、细节、规格模块，准确文字图层和移动端切图 |
| 把商品放进可信的使用环境 | [商品场景图](../skills/product-lifestyle-scene-generation/SKILL.zh-CN.md) | 保留商品原貌，匹配比例、光照和接触阴影的场景图片 |
| 展示套装内包含的每件商品 | [套装合成图](../skills/product-bundle-image-composition/SKILL.zh-CN.md) | 多 SKU 合成、准确件数及商品对应清单 |
| 一次促销制作全套素材 | [整套促销物料](../skills/product-campaign-visual-set/SKILL.zh-CN.md) | 共用商品、报价和期限的店铺、邮件、社媒图片 |
| 制作单个商品广告主视觉 | [广告主视觉](../skills/product-ad-key-visual-generation/SKILL.zh-CN.md) | 生成的画面、可编辑的准确广告文字和报价图层 |
| 把图片中的文字换成另一种语言 | [图片本地化](../skills/product-image-localization/SKILL.zh-CN.md) | 保留商品外观与必要说明的本地化图片 |

## 视频制作

| 卖家任务 | 技能 | 交付内容 |
|---|---|---|
| 把商品参考图变成短动态 | [图生视频](../skills/product-image-to-video/SKILL.zh-CN.md) | 限定运动范围的短片、生成任务记录和商品保真检查 |
| 展示商品怎么用 | [商品演示视频](../skills/product-demo-video-production/SKILL.zh-CN.md) | 按真实使用步骤制作、结合实拍或适合生成的镜头的成片 |
| 制作创作者口吻的商品讲解 | [UGC 风格视频](../skills/product-ugc-video-production/SKILL.zh-CN.md) | 有完整脚本的品牌演示，不把虚构角色包装成真实买家证言 |
| 为其他市场制作语言版本 | [视频本地化](../skills/product-video-localization/SKILL.zh-CN.md) | 译配、字幕、画面文字及按实际音频重新对齐的成片 |
| 制作可比较的广告素材版本 | [视频广告变体](../skills/product-video-ad-variants/SKILL.zh-CN.md) | 按指定变量变化的成片和版本清单 |
| 做详情页自动循环短片 | [循环商品视频](../skills/product-loop-video-generation/SKILL.zh-CN.md) | 检查首尾接缝的循环视频，以及封面或静态替代图 |

## 复制给 Agent 安装

在需要安装技能的项目中，把下面这段发给 Codex：

```text
请从 ai-project-official/shopchief-commerce-skills 为当前项目的 Codex 安装 product-detail-page-image-production、product-bundle-image-composition 和 product-image-to-video。保留已有的同名目录或链接，只安装缺失的技能，并检查随包参考文件和案例。安装完成后告诉我当前可用的生图、生视频工具，以及我需要提供哪些商品素材。此次只安装，不提交付费生成任务。
```

使用 Claude Code 时，将“Codex”改成“Claude Code”。需要整库安装时，使用 [README 的复制指令](../README.zh-CN.md#一键复制安装)。

安装后，可以连同真实照片、尺寸一起发送：

```text
使用 product-bundle-image-composition。附上的三张自有商品图分别是套装中的水杯、刷子和收纳袋。请做一张正方形商品图，每件各出现一次，按我提供的尺寸保持比例，标签文字不变。调用当前图片编辑工具，检查结果后交付文件，并说明尚未解决的问题。不要上传到店铺。
```

## 工具和交付

- 生图、生视频需要当前已接入的生成器或本地编辑工具。参考图、遮罩、时长、分辨率、音频和导出格式以所选工具的当前能力为准。
- 图生视频包附 [Runway 脚本](../skills/product-image-to-video/scripts/runway_video.py)，支持离线检查请求、明确提交付费任务、保存任务 ID、继续查状态和下载文件。参见[配置与命令](../skills/product-image-to-video/references/runway-cli.md)。也可以使用其他已连接的生成器。
- 商品款式、数量、卖点、人物和声音以已有素材及授权为准。合成视频不能当作防水、合身、健康效果或真实使用体验的证据。
- 交付要区分提示词、已生成候选、验收通过的成品和未完成项。已做与未做的验证见[验证记录](../VALIDATION.md)。

[商品生图与视觉设计分类](catalog.md#product-images-and-design)和[商品视频与动画分类](catalog.md#product-video-and-animation)还包含策划、剪辑和审核辅助技能，分类总数包含这些辅助任务。
