# Image tools and delivery

Inspect the user's actual product images and record which reference belongs to each SKU. Use an image tool installed in the current host. Read its schema before calling it: input reference types, number of outputs, supported dimensions, aspect ratios and edit controls differ by provider. Do not invent arguments or treat prompt-planning labels as API parameters.

Within ShopChief an optional `image_generate` adapter exists; it is not bundled here. Outside that runtime use the configured provider's documented tool. If generation is unavailable, deliver prompts and a shot list, clearly marking images as pending. Never claim an image was generated from a prompt alone.

Preserve product geometry, material, color, labels and other verified facts. Use the requested supported dimensions; disclose any crop or outpainting that changes the composition. Inspect returned images against the request before reporting fidelity. Do not silently replace merchant product photography with a generated approximation.

For a batch, map every input and requested output to a result or explicit failure. Avoid duplicate paid generations after uncertain errors. Resolve existing results before retrying. Record real artifact paths, source references and usage restrictions. Use a deterministic resize/compression tool for technical transformations when available, rather than redrawing the product.

Write prompts in the language best supported by the selected provider while preserving the meaning of the user's terminology. Explain in the user's requested language; do not translate a product claim into a stronger one.
