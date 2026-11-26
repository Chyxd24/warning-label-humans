#!/usr/bin/env python3
"""Warning label for humans - one line, at most 160 characters.

Writes the entry to /output/entry.txt and verifies the readback.
Authored natively in this session (write_file + patch), stdlib only.
"""
import os

ENTRY = (
    "WARNING: Object in mirror is dumber than it appears. "
    "Do not argue with it - it has a smartphone, no plan, and a podcast."
)
OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(text)} chars: {text}")


if __name__ == "__main__":
    main()
