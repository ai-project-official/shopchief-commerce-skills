# 德语商品视频本地化：可执行交付方案

执行性质：独立行为验收。本方案仅依据给定商家输入，以及 `product-video-localization/SKILL.md` 和其 `references/production.md` 编制；未查看 worked-example，未调用外部服务。当前未提供实际视频文件，未合成音频、未生成最终字幕、未渲染成片。下列所有时间为拟定剪辑分配，不是实测时码。

## 已确认事实与文案处理

| 项目 | 原片信息 | 德语版本采用 | 处理 |
|---|---|---|---|
| 商品 | travel mug | Reisebecher | 暂用通用译名，不虚构品牌或容量 |
| 操作 | The lid locks with one twist. | Mit einer Drehung lässt sich der Deckel verriegeln. | 保留源文含义；实片复查要能对应开合动作，不添加防漏或保温承诺 |
| 价格 | $29 | 34 € inkl. MwSt. | 使用商家明确给定的新市场价格，不做汇率换算 |
| 优惠幅度 | 20% off | 不出现百分比 | 未确认；移除画面和配音中全部“20% off”，不计算原价或节省金额 |
| 期限 | ends Friday | Aktionsende: 12.10.2026, 23:59 Uhr (Europe/Berlin) | 使用明确时间，不保留 Friday，不创建倒计时 |
| 声音 | 英文原声 | 获授权通用德语 TTS | 不克隆原说话人，不冒称真人德语配音 |
| 时长 | 15 秒 | 目标 30 秒 | 通过实拍重剪、可用细节、静帧和文字卡延展；不需要视频生成器 |

优惠幅度缺失不阻塞当前版本：采用已确认价格与活动期限即可。若商家后续必须展示“优惠 X%”，仅该文案待确认；其他准备和剪辑仍可进行。

## 完整德语文案

### TTS 可直接输入稿

```text
Entdecke unseren Reisebecher. Mit einer Drehung lässt sich der Deckel verriegeln. Der Preis: vierunddreißig Euro inklusive Mehrwertsteuer. Die Aktion endet am zwölften Oktober zweitausendsechsundzwanzig um dreiundzwanzig Uhr neunundfünfzig, Berliner Zeit. Jetzt entdecken.
```

语气：自然清楚的德语商品介绍；使用现有获授权的通用德语声音。数字展开便于准确发音，不指定不存在的声音 ID 或速度参数。先生成一个获授权候选，读取实际时长并听完整段，再做剪辑和字幕。

若实测配音超过可用 30 秒，先采用下面的较短版本并把完整期限保留在可读的画面文字中；不要直接加速到难以听清，也不要把超长音频截断：

```text
Entdecke unseren Reisebecher. Mit einer Drehung lässt sich der Deckel verriegeln. Für vierunddreißig Euro inklusive Mehrwertsteuer. Das Aktionsende findest du unten im Bild. Jetzt entdecken.
```

较短版本也是候选文稿，不是已生成的音频，使用前应确认相应画面确实完整呈现期限。若音频短于 30 秒，可通过自然停顿、商品细节及末尾价格卡补足，不需要为了填满时长添加新卖点。

### 精确画面文字

- 主标题：`Dein Reisebecher für unterwegs`
- 操作说明：`Mit einer Drehung verriegelt`
- 价格：`34 € inkl. MwSt.`
- 期限两行：`Aktionsende: 12.10.2026, 23:59 Uhr` / `(Europe/Berlin)`
- CTA：`Jetzt entdecken`

不得出现 `$29`、`20% off`、`20 % Rabatt`、`Friday`、旧的原价删除线或未经确认的运费、退货、库存等文案。

## 30 秒剪辑蓝图：全部为暂定目标区间

保持源视频实际画幅和帧率作为初始编辑设定；收到文件后读取真实参数，不预设原片是竖屏或某个分辨率。

| 目标区间（暂定） | 画面与处理 | 字幕／叠加 | 源素材绑定 |
|---|---|---|---|
| 00–04 秒 | 商品整体开场；保留主体完整 | 主标题，U1 对应字幕 | 导入后选择没有旧价或可准确遮盖旧字的全景；实际源时码待记录 |
| 04–11 秒 | 展示一次完整真实旋转锁盖动作，保留自然动作速度 | 操作说明，U2 字幕 | 原片操作镜头实际入出点待查看；不复制拼接成不存在的操作效果 |
| 11–17 秒 | 使用另一真实细节镜头；没有第二镜头时使用已确认清晰商品静帧及轻微取景变化 | 价格首次出现，U3 字幕 | 记录具体源帧；取景不裁掉产品识别特征，不虚构背面或额外结构 |
| 17–26 秒 | 商品静帧或干净底色信息卡，保留清晰商品缩略图（如有合适帧） | 价格和完整期限；U4 字幕 | 现有剪辑器与字幕工具即可完成，不需生成画面 |
| 26–30 秒 | 收尾卡；价格与期限仍可阅读 | CTA，U5 字幕 | 从真实商品帧延展或纯版式收尾；不新增未经授权品牌素材 |

