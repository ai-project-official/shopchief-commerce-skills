#!/usr/bin/env python3
"""Build the task directory from entrypoints, using only the standard library."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


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
    return {ROOT / "catalog.json": json.dumps(sorted(catalog, key=lambda e: e["name"]), ensure_ascii=False, indent=2) + "\n",
            ROOT / "docs/catalog.md": "\n".join(lines) + "\n"}


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
