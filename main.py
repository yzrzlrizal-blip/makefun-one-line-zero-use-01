#!/usr/bin/env python3
"""Write one original line describing a hilariously useless superpower.

Deterministic, standard library only, no file reads, no network.
Writes exactly one line (no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

LINE = "I can stop time with a single thought \u2014 unfortunately, the thought only ever comes to me while I'm already late."


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
