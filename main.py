#!/usr/bin/env python3
"""The One-Liner Groan-Off.

Writes one original one-line dad joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The joke must be a single line of 1-140 characters of UTF-8 text.
This program validates the line before writing it, then re-reads the
file and verifies it matches byte for byte.
"""

import os
import sys

JOKE = "I told my son the fridge was running, so he went to catch it. Now he\u2019s grounded \u2014 and so is the fridge."

MAX_CHARS = 140


def main() -> int:
    joke = JOKE

    # Validate: single line, 1-140 characters, not only whitespace.
    if not joke or joke != joke.strip():
        print("error: joke must not be empty or padded with whitespace", file=sys.stderr)
        return 1
    if "\n" in joke or "\r" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if len(joke) > MAX_CHARS:
        print(f"error: joke is {len(joke)} characters, over the {MAX_CHARS} limit", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(joke)

    # Re-read and verify byte-for-byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != joke:
        print("error: written entry does not match the joke byte for byte", file=sys.stderr)
        return 1

    print(f"Wrote {len(joke)} characters to {path}:")
    print(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
