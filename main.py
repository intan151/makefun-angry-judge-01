#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes exactly one short, angry, funny rant to /output/entry.txt.
Python standard library only, no network access, fully deterministic:
the same text is produced on every run.
"""

import os

ENTRY = (
    "Your Honor, Exhibit A: the office printer. One job. ONE. "
    "It waits until the meeting starts in ninety seconds, then declares "
    "it is out of cyan. The document is black text. It jams on page one, "
    "flashes a light I have never seen in my life, and beeps like IT is "
    "the victim. I move to hold this machine in contempt of court."
)

MAX_CHARS = 400


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # gate requires valid UTF-8 text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
