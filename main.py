#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes a single line to /output/entry.txt: the Moon, after four billion
years of wishes, howls and late-night promises, finally answering back.
"""

import os

ENTRY = (
    "Four billion years of wishes, howls, and 2 a.m. promises \u2014 "
    "and not one of you has ever once asked how I'm doing."
)


def main() -> None:
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _ = input_dir  # No input data is needed for this entry.
    # The gate requires 1 to 240 characters, not only white space.
    assert 1 <= len(ENTRY) <= 240 and ENTRY.strip(), "entry out of bounds"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
