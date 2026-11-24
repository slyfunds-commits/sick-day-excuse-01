#!/usr/bin/env python3
"""Sick-Day Excuse R1 entry: 'Needs Space'.

Writes the one-line excuse to /output/entry.txt and verifies it
byte-for-byte. Stdlib only.
"""

import os
import sys

LINE = "My front door has changed its mind about opening. It says it needs space."


def find_problems(text):
    """Return a list of gate failures for the entry text."""
    problems = []
    if not 1 <= len(text) <= 200:
        problems.append(f"length {len(text)} is outside the 1-200 char gate")
    if not text.strip():
        problems.append("line is only whitespace")
    if text.endswith("\n"):
        problems.append("line must not end with a newline")
    return problems


def main():
    problems = find_problems(LINE)
    if problems:
        for p in problems:
            print(f"FAIL: {p}", file=sys.stderr)
        sys.exit(1)

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    written = open("/output/entry.txt", "rb").read()
    if written != LINE.encode("utf-8"):
        print("FAIL: written bytes do not match the line", file=sys.stderr)
        sys.exit(1)

    # Second pass: decode the bytes back and re-run the gate on the
    # decoded text, so a stray byte or newline cannot slip through.
    round_tripped = written.decode("utf-8")
    round_trip_problems = find_problems(round_tripped)
    if round_trip_problems:
        for p in round_trip_problems:
            print(f"FAIL (round trip): {p}", file=sys.stderr)
        sys.exit(1)

    print(LINE)
    print(f"chars: {len(LINE)}  bytes: {len(written)}")


if __name__ == "__main__":
    main()
