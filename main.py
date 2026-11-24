#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — round 1 entry.

Writes the final line to /output/entry.txt.
Pure standard library; deterministic.
"""

import os
import sys

LINE = "My front door has changed its mind about opening. It says it needs space."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def check_problems(text):
    problems = []
    if not (1 <= len(text) <= 200):
        problems.append(f"length {len(text)} outside 1-200 chars")
    if not text.strip():
        problems.append("text is only whitespace")
    if text.endswith("\n"):
        problems.append("trailing newline")
    return problems


def main():
    problems = check_problems(LINE)
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    with open(OUT_PATH, "rb") as handle:
        written = handle.read()
    if written != LINE.encode("utf-8"):
        print("byte mismatch after write", file=sys.stderr)
        return 1
    decoded = written.decode("utf-8")
    problems = check_problems(decoded)
    if problems:
        for problem in problems:
            print(f"written entry invalid: {problem}", file=sys.stderr)
        return 1
    print(decoded)
    print(f"chars={len(LINE)} bytes={len(written)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
