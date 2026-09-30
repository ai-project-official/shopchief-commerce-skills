# HD Upscale

## Routing Header

- **Load when**: user asks to upscale, sharpen, enhance clarity, restore resolution, or make an existing image clearer without content changes.
- **Do not load when**: user asks only to increase file size, convert format, resize dimensions, crop, or change visual content.
- **Merge notes**: do not treat upscale as a separate paid AI step when the user mainly wants native delivery sizing. If content edits are needed, perform content edits first and upscale only when quality is still insufficient or the user explicitly requested it.
- **Hard stop**: this scene must not remove watermarks, change backgrounds, fix layout, edit text, or alter any image content.

## Scene Description

Enhance the resolution and sharpness of an existing image without modifying its content, composition, colors, or elements.

> **Hard constraint**: This scene only enhances clarity. It does not remove watermarks, change backgrounds, adjust elements, or alter image content in any way.

## Apply Method

Call `image_generate` with the exact source in `input_images` and a required concise prompt:

```text
Enhance clarity and detail only. Preserve content, composition, colors, text, layout, and identity exactly. Do not add, remove, or redesign anything.
```

Use `size="2K"` when the user requests the highest currently supported output tier; otherwise
leave `size="auto"`. `hd_upscale` is a planning label, not a tool argument.

## Content-Type Pre-Check

Before calling `hd_upscale`, the Agent should assess the image content type:

| Content Type | Recommendation |
|-------------|----------------|
| Product photos, natural scenes, portraits | Proceed normally with `hd_upscale` |
| **Text-heavy images** (posters, UI screenshots, infographics, documents) | **Warn the user**: "HD upscale may cause text distortion or garbled characters on text-heavy images. Consider obtaining a higher-resolution source file or using a non-AI upscaling tool instead." |
| **File size requests** ("I need it to be 2MB", "output is too small") | **This is NOT an AI task**. Route to resize tool or quality-parameter adjustment. Increasing file size ≠ increasing visual clarity. |

## Output Size Routing

| User Request | Action |
|--------------|--------|
| "Make clearer / sharpen / restore" | `image_generate` with explicit `input_images` and the preservation prompt above. |
| "Generate at 1K/2K" | Pass the requested value through `size`. |
| "Generate at 4K" | Current route is limited to 2K. Use 2K plus a native upscaler if available; otherwise state the limitation. |

## Notes

- **No content modification**: this scene must not change composition, colors, elements, or background — only resolution and sharpness
- **4K support depends on the runtime**: use native high-resolution generation when available; otherwise use highest supported generation followed by upscale.
