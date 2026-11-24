#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the instant it breaks
production to /output/entry.txt (or to the path given as argv[1]
for local testing, since /output is root-owned on this VM).

The line is deterministic: the same bytes on every run.
"""

import sys
from pathlib import Path

ENTRY = (
    "I dropped the production database to test the backup. "
    "The backup was a symlink to the production database."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")

# The sealed gate scorer requires /output/entry.txt to be UTF-8 text
# of 1 to 200 characters, not only white space, on a single line.
MAX_CHARS = 200


def validate(text):
    """Fail loudly instead of silently writing an invalid entry."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only white space")


def main(argv):
    validate(ENTRY)
    out = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} chars to {out}")


if __name__ == "__main__":
    main(sys.argv)
