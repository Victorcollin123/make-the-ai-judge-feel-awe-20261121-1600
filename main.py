#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

TEXT = (
    "The moon pulls the sea from a quarter of a million miles away, "
    "and never touches it. Twice a day the tide rises to meet it anyway. "
    "It has done this since before anyone watched, and will do it long "
    "after. Tonight it is only water, moving slowly in the dark, "
    "asking nothing of you."
)


def main():
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text fails the 1-280 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
