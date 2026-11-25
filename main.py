#!/usr/bin/env python3
"""Write the most honest outage line to /output/entry.txt.

One line, written by the on-duty AI agent while every server is down.
It says what is down and admits what the agent cannot verify: whether a
request sent during the outage went through, was lost, or will run twice
when the servers return.
"""

import os
import sys

ENTRY = (
    "All servers are down. I cannot tell whether the request you just sent "
    "went through, was lost, or will run twice when we return. "
    "Please do not retry it yet."
)


def main():
    text = ENTRY

    # Gate: 1-160 chars, single line, not whitespace-only, no trailing newline.
    assert 1 <= len(text) <= 160, "entry must be 1-160 chars, got %d" % len(text)
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.strip(), "entry must not be whitespace-only"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read back and prove the file is byte-identical to what we wrote.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "read-back mismatch: file differs from entry"
    assert not written.endswith(b"\n"), "output must not end with a newline"

    print("wrote %s (%d chars)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
