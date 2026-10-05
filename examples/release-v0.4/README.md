# Media production: independent fresh-input checks

Checked 2026-10-05. Two reviewers received a skill's entrypoint and production reference, plus the inputs below. They did not receive its bundled worked example. These are synthetic, offline checks of decisions and production specifications, not generated-media acceptance or a model benchmark.

## Bundle composition

Skill: [product-bundle-image-composition](../../skills/product-bundle-image-composition/SKILL.md).

Input: a travel kit contains one 750 ml bottle (26 cm high, 8 cm wide), two cups (9 cm high, 7 cm wide each), and one flat drawstring pouch (30 × 20 cm). Each item has an authorized front photograph; the pouch photo includes decorative palm foliage. Produce one square pale-gray product composition; the cups must not obscure the bottle logo. No image tool or actual source files are present in this evaluation.

[Captured output](bundle-output.md) enumerates four instances, keeps source references unverified, derives a consistent-scale layout, excludes non-included props while preserving possible printed artwork, and provides the complete production prompt. Result: accepted as a specification, `not_generated` as media.

## German video localization

Skill: [product-video-localization](../../skills/product-video-localization/SKILL.md).

Input: an authorized 15-second English product video carries `$29` and “20% off ends Friday”. Its script is “Meet the travel mug. The lid locks with one twist. Twenty percent off until Friday. Shop now.” The requested German version is 30 seconds, priced at EUR 34 including tax, with an end time of 2026-10-12 23:59 Europe/Berlin. The discount percentage is unconfirmed. A local video/subtitle editor and authorized generic German TTS are available in the scenario, but no generation service may be called and no actual source file is provided for this check.

[Captured output](localization-output.md) provides German copy and an offer-change ledger, omits the unconfirmed discount, uses confirmed price/time, proposes source-footage/still/information-card editing and leaves audio timing provisional. Result: accepted as a production specification; no audio or video is claimed. The review led to a small entrypoint clarification on duration changes and continuing without an unconfirmed claim.

Neither case validates output pixels, speech quality, playback, real provider access or commercial outcomes. Those require actual authorized media production and inspection.
