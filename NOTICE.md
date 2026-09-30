# Attribution and provenance

## ShopChief production-derived packages

The 34 `shopchief-production` entries in `provenance.json` were exported from the maintainer-authorized current published skill revisions observed on 2026-09-30. The original snapshot remains outside this public repository. This release adapts their runtime assumptions, metadata and provider interfaces; it is not a byte-for-byte production backup.

Copyright (c) 2026 Clivia and ShopChief contributors. Released under the repository MIT license by the maintainer's publication authorization. Referenced third-party documentation and trademarks remain with their respective owners.

## Corey Haines Marketing Skills

The six `licensed-upstream-adaptation` entries in `provenance.json` are DTC-focused adaptations of:

- Repository: https://github.com/coreyhaines31/marketingskills
- Commit: `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`
- Copyright (c) 2025 Corey Haines
- License: MIT; full text in `licenses/coreyhaines31-marketingskills-MIT.txt` and each adapted skill's `LICENSE`.

Upstream `ab-testing`, `content-strategy`, `launch`, `social`, `marketing-psychology` and `marketing-ideas` informed the corresponding DTC packages. They were rewritten for physical-goods merchants; SaaS examples, unverified benchmark tables, unrelated partner links and unbundled dependencies were omitted. The adaptations do not imply upstream endorsement.

## Local candidate audit

The local Accio installation was a discovery input, not a blanket source of licensed content. Its cache field named `oss` is a download URL and is not treated as an open-source license. Unverified local modifications and packages were excluded; the six marketing additions use the licensed upstream directly. No claim is made that similarly named local files are identical to that upstream.
