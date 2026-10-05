#!/usr/bin/env python3
"""Build the task directory from entrypoints, using only the standard library."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CATEGORY_COPY = {
    "Research and positioning": ("研究与定位", "Product opportunities, competitors, customer research and positioning", "选品机会、竞品分析、顾客研究与品牌定位"),
    "Storefront and conversion": ("店铺与转化", "Shopify storefronts, product pages, checkout and catalog quality", "Shopify 建站、商品页、结账流程与商品目录质量"),
    "Search visibility and product feeds": ("SEO、GEO 与商品 Feed", "SEO audits, AI search visibility, structured data and shopping feeds", "SEO 审查、AI 搜索可见性、结构化数据与购物 Feed"),
    "Content and creative": ("内容与创意", "Product copy, brand voice, campaign content and merchant documents", "商品文案、品牌表达、营销内容与商家文档"),
    "Product images and design": ("商品生图与视觉设计", "Product-page images, lifestyle scenes, bundles, campaign visuals and image localization", "详情页图组、场景图、套装图、促销物料、广告图与图片本地化"),
    "Product video and animation": ("商品视频与动画", "Image-to-video, demos, UGC-style clips, ad variants, localization and seamless loops", "图生视频、商品演示、UGC 风格短片、广告变体、多语言与循环视频"),
    "Advertising and partnerships": ("广告与合作", "Ad planning, budget pacing, creators and affiliate programs", "广告规划、预算进度、达人合作与联盟营销"),
    "Email and retention": ("邮件与客户留存", "Welcome flows, cart recovery, SMS, loyalty and repeat purchases", "欢迎邮件、弃购挽回、短信、会员与复购"),
    "Measurement and unit economics": ("经营分析与利润", "Profit, ROAS, attribution, pricing and financial reconciliation", "利润、ROAS、归因、定价与财务对账"),
    "Inventory fulfillment and support": ("库存、履约与客服", "Replenishment, purchasing, shipping, returns and customer support", "补货、采购、物流、退换货与客户服务"),
}


def readme_overview(groups, chinese=False):
    total = sum(len(members) for members in groups.values())
    lines = ["<!-- skill-overview:start -->",
             "## 技能分类与数量" if chinese else "## Skills by category", "",
             f"**共 {total} 个技能，分为 {len(groups)} 类。** 每个技能包只计一次，中文说明和参考文件不重复计数。" if chinese else
             f"**{total} skills across {len(groups)} categories.** Each skill package is counted once; translations and reference files are not additional skills.", "",
             "| 分类 | 数量 | 典型任务 |" if chinese else "| Category | Skills | Typical tasks |",
             "|---|---:|---|"]
    for group, members in groups.items():
        title_zh, tasks_en, tasks_zh = CATEGORY_COPY[group]
        anchor = re.sub(r"[^a-z0-9 -]", "", group.lower()).replace(" ", "-")
        title, tasks = (title_zh, tasks_zh) if chinese else (group, tasks_en)
        lines.append(f"| [{title}](docs/catalog.md#{anchor}) | {len(members)} | {tasks} |")
    lines.extend([f"| **{'合计' if chinese else 'Total'}** | **{total}** | |",
                  "<!-- skill-overview:end -->"])
    return "\n".join(lines)


def scalar(header, key, indent=0):
    """Read the plain/quoted/folded string fields used by these packages."""
    lines = header.splitlines()
    prefix = " " * indent + key + ":"
    for index, line in enumerate(lines):
        if not line.startswith(prefix):
            continue
        value = line[len(prefix):].strip()
        continuation = []
        for following in lines[index + 1:]:
            if following and len(following) - len(following.lstrip()) <= indent:
                break
            continuation.append(following.strip())
        if value in (">", ">-", "|", "|-"):
            value = " ".join(continuation)
        elif continuation:
            value += " " + " ".join(continuation)
        if value.startswith('"'):
            value = json.loads(value)
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        return " ".join(value.split())
    raise ValueError(f"Missing frontmatter field: {key}")


def generate():
    groups = json.loads((ROOT / "scripts/catalog-groups.json").read_text())
    names = [name for group in groups.values() for name in group]
    folders = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if len(names) != len(set(names)) or set(names) != folders:
        raise ValueError(f"Group coverage mismatch: missing={sorted(folders-set(names))}, absent={sorted(set(names)-folders)}")
    catalog = []
    for group, members in groups.items():
        for name in members:
            entry = (ROOT / "skills" / name / "SKILL.md").read_text()
            header = entry.split("---", 2)[1]
            if scalar(header, "name") != name:
                raise ValueError(f"Folder/name mismatch: {name}")
            catalog.append({"name": name, "description": scalar(header, "description"),
                            "license": scalar(header, "license"),
                            "version": scalar(header, "version", 2), "category": group})
    by_name = {entry["name"]: entry for entry in catalog}
    lines = ["# Skill catalog", "", "Choose a merchant task, then install just the skills you need. Each package includes its own license and references. Tool access and merchant evidence determine which steps can run.", "", "```sh", "npx skills add ai-project-official/shopchief-commerce-skills --skill <skill-name>", "```", ""]
    for group in groups:
        anchor = re.sub(r"[^a-z0-9 -]", "", group.lower()).replace(" ", "-")
        lines.append(f"- [{group}](#{anchor})")
    for group, members in groups.items():
        lines.extend(["", f"## {group}", "", "| Skill | Use it for | Example |", "|---|---|---|"])
        for name in members:
            entry = by_name[name]
            example = next((path for path in ["assets/worked-example.md", "assets/worked-review.md"] if (ROOT / "skills" / name / path).exists()), None)
            sample = f"[Worked example](../skills/{name}/{example})" if example else "See skill instructions"
            description = entry["description"].replace("|", "\\|")
            lines.append(f"| [{name}](../skills/{name}/SKILL.md) | {description} | {sample} |")
    outputs = {ROOT / "catalog.json": json.dumps(sorted(catalog, key=lambda e: e["name"]), ensure_ascii=False, indent=2) + "\n",
               ROOT / "docs/catalog.md": "\n".join(lines) + "\n"}
    for filename, chinese in (("README.md", False), ("README.zh-CN.md", True)):
        readme = ROOT / filename
        content, replacements = re.subn(
            r"<!-- skill-overview:start -->.*?<!-- skill-overview:end -->",
            lambda _: readme_overview(groups, chinese), readme.read_text(), flags=re.S,
        )
        if replacements != 1:
            raise ValueError(f"{filename}: expected one skill overview block")
        outputs[readme] = content
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for path, content in generate().items():
        if args.check:
            if not path.exists() or path.read_text() != content:
                raise SystemExit(f"Outdated generated catalog: {path.name}; run python3 scripts/build_catalog.py")
        else:
            path.write_text(content)
    print("PASS: task groups and generated catalog agree")


if __name__ == "__main__":
    main()
