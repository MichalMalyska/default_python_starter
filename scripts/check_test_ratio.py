"""Fail when test code grows much larger than source code.

This is a rough guard against overtesting. Lines that are blank or only a
comment are not counted. Change MAX_RATIO if a project needs more.
"""

import sys
from pathlib import Path

MAX_RATIO = 1.5
MIN_SOURCE_LINES = 200  # Small projects skip the check.


def count_lines(root: Path) -> int:
    lines = (line.strip() for path in root.rglob("*.py") for line in path.read_text().splitlines())
    return sum(1 for line in lines if line and not line.startswith("#"))


def main() -> None:
    source = count_lines(Path("src"))
    tests = count_lines(Path("tests"))
    if source >= MIN_SOURCE_LINES and tests > source * MAX_RATIO:
        sys.exit(
            f"Test code is {tests / source:.1f}x source code ({tests} vs {source} lines). Limit: {MAX_RATIO}x.\n"
            "Delete tests that repeat each other or test implementation details.",
        )


if __name__ == "__main__":
    main()
