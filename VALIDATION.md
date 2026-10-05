# Release validation

Media expansion, 2026-10-05, v0.4.0. [Previous release record](docs/validation-v0.3.0.md).

## Scope

The update adds six original image-production packages and six original video-production packages, each with English/Chinese instructions, a synthetic worked example, production references and a bundled MIT license. The existing image prompt guide now resolves the current tool's interface instead of assuming one tool name, fixed resolution or upload mechanism.

The library has 360 distinct packages in ten categories. Product images/design has 14 packages and product video/animation has 13; both include planning and review helpers as well as production workflows. The remaining content category has 58 packages. Renaming a category does not add a skill.

## Executable video helper

The optional Python-standard-library Runway helper in `product-image-to-video` provides offline request validation, one explicit billable submission, a durable receipt, resumable status lookup and output download. Its request/task/output contract was checked against the official documentation on 2026-10-05. Model access and current supported parameters still require a check at execution time.

Ten offline lifecycle scenarios passed using simulated provider responses: dry run without a request; receipt persistence; duplicate-submission prevention; status lookup using the same task ID; truncated download rejection; partial cleanup after timeout; exact-byte download on retry; existing-file preservation; unknown-submission receipt preservation; and rejection of an HTTP output redirect. These simulations do not establish real provider acceptance or video quality.

## Validation boundary

The full catalog and package validator passed for 360 skills. All twelve new entrypoints passed the skill-creator format validator. The twelve packages were installed from the local release source into fresh Codex and Claude Code project directories using skills CLI 1.7.0; each client's 62 package files matched source bytes, with no symlinks. The npm dependency audit reported zero vulnerabilities; no runtime npm dependency was added.

[Two independent fresh-input cases](examples/release-v0.4/README.md) checked exact bundle membership/scale and a changed-price, changed-duration German video. Both produced concrete specifications without inventing source inspection, generated files or measured audio. A video-localization clarification was added from the review. These are selected offline checks, not a benchmark across the library.

Package validation checks catalog coverage, entrypoint names, bundled licenses, relative links, attribution parameters and limited secret patterns. Worked examples are synthetic production specifications, not fabricated merchant results or claims that media has been generated.

No paid generation jobs, live store writes, advertising publication or actual voice cloning are part of this release acceptance. Image fidelity, video coherence, audio synchronization and playback must be inspected on real generated outputs before delivery. The library includes workflows and an optional provider adapter; it does not include provider accounts or credits.

## Reproduce package checks

```sh
python3 scripts/build_catalog.py --check
python3 scripts/validate.py
python3 skills/product-image-to-video/scripts/runway_video.py --help
npm audit --omit=dev
```

Use the [media guide](docs/media-production.md) for task selection and the installed package's worked example for a complete input/prompt/timeline specification. Run the helper's `submit` command without `--execute` for offline payload checks. Executing billable generation requires the user's authorized scope and provider setup.
