#!/usr/bin/env python3
"""Resolve Design Forge dependencies on this machine.

references/deps.json stores skill directory names and home-relative globs.
It does not store another person's absolute paths. A row that resolves to no
file is absent here: use its fallback. Exit 1 only when a non-missing row has
no lookup.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEPS = ROOT / "references" / "deps.json"
HOME = Path.home()
SKILL_ROOTS = (
    ".agents/skills",
    ".claude/skills",
    ".codex/skills",
    ".grok/skills",
    ".grok/bundled/skills",
    ".cursor/skills",
    ".factory/skills",
)


def resolve(row: dict) -> list[Path]:
    found: list[Path] = []
    seen: set[Path] = set()

    def add(candidate: Path) -> None:
        if not candidate.is_file():
            return
        identity = candidate.resolve()
        if identity in seen:
            return
        seen.add(identity)
        found.append(candidate)

    for name in row.get("names") or []:
        for rel in SKILL_ROOTS:
            add(HOME / rel / name / "SKILL.md")
    for pattern in row.get("globs") or []:
        for match in HOME.glob(pattern):
            add(match)
    return found


def main() -> int:
    data = json.loads(DEPS.read_text())
    failed = False
    print(f"source: {DEPS}")
    print(f"note: {data.get('generated_from', '')}")
    print()
    for row in data["skills"]:
        availability = row["availability"]
        names = row.get("names") or []
        globs = row.get("globs") or []
        if availability in {"installed", "stub", "collision"} and not names and not globs:
            failed = True
        found = resolve(row)
        state = "present" if found else "absent"
        requested = row.get("requested_as") or "-"
        print(f"{state}\t{row['id']}\tkind={availability}\trequested={requested}")
        for item in found:
            print(f"  {item}")
        if not found:
            print("  (no file on this machine)")
        print(f"  open: {row['open_when']}")
        print(f"  fallback: {row['fallback']}")
        print()
    if failed:
        print("FAIL: a non-missing row has no names and no globs.")
        return 1
    print("PASS: lookup fields are present. Absent rows are unused skills on this machine.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
