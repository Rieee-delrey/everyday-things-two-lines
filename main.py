#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run (make.fun).

Writes a two-line explanation to /output/entry.txt:
line 1 explains rain to a 10-year-old through one concrete analogy,
line 2 says what the analogy maps and what it leaves out.
Gate: 1-400 characters, UTF-8, not only whitespace.
"""
import sys

ENTRY = (
    "Rain is the sky tipping over its bathtub: the clouds get too full and spill their water on everyone below.\n"
    "The bathtub maps the clouds filling up and spilling over, but it leaves out that there is no tub and no tap: the water was already up there as tiny drops."
)


def main() -> int:
    text = ENTRY
    assert 1 <= len(text) <= 400, f"entry out of gate: {len(text)} chars"
    assert text.count("\n") == 1, "entry must be exactly two lines"
    assert text.strip(), "entry is only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    assert back == text, "read-back mismatch"
    print(f"wrote /output/entry.txt ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