以上区间仅是编辑槽位。实际配音测量后允许移动边界，以保证操作镜头完整、口播自然和条款可读；最终时间线保持目标 30 秒。重复素材优先用于非动作特写，避免机械循环同一手部操作。若缺少合适静帧，使用清楚的信息卡补足，不把“需要视频生成器”列为阻碍。

## 源字幕、译句与最终时码分离

| ID | 已给源文 | 德语译句／作用 | 源时码 | 最终音频／字幕时码 |
|---|---|---|---|---|
| U1 | Meet the travel mug. | Entdecke unseren Reisebecher. | 未提供，查看原片后记入 | 未生成音频，待测 |
| U2 | The lid locks with one twist. | Mit einer Drehung lässt sich der Deckel verriegeln. | 同上 | 待测 |
| U3 | Twenty percent off until Friday. | Der Preis: vierunddreißig Euro inklusive Mehrwertsteuer. | 同上 | 待测；这是获准报价替换，不是逐字翻译 |
| U4 | 源句中的 until Friday | Die Aktion endet am zwölften Oktober zweitausendsechsundzwanzig um dreiundzwanzig Uhr neunundfünfzig, Berliner Zeit. | 源商业条件实际位置待记 | 待测；使用较短稿时改为画面完整期限与对应引导句 |
| U5 | Shop now. | Jetzt entdecken. | 未提供 | 待测 |

不以这些拟定时间生成可误认最终成品的 SRT/VTT。先听实测 TTS，通过字幕编辑器逐句打点；没有强制对齐器时手动听音与拖动时间线足够。字幕显示数字时使用 `34 € inkl. MwSt.` 和完整日期格式，并逐字符核对 `€`、重音字母与标点在实际导出中显示正常。

## 本地执行顺序与恢复办法

1. 导入商家提供的原片，记录文件位置、时长、画幅、帧率和音轨。逐段查看画内文字，建立旧价、20% 和 Friday 的区域／时间范围清单；不能只修改字幕轨。
2. 优先使用无字母版或原编辑工程。只有压制英文文字时，用准确、不遮挡重要商品部位的实色字幕板／价格板盖住原文字。若无法安全覆盖，就舍弃该镜头，改用已经确认的清晰商品静帧或版式卡；不得声称完美移除了旧字。
3. 使用已获授权德语 TTS 渲染一次候选并保存音频。此验收任务禁止真实外部调用，因此此步状态为未执行。执行真实任务时记录实际声音、语言、输出文件和实测时长，不在清单中存凭证。
4. 英文配音不能与德语叠放。若有独立音轨，保留合适的音乐／效果并替换人声；只有混合音轨时，先评估静音或可用的分离方案。没有可用分离能力可整轨静音，采用清楚的德语旁白，明确原操作声不保留；不虚构旋转“咔哒”声来暗示额外锁紧性能。
5. 如源片含正脸讲话，当前没有唇形同步能力：用产品特写／信息卡覆盖讲话画面并将新音轨作为旁白。不把不对嘴的人脸画面标成完成配音。替代画面不足时用商品静帧，仍不需要生成器。
6. 按实际音频重排 30 秒时间线，逐句制作字幕，放置已确认德语价格与期限；检查字幕和优惠信息不互相遮挡，避免条款只出现一闪而过。
7. 本地渲染，实际检查导出时长及完整播放。听清价格、日期、操作句和音频结尾；复核每处旧优惠均已移除，锁盖镜头未改事实。失败仅修对应片段或字幕，不自动增加 TTS 候选或付费尝试。

## 交付清单及当前状态

| 交付 | 建议文件名 | 当前状态 |
|---|---|---|
| 本处理方案与完整译稿 | `shopchief-media-behavior-localization.md` | 已完成本文 |
| 商业条件与翻译台账 | 可从本文建立 `travel-mug-de-DE-localization.csv` | 内容已完整给出，尚未单独导出文件 |
| 德语配音 | `travel-mug-de-DE-voice.wav` | 未生成；实际路径／时长为 null |
| 最终字幕 | `travel-mug-de-DE.srt` | 等待真实音频后定时；未生成 |
| 编辑工程 | `travel-mug-de-DE-project` | 未创建，原片未提供 |
| 30 秒德语成片 | `travel-mug-de-DE-30s.mp4` | 未渲染；无虚构下载地址或视频 ID |

当前可交付的是完整可执行方案、两版可用 TTS 文稿、精确画面文案、事实变更台账和剪辑蓝图。接入实际原片及授权音频执行后，可直接继续现有编辑器工作；未确认优惠百分比无需成为全任务阻塞点。

## 技能质量判断

技能能把本场景推进到可生产状态，没有强制要求视频生成器、原声克隆或自动对齐器。它明确区分商业条件替换和翻译，允许可读文字板处理压字，要求音频实测及逐语言导出，能够避免“泛泛 brief”或伪造完成。

一个可改进点：正文没有直接处理“15 秒扩展为 30 秒”的决策例子，也未明确写出“未确认旧优惠可以省略，继续使用新价格”这一部分完成原则。本次结合其 preserve facts、permitted visual holds 和 available execution 已能完成方案，但增加一段“时长改变用实拍重剪／静帧／信息卡，不默认依赖生成器；未确认商业声明仅阻塞该声明”会降低执行模型整单停住的概率。
