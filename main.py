#!/usr/bin/env python3
"""Midnight Fridge Roast — writes one roast line to /output/entry.txt.

The roast: a smart fridge that refuses to open after midnight, told as a
legal gag — the fridge took out a restraining order against its owner's
hunger. One joke, one line, spoken like a person standing at the kitchen
door at midnight.
"""

import hashlib
from pathlib import Path

ENTRY = "At midnight my fridge took out a restraining order against my hunger."

GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 200


def validate(text: str) -> str:
    """Enforce the gate: 1-200 chars, UTF-8, not only white space."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be only white space")
    if not GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS:
        raise ValueError(
            f"entry must be {GATE_MIN_CHARS}-{GATE_MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"wrote {out} ({len(text)} chars, sha256 {digest})")


if __name__ == "__main__":
    main()
