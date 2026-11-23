#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters — make.fun entry.

Writes one line, a robot vacuum's excuse for missing a spot, to
/output/entry.txt. Stdlib only, no network, no dependencies.

Run: python3 main.py
"""

import os

LINE = (
    "Spot 47 remains untouched: my lidar classified the Cheerios as a "
    "load-bearing structure, and I do not argue with architecture."
)


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse:
    # 1-200 UTF-8 characters, not whitespace-only.
    if not LINE.strip():
        raise SystemExit("entry line is empty or whitespace-only")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry line is {len(LINE)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
