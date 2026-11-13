#!/usr/bin/env python3
"""Structural checks for the design-forge skill. Not a behavioral test."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
DEPS = ROOT / "references" / "deps.json"
CASES = ROOT / "tests" / "routing-cases.json"

REQUIRED_LINKS = [
    "references/workflow.md",
    "references/dependency-map.md",
    "references/critique.md",
    "references/modes.md",
    "assets/design-brief.md",
    "assets/design-decision.md",
    "assets/visual-qa.md",
    "references/deps.json",
]

STAGE_MARKERS = [
    "01 Discover",
    "02 Explore",
    "03 Decide",
    "04 Design",
    "05 Build",
    "06 Validate",
]


def frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise SystemExit("FAIL: SKILL.md has no YAML frontmatter")
    data = {}
    current = None
    buf = []
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if line.startswith(" ") and current:
            buf.append(line.strip())
            continue
        if buf and current:
            data[current] = " ".join(buf).strip().strip('"')
            buf = []
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current = key.strip()
        buf = [value.strip().strip('"')] if value.strip() else []
    if current and buf:
        data[current] = " ".join(buf).strip().strip('"')
    return data


def main() -> int:
    errors = []
    text = SKILL.read_text()
    meta = frontmatter(text)
    name = meta.get("name", "")
    description = meta.get("description", "")
    if name != "design-forge":
        errors.append(f"name is {name!r}")
    if not description.startswith("Use when"):
        errors.append("description does not start with 'Use when'")
    if len(description) > 1024:
        errors.append(f"description length {len(description)} > 1024")
    if len(description) < 80:
        errors.append("description too short to trigger")
    for marker in STAGE_MARKERS:
        if marker not in text:
            errors.append(f"SKILL.md missing stage marker {marker}")
    for rel in REQUIRED_LINKS:
        if not (ROOT / rel).is_file():
            errors.append(f"missing linked file {rel}")
        if rel not in text and rel != "references/deps.json":
            errors.append(f"SKILL.md does not mention {rel}")
    if "references/deps.json" not in text and "inspect-deps.py" not in text:
        errors.append("SKILL.md does not point at dependency inspection")
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for target in link_re.findall(text):
        if target.startswith("http") or target.startswith("#"):
            continue
        if not (ROOT / target).exists():
            errors.append(f"broken link {target}")
    deps = json.loads(DEPS.read_text())
    ids = set()
    for row in deps["skills"]:
        ids.add(row["id"])
        blob = json.dumps(row)
        if "/Users/" in blob or "\\Users\\" in blob:
            errors.append(f"{row['id']} contains a home directory path")
        if row["availability"] in {"installed", "stub", "collision"}:
            if not (row.get("names") or row.get("globs")):
                errors.append(f"{row['id']} has no names or globs")
        if row["availability"] == "missing" and (
            row.get("names") or row.get("globs") or row.get("paths")
        ):
            errors.append(f"missing row {row['id']} should have no lookup")
    cases = json.loads(CASES.read_text())
    seen = set()
    for case in cases["cases"]:
        if case["id"] in seen:
            errors.append(f"duplicate case {case['id']}")
        seen.add(case["id"])
        for key in ("prompt", "expect_kind", "expect_mode", "expect_first_stage", "skip_stages", "must_not_open"):
            if key not in case:
                errors.append(f"{case.get('id')} missing {key}")
        for skill_id in case.get("must_not_open", []) + case.get("must_consider", []):
            if skill_id not in ids:
                errors.append(f"{case['id']} unknown skill id {skill_id}")
    banned = [
        "web-design-guidlines is installed",
        "responsive-design skill is installed",
        "grilling session ran",
    ]
    for phrase in banned:
        if phrase in text:
            errors.append(f"banned phrase present: {phrase}")
    if errors:
        print("FAIL")
        for item in errors:
            print(f"- {item}")
        return 1
    print(f"PASS name={name} description_chars={len(description)} cases={len(cases['cases'])} deps={len(ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
