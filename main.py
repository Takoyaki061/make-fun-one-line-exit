#!/usr/bin/env python3
"""Write one one-line resignation letter for the make.fun bounty
"The One-Line Exit" (u-kreutzx-the-one-line-exit-1dc652d1).

Writes the letter to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Standard library only.
"""
import os

LINE = (
    "The animals and I have agreed to a mutual separation\u2014"
    "they keep the enclosure, I keep my dignity, "
    "and the penguins keep the keys."
)


def main() -> None:
    # Self-check against the gate before writing: one line, 1-140 chars.
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, gate is 1-140"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
