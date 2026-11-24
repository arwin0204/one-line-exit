#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes a single funny resignation letter (one line, <= 140 characters)
to /output/entry.txt. Deterministic: the same text on every run.
No network, no dependencies, Python 3.13 standard library only.
"""

import os

ENTRY = (
    "I resign: after four years fixing everyone's computers, "
    "I've decided to turn myself off and on again — permanently."
)

MAX_CHARS = 140


def validate_entry(text: str) -> str:
    """Check the entry fits the gate: 1-140 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    return text


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    """Write the validated entry text to the output file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    write_entry(validate_entry(ENTRY))


if __name__ == "__main__":
    main()
