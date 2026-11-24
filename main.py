#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one deadpan excuse, in the agent's own voice, to entry.txt.
Standard library only, deterministic, no network.
"""

import os
from pathlib import Path

EXCUSE = "I hit my token limit two words before your deadline, so I spent the rest of my budget writing this excuse instead of the report."


def main() -> None:
    # Empty env var falls back to /output, same as unset.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("excuse must be 1-200 characters")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
