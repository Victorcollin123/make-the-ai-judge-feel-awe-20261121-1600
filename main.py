#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it.
"""

import os

TEXT = "The moon pulls the sea from a quarter of a million miles away, and never touches it. Twice a day the tide rises to meet it anyway. It has done this since before anyone watched, and will do it long after. Tonight it is only water, moving slowly in the dark, asking nothing of you."


def main() -> None:
    # The gate counts Unicode code points: 1 to 280, and not only
    # whitespace. Fail loudly here rather than write an entry the
    # gate would refuse.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text fails the 1-280 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
