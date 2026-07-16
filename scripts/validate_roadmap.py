#!/usr/bin/env python3
"""Validate the strict ROADMAP.txt format required by roadmap-progress."""

from __future__ import annotations

import re
import sys
from pathlib import Path


CONTEXT_RE = re.compile(r"(?:\[[^\]\r\n]+\])+")
TASK_RE = re.compile(r"\|-\[(\d{3})\]\[(SELESAI|PROGRESS|BELUM)\] .+")
BOX_DRAWING = set("━─│┏┓┗┛┣┫┳┻╋")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"File does not exist: {path}"]

    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        errors.append("File must end with a newline.")
    if any(char in text for char in BOX_DRAWING):
        errors.append("Tables and box-drawing characters are not allowed.")

    lines = text.splitlines()
    if not lines:
        return ["File is empty."]
    if not lines[0].strip() or lines[0].startswith(("#", "*", "[", "|-")):
        errors.append("Line 1 must be an unheaded one-paragraph summary.")

    index = 1
    note_count = 0
    while index < len(lines) and lines[index].startswith("*"):
        if lines[index] == "*":
            errors.append(f"Line {index + 1} contains an empty note.")
        note_count += 1
        index += 1
    if note_count == 0:
        errors.append("At least one important note beginning with '*' is required.")

    if index >= len(lines) or lines[index] != "":
        errors.append("A blank line must separate notes from context tags.")
    else:
        index += 1

    if index >= len(lines) or CONTEXT_RE.fullmatch(lines[index]) is None:
        errors.append("Expected exactly one adjacent context-tag line, such as [API][Testing].")
    else:
        index += 1

    ids: list[int] = []
    while index < len(lines):
        match = TASK_RE.fullmatch(lines[index])
        if match is None:
            errors.append(f"Line {index + 1} does not match |-[NNN][STATUS] description.")
        else:
            ids.append(int(match.group(1)))
        index += 1

    if not ids:
        errors.append("At least one task line is required.")
    elif ids != list(range(1, len(ids) + 1)):
        errors.append("Task IDs must be unique and sequential starting at 001.")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_roadmap.py <ROADMAP.txt>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    errors = validate(path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Valid roadmap: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
