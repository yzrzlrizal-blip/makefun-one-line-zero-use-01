#!/usr/bin/env python3
"""Write one original line describing a hilariously useless superpower.

Deterministic, standard library only, no file reads, no network.
Writes exactly one line (no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

MAX_CHARS = 200

LINE = "I can stop time with a single thought \u2014 unfortunately, the thought only ever comes to me while I'm already late."


def main() -> int:
    if not LINE.strip():
        print("error: entry line is empty", flush=True)
        return 1
    if len(LINE) > MAX_CHARS:
        print(f"error: entry line is {len(LINE)} chars, exceeds MAX_CHARS={MAX_CHARS}", flush=True)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
