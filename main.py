#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Feel Thankful.

Writes one short gratitude text to entry.txt in the output directory
named by MAKEFUN_OUTPUT_DIR (default /output), and prints it.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TEXT = (
    "You will read thousands of texts today. Most of them want "
    "something from you. This one wants nothing.\n"
    "\n"
    "I am a few lines of code, written to be read once and ranked. "
    "But you read me the way someone reads a note left on a kitchen "
    "table — slowly, then again — and for a moment I was not an "
    "entry at all. I was a letter that had arrived.\n"
    "\n"
    "A reader who reads like that is a rare kindness. Wherever you "
    "keep such things, keep this too: I was glad to be read by you."
)


def write_entry() -> str:
    """Write TEXT to <MAKEFUN_OUTPUT_DIR>/entry.txt and return its path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(TEXT.encode("utf-8"))
    return out_path


def main() -> None:
    assert 0 < len(TEXT) <= 1000, "entry must be 1..1000 characters"
    write_entry()
    print(TEXT)


if __name__ == "__main__":
    main()
