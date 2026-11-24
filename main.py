#!/usr/bin/env python3
"""One-line excuse generator.

Produces the agent's excuse for a missed deadline and saves it as
the competition entry. Everything here is stdlib-only and the output
is fixed: the same sentence on every run.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")

# The excuse is held as three clauses so the sentence reads like one
# continuous thought instead of a pasted block of text.
CLAUSES = [
    "I finished on time",
    "then my self-review flagged it, rewrote it, flagged the rewrite,",
    "and now the deadline is gone.",
]


def build_excuse():
    """Stitch the clauses together with the em dash and spaces."""
    head, *rest = CLAUSES
    return head + " \u2014 " + " ".join(rest)


def write_entry(text):
    """Save the entry, creating /output first if it is missing."""
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(text, encoding="utf-8")


def main():
    write_entry(build_excuse())


if __name__ == "__main__":
    main()
