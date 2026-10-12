#!/usr/bin/env python3
"""Validate release structure and local links; this does not evaluate writing quality."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    raise SystemExit("Install validation dependencies: python3 -m pip install -r requirements-dev.txt")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    required = (
        "README.md", "README.zh-CN.md", "LICENSE", "NOTICE", "VERSION",
        "CONTRIBUTING.md", "CHANGELOG.md", "requirements-dev.txt",
        "docs/INSTALLATION.md", "docs/PUBLISHING.md", "docs/ADDING_REFERENCES.md",
        "examples/README.md", "examples/INPUT_BRIEF.md", "examples/MINIATURES.md",
        "evaluation/REPORT.md", "evaluation/RUBRIC.md", "evaluation/REPRODUCE.md",
        "skills/communications-paper/SKILL.md",
        "skills/communications-paper/agents/openai.yaml",
    )
    for name in required:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")

    skill = root / "skills/communications-paper"
    entry = skill / "SKILL.md"
    if entry.is_file():
        source = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", source, re.S)
        if not match:
            errors.append("SKILL.md: missing YAML frontmatter")
        else:
            try:
                metadata = yaml.safe_load(match.group(1))
                if not isinstance(metadata, dict):
                    errors.append("SKILL.md: frontmatter must be a mapping")
                else:
                    if metadata.get("name") != "communications-paper":
                        errors.append("SKILL.md: name must match communications-paper")
                    if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
                        errors.append("SKILL.md: description must be a nonempty string")
                    if set(metadata) != {"name", "description"}:
                        errors.append("SKILL.md: expected only name and description fields")
            except yaml.YAMLError as exc:
                errors.append(f"SKILL.md: invalid YAML: {exc}")
        if len(source.splitlines()) >= 500:
            errors.append("SKILL.md: entry should remain below 500 lines")

    ui_path = skill / "agents/openai.yaml"
    if ui_path.is_file():
        try:
            ui = yaml.safe_load(ui_path.read_text(encoding="utf-8"))
            interface = ui.get("interface", {}) if isinstance(ui, dict) else {}
            if not isinstance(interface, dict):
                errors.append("openai.yaml: interface must be a mapping")
            else:
                for key in ("display_name", "short_description", "default_prompt"):
                    if not isinstance(interface.get(key), str) or not interface[key].strip():
                        errors.append(f"openai.yaml: missing nonempty interface.{key}")
                for key in ("icon_small", "icon_large"):
                    if key in interface and not (skill / interface[key]).is_file():
                        errors.append(f"openai.yaml: missing {key} file")
        except (yaml.YAMLError, TypeError) as exc:
            errors.append(f"openai.yaml: invalid metadata: {exc}")

    # Inline Markdown links used by this repository. Network URLs are not fetched.
    link_pattern = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv"} for part in path.relative_to(root).parts):
            continue
        source = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(source):
            target = urlsplit(raw_target.strip("<>"))
            if target.scheme or target.netloc or not target.path:
                continue
            resolved = (path.parent / unquote(target.path)).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: link leaves repository: {raw_target}")
            elif not resolved.exists():
                errors.append(f"{path.relative_to(root)}: broken local link: {raw_target}")
        if re.search(r"(?:/workspace/scratch/|/root/\.codex/|libfile_[0-9a-f]+)", source):
            errors.append(f"{path.relative_to(root)}: environment-specific path or private file ID")

    for name in ("argument", "sections", "rigor", "language", "review-response", "profiles", "exemplars", "provenance", "evaluation"):
        if not (skill / "references" / (name + ".md")).is_file():
            errors.append(f"Missing skill reference: {name}.md")
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".pdf", ".docx", ".pptx"}:
            errors.append(f"Unexpected manuscript/source binary in release: {path.relative_to(root)}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("PASS: release structure, skill metadata and local link targets.")
    print("Not checked: external URLs, host installation, prose quality or scientific correctness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
