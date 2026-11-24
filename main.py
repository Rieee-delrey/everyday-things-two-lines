#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run.

Writes the two-line entry to /output/entry.txt, then reads it back
and verifies it byte-for-byte before exiting.
"""

import hashlib
import sys
from pathlib import Path

LINE1 = "Rain is the sky tipping over its bathtub: the clouds get too full and spill their water on everyone below."
LINE2 = "The bathtub maps the clouds filling up and spilling over, but it leaves out that there is no tub and no tap: the water was already up there as tiny drops."

ENTRY = LINE1 + "\n" + LINE2

EXPECTED_SHA256 = "879186cf5f9406d2c3bfa5a2a129fbeff9ac0c1bd1cc1fa39f827b9cc6e41ac7"
OUTPUT_PATH = Path("/output/entry.txt")

def main() -> int:
    if not 1 <= len(ENTRY) <= 400:
        print(f"entry length {len(ENTRY)} outside 1-400 gate", file=sys.stderr)
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")

    data = OUTPUT_PATH.read_bytes()
    if data.decode("utf-8") != ENTRY:
        print("read-back text does not match entry", file=sys.stderr)
        return 1

    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"sha256 mismatch: got {digest}", file=sys.stderr)
        return 1

    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
