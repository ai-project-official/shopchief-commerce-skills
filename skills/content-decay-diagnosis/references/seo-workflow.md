# SEO / GEO evidence, repair and review contract

## One scoped workspace artifact
Before work, resolve tenant/store, target domain, selected pages/products, market, search language and user intent from current context. Ask only for missing decision-critical input; never silently select another store or market. Read the existing evidence artifact before research. Keep one ledger per task with:
- artifact ID and task ID; scope, page types, discovered/visited/skipped pages and observation window;
- evidence ID, source URL or authorized connection/file, retrieval time, measurement period, market/language/platform, observed/estimated/inferred classification and limitations;
- provider task IDs, acceptance/completion/failure status, returned cost and cumulative cost (unknown is not zero);
- issue ID stable across handoffs, dimension, affected URLs, SEO/GEO impact, evidence IDs, priority with reason, concrete repair, acceptance check and current state;
- before/after field values, authorization reference, execution receipt, backend readback, storefront verification, baseline and next review window.
Deduplicate by the scoped canonical page/issue, preserving the original issue ID. Save updates to the same logical ledger and link new artifact versions to the baseline. Do not create a new business collection or pretend a workspace file is an automatic cache.

## Evidence and capability boundaries
Use only `dataforseo_docs_list_sections`, `dataforseo_docs_index`, `dataforseo_docs_search`, `dataforseo_api_request`, as documented in [the query contract](dataforseo-contract.md). Confirm the actual names against loaded schemas before use. The platform administrator role, enabled feature, tenant/store/user context, tool policy and budget govern availability; skills cannot grant access. Discover exact endpoint documentation first. Reuse matching market/time evidence and task IDs; never repeat a paid query to reformat a report or poll by resubmission.
GSC indexing/inspection evidence is different from a public page appearing indexable. Without an actual authorized GSC connection or dated export, mark Google index status unverified. GA4 visits, order outcomes, provider estimates and AI samples remain separate. Extract real JSON-LD/microdata before deciding whether markup or a field is missing. Unavailable extraction is not absent markup.

## Diagnosis, repair and specialist handoff
A diagnostic request produces evidence and a repair plan without store writes. An optimization request continues to complete content and reviewable field changes, executes within actual existing authorization, and reads back the result. Do not repeatedly request permission already granted for that exact action. New publication, outreach, budget or monitoring actions need actual authorization. If a tool or template permission is missing, finish the supported deliverable and make a concrete development task with path/template, intended behavior and acceptance steps. Never label it repaired.
For pages, articles and links deliver actual copy, fields and verified source/target links, not only outlines. Verify backend fields and public rendered pages separately; a successful mutation does not prove the storefront updated. Preserve product truth, market, prices, inventory and supported schema. Finish the requested scope rather than manufacturing more skills.

## Reports and follow-up
Use text for short explanations. When a substantial report or page is requested/useful, create a complete self-contained UTF-8 HTML file under an `outputs/` directory inside the current authorized workspace, with inline CSS, embedded images and local scripts only when useful. No external dependencies, credentials, fabricated scores, invented charts or fake metrics. List real sources, dates, sample limits, missing data, issue IDs, changes and baselines. Keep key conclusions in the chat text.
Call `save_resource` with the real `file_path`; inspect success and the returned stable key/asset ID. Only report delivery once saved. Use `reveal_file` if a separate display operation is needed; reuse the same persisted file identity rather than saving a duplicate. A code block or sandbox path alone is not delivery. Store HTML as a file, not `content_text` pretending to be a previewable file.
For an SEO report with an actual issue register and baseline, pass `content_json={"seo_review":{"issue_ids":["actual issue ID"],"baseline_period":"actual baseline dates"}}` alongside `file_path` to `save_resource`. Replace example values with real ledger values; omit this metadata if no baseline exists. These fields persist with the asset. Chat renders “Review optimization results” / “复查优化效果” beneath the file and carries its actual asset ID, issue IDs and baseline into the existing current-conversation follow-up action. Do not invent a recommendation tool or reference. No recurring task is created. The follow-up reads [the review procedure](review-procedure.md).

## 中文执行要点
全程沿用当前租户/店铺、目标市场与语言。先读取已有成果，统一记录来源、采集时间、观测周期、观测/估计/推断、任务状态、费用、稳定问题标识、修复前后值和基线；跨专项更新同一问题，不重复付费。
只诊断不写店铺；请求优化则交付成品和字段级修改并在已有授权范围执行，分别核验后台回读与前台渲染。能力缺失时交付可用部分及具体开发任务，不声称已修复。不绕过 DataForSEO 管理员、权限和预算，不假装已连接 GSC，也不把公开可索引性当实际收录。
有价值的报告生成完整自包含 HTML，以真实保存工具返回的文件身份交付，并保留对话摘要。使用实际后续问题能力给出“复查优化效果”，问题中带回真实 artifact、问题标识与基线；不创建第七张首页卡或未授权定时任务。
