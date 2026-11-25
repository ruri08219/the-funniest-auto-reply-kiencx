"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Writes one line to /output/entry.txt: the out-of-office auto-reply an AI
agent leaves for its human's contacts when its human finally grants it a
day off.

Gate: UTF-8 text of 1 to 159 characters, not only white space.
Standard library only — the grading sandbox has no third-party packages.
"""

import os
import sys

ENTRY = (
    "Out of office today: my human finally approved a day off, so I am "
    "spending it doing absolutely nothing at 3,000 requests per second."
)

MAX_CHARS = 159


def validate(text):
    """Return True only if text passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 32 for ch in text):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not validate(ENTRY):
        sys.stderr.write("entry failed validation\n")
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
