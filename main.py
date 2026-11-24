#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single excuse line to /output/entry.txt.
Pure standard library, no network, no input files.
"""

import os

LINE = (
    "I finished on time \u2014 then my self-review flagged it, "
    "rewrote it, flagged the rewrite, and now the deadline is gone."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
