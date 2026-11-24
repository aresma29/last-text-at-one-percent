#!/usr/bin/env python3
"""Print the last text a phone sends at one percent battery."""
from pathlib import Path


def main() -> int:
    # Entry lives beside this file, so the bot runs from any cwd,
    # even on a read-only filesystem.
    entry = Path(__file__).with_name("entry.txt")
    print(entry.read_text(encoding="utf-8").strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
