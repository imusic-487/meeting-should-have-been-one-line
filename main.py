#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt.
"""

import os

ENTRY = "This meeting is just an email that took an hour to say 'yes'."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and verify the gate: UTF-8 text, 1-200 chars, one line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert written.strip() and "\n" not in written.strip(), "entry must be a single line"


if __name__ == "__main__":
    main()
