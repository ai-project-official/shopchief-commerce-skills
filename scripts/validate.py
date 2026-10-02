#!/usr/bin/env python3
"""Offline package consistency checks. Does not execute skill instructions."""
import json
import re
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from build_catalog import generate, scalar

ROOT = Path(__file__).resolve().parents[1]

def main():
    errors = []
    catalog = json.loads((ROOT / "catalog.json").read_text())
    try:
        for path, content in generate().items():
            if not path.exists() or path.read_text() != content:
                errors.append(f"{path.name}: generated catalog is outdated")
    except (ValueError, IndexError, FileNotFoundError) as error:
        errors.append(f"Catalog generation: {error}")
    folders = sorted((ROOT / "skills").iterdir())
    expected = {entry["name"] for entry in catalog}
    actual = {p.name for p in folders if p.is_dir()}
    if expected != actual or len(expected) != len(catalog):
        errors.append("Catalog and skill folders differ, or names are duplicated")
    for folder in folders:
        if not folder.is_dir():
            continue
        if not (folder / "LICENSE").exists():
            errors.append(f"{folder.name}: missing bundled license")
        entry = folder / "SKILL.md"
        if not entry.exists():
            errors.append(f"{folder.name}: missing SKILL.md")
            continue
        text = entry.read_text()
        pieces = text.split("---", 2)
        if not text.startswith("---\n") or len(pieces) != 3:
            errors.append(f"{folder.name}: invalid frontmatter framing")
            continue
        names = re.findall(r"^name:\s*(.+)$", pieces[1], re.M)
        if names != [folder.name] or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", folder.name) or len(folder.name) > 64:
            errors.append(f"{folder.name}: invalid skill name")
        if not re.search(r"^description:\s*\S", pieces[1], re.M):
            errors.append(f"{folder.name}: missing description")
        desc = next((x["description"] for x in catalog if x["name"] == folder.name), "")
        if not desc or len(desc) > 1024:
            errors.append(f"{folder.name}: invalid description length")
        try:
            if scalar(pieces[1], "description") != desc:
                errors.append(f"{folder.name}: entrypoint and catalog descriptions differ")
            version = scalar(pieces[1], "version", 2)
            if not re.fullmatch(r"\d+\.\d+\.\d+", version):
                errors.append(f"{folder.name}: invalid package version")
            elif tuple(map(int, version.split("."))) >= (0, 2, 0):
                example = folder / "assets/worked-example.md"
                if not example.is_file() or "assets/worked-example.md" not in text:
                    errors.append(f"{folder.name}: new package must link its bundled worked example")
            if version == "0.3.0":
                source = folder / "references/source.md"
                if not source.is_file() or "references/source.md" not in text:
                    errors.append(f"{folder.name}: adaptation must link its bundled source record")
                else:
                    attribution = source.read_text()
                    if not re.search(r"https://github\.com/[^/\s]+/[^/\s]+/blob/[a-f0-9]{40}/", attribution):
                        errors.append(f"{folder.name}: source record lacks a fixed upstream file revision")
                    if not re.search(r"\b[a-f0-9]{64}\b", attribution):
                        errors.append(f"{folder.name}: source record lacks an upstream SHA-256")
        except (ValueError, IndexError) as error:
            errors.append(f"{folder.name}: {error}")
    for entry in ROOT.glob("skills/*/SKILL*.md"):
        links = re.findall(r"https://shopchief\.ai/[^\s)]+", entry.read_text())
        if not links:
            errors.append(f"{entry.relative_to(ROOT)}: missing ShopChief source link")
        for link in links:
            query = parse_qs(urlparse(link).query)
            if query.get("utm_source") != [entry.parent.name] or query.get("utm_medium") != ["agent_skill"] or query.get("utm_campaign") != ["commerce_skills"] or not query.get("utm_content"):
                errors.append(f"{entry.relative_to(ROOT)}: invalid skill attribution link")
    secret_patterns = [r"gh[pousr]_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}", r"sk_(?:live|test)_[A-Za-z0-9]{16,}", r"AKIA[A-Z0-9]{16}", r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", r"mongodb(?:\+srv)?://[^\s/]+:[^\s/]+@"]
    checked = 0
    for path in ROOT.rglob("*"):
        if path.is_symlink() and "skills" == path.relative_to(ROOT).parts[0]:
            errors.append(f"{path.relative_to(ROOT)}: installed packages must not depend on symlinks")
            continue
        if not path.is_file() or any(part in {".git", "node_modules", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix not in {".md", ".json", ".csv", ".py", ".yml", ".yaml", ".txt", ".html", ".js", ".ts"} and path.name not in {"LICENSE", "NOTICE"} and "licenses" not in path.parts:
            continue
        text = path.read_text()
        checked += 1
        if path.name != "validate.py" and any(re.search(pattern, text) for pattern in secret_patterns):
            errors.append(f"{path.relative_to(ROOT)}: possible secret")
        if path.name != "validate.py" and ("/Users/" in text or "/.accio/accounts/" in text):
            errors.append(f"{path.relative_to(ROOT)}: local machine path")
        if path.suffix == ".md":
            # Ignore code fences: example Markdown snippets are not package links.
            prose = re.sub(r"```.*?```", "", text, flags=re.S)
            for match in re.finditer(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)", prose):
                target = match.group(1).split(' "', 1)[0].strip("<>")
                if re.match(r"(?:[a-z]+:|#|\{|<)", target, re.I):
                    continue
                rel = target.split("#", 1)[0]
                if not rel:
                    continue
                resolved = (path.parent / rel).resolve()
                boundary = ROOT / "skills" / path.relative_to(ROOT).parts[1] if path.relative_to(ROOT).parts[0] == "skills" else ROOT
                if not resolved.is_relative_to(boundary) or not resolved.exists():
                    errors.append(f"{path.relative_to(ROOT)}: broken/escaping reference {target}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(actual)} skills; {checked} files; catalog, bundled licenses, relative links and secret-pattern checks")

if __name__ == "__main__":
    main()
