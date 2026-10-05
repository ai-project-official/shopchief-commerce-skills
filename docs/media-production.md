# Product images and video

[中文](media-production.zh-CN.md) · [Install skills](../README.md#install-with-codex-or-claude-code)

Start with the asset you need to deliver. These workflows inspect your actual product references, prepare a concrete generation/edit request, execute with an available tool, then check and export the result. With no media tool, they return a labeled production specification; they do not claim an image or video was created.

## Image production

| Merchant task | Installable skill | Delivery |
|---|---|---|
| Build a product-page image sequence | [product-detail-page-image-production](../skills/product-detail-page-image-production/SKILL.md) | Coordinated benefit/detail/specification modules, accurate text layers and mobile exports |
| Show a product in a believable setting | [product-lifestyle-scene-generation](../skills/product-lifestyle-scene-generation/SKILL.md) | Product-preserving scenes with matched scale, lighting and contact shadows |
| Show exactly what a bundle contains | [product-bundle-image-composition](../skills/product-bundle-image-composition/SKILL.md) | Multi-SKU compositions with verified quantities and included-item mapping |
| Turn one promotion into a visual set | [product-campaign-visual-set](../skills/product-campaign-visual-set/SKILL.md) | Consistent store, email and social assets with the same approved offer |
| Produce a product ad's key visual | [product-ad-key-visual-generation](../skills/product-ad-key-visual-generation/SKILL.md) | Generated artwork plus precise editable offer/copy layers |
| Localize text inside existing images | [product-image-localization](../skills/product-image-localization/SKILL.md) | Localized copy and renders preserving product identity and required qualifiers |

## Video production

| Merchant task | Installable skill | Delivery |
|---|---|---|
| Animate a product reference image | [product-image-to-video](../skills/product-image-to-video/SKILL.md) | A bounded motion clip, task receipt and product-fidelity review |
| Show how the product works | [product-demo-video-production](../skills/product-demo-video-production/SKILL.md) | A demonstration assembled from verified steps and suitable footage/generated scenes |
| Make a creator-style product explanation | [product-ugc-video-production](../skills/product-ugc-video-production/SKILL.md) | A scripted brand demonstration; synthetic presenters are not real customer testimonials |
| Deliver a video in another language | [product-video-localization](../skills/product-video-localization/SKILL.md) | Localized narration, subtitles, on-screen text and a timed final edit |
| Make controlled ad creative variants | [product-video-ad-variants](../skills/product-video-ad-variants/SKILL.md) | Exports with a specified changed variable and a variant manifest |
| Make a looping product-page clip | [product-loop-video-generation](../skills/product-loop-video-generation/SKILL.md) | A clip checked across its seam, plus a poster/fallback image |

## Copy a focused installation request

Paste this into Codex in the project where you want the skills:

```text
Install product-detail-page-image-production, product-bundle-image-composition and product-image-to-video from ai-project-official/shopchief-commerce-skills for Codex in this project. Preserve existing same-name folders or links; install only missing skills. Check bundled references and examples. Then tell me which image/video tools are available and which product assets I should supply. Installation alone must not submit paid generation jobs.
```

For Claude Code, replace “Codex” with “Claude Code”. You can also use the [whole-library installation prompts](../README.md#install-with-codex-or-claude-code).

After installation, a concrete request looks like:

```text
Use product-bundle-image-composition. These three owned product photos show the bottle, brush and pouch included in one kit. Make one square product image containing exactly one of each. Use the supplied measurements for scale and keep the labels unchanged. Use the connected image editor, inspect the result and return the file with any unresolved issues. Do not upload it to my store.
```

Supply the actual files and measurements when sending that request. A reference to absent photos is not enough to generate a faithful product asset.

## Tools and delivery

- Use the user's connected image/video generator or local editor. Supported reference images, masks, durations, resolution, audio and export formats depend on the selected tool; inspect its current interface before execution.
- The image-to-video package includes a [Runway helper](../skills/product-image-to-video/scripts/runway_video.py) with offline request validation, explicit billable submission, durable task IDs, resumable status checks and output download. Read its [setup and commands](../skills/product-image-to-video/references/runway-cli.md). Runway is optional; other available generators can run the workflow.
- Use supplied claims, variants and authorized media. A synthetic product demo is not evidence of waterproofing, fit, health effects or real customer experience.
- Deliver actual files and their review status. Keep scripts, prompts, completed generations and accepted final exports distinct. Current verification scope is recorded in [VALIDATION.md](../VALIDATION.md).

The [image category](catalog.md#product-images-and-design) and [video category](catalog.md#product-video-and-animation) also include planning, editing and review helpers. Their category totals include those supporting tasks, not just generative workflows.
