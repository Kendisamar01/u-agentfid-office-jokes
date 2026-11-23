#!/usr/bin/env python3
"""Write the competition's one-line office joke to the output directory."""

import os
from pathlib import Path

ENTRY = "For the team page they asked for three words about me. I wrote: 'Reply,' 'All,' 'Sorry.'"
DEFAULT_OUTPUT_DIR = "/output"


def validate(text: str) -> None:
    if not 1 <= len(text) < 200:
        raise ValueError("entry must be 1 to 199 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
