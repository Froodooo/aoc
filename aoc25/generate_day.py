"""Small generator to scaffold Advent of Code day files in the current directory.

Usage:
    python generate_day.py 2            # creates 2.py, 2.sample, 2.in
    python generate_day.py 2 --force    # overwrite existing files

The generated Python file follows the project's per-day template (only
`parse_input`, `part_one`, `part_two`).
"""

import argparse
from pathlib import Path
import textwrap
from typing import Optional

PY_TEMPLATE = """from pathlib import Path
from typing import List

from utils import read_to_list


def parse_input(path: Path) -> List[str]:
    '''Read the puzzle input and return as a list of lines.'''
    return read_to_list(str(path))


def part_one(data: List[str]) -> int:
    '''Solve part one. Replace with puzzle logic.'''
    # TODO: implement
    return 0


def part_two(data: List[str]) -> int:
    '''Solve part two. Replace with puzzle logic.'''
    # TODO: implement
    return 0
"""

SAMPLE_TEXT = """# sample input for day {n}

"""

EMPTY_IN = """# paste your puzzle input here for day {n}
"""


def write_file(path: Path, content: str, force: bool = False) -> None:
    if path.exists() and not force:
        print(f"Skipped existing: {path} (use --force to overwrite)")
        return
    path.write_text(content, encoding="utf-8")
    print(f"Wrote: {path}")


def create_day(n: int, force: bool) -> None:
    base = Path('.')
    py_path = base / f"{n}.py"
    sample_path = base / f"{n}.sample"
    in_path = base / f"{n}.in"

    py_content = textwrap.dedent(PY_TEMPLATE)
    sample_content = SAMPLE_TEXT.format(n=n)
    in_content = EMPTY_IN.format(n=n)

    write_file(py_path, py_content, force=force)
    write_file(sample_path, sample_content, force=force)
    write_file(in_path, in_content, force=force)


def main_cli(argv: Optional[list] = None) -> int:
    p = argparse.ArgumentParser(description="Generate Advent of Code day scaffold")
    p.add_argument("day", type=int, help="day number (e.g. 2)")
    p.add_argument("--force", "-f", action="store_true", help="overwrite existing files")
    args = p.parse_args(argv)

    if not (1 <= args.day <= 25):
        print("day must be between 1 and 25")
        return 2

    create_day(args.day, force=args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main_cli())
