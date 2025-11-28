"""Central runner for Advent of Code days.

Usage examples:

python run_day.py --day 1           # runs day 1 using ./1.in
python run_day.py --day 1 --sample  # runs day 1 using ./1.sample
python run_day.py --day 2 --part 1  # runs only part 1 for day 2

The runner loads a day's module from `./N.py`, determines the input path,
and calls `parse_input(path)` then `part_one`/`part_two` with parsed data.
"""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import time
from typing import Optional


def find_day_file(n: int) -> Optional[Path]:
    # Only look for `N.py` in the current directory.
    p = Path(f"{n}.py")
    return p if p.exists() else None


def load_module_from_path(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, str(path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="run_day")
    p.add_argument("--day", "-d", type=int, required=True, help="day number to run")
    p.add_argument("--input", "-i", type=Path, help="input file (default: ./N.in)")
    p.add_argument("--sample", "-s", action="store_true", help="use sample input (./N.sample)")
    p.add_argument("--part", "-p", choices=["1", "2", "both"], default="both", help="which part to run")
    p.add_argument("--test", "-t", action="store_true", help="run simple sample assertions")
    args = p.parse_args(argv)

    day = args.day
    day_file = find_day_file(day)
    if day_file is None:
        print(f"Day {day} file not found. Looked in current directory for {day}.py")
        return 2

    # load module with a stable name
    modname = f"aoc_day_{day:02d}"
    mod = load_module_from_path(day_file, modname)

    # Determine input path based on CLI flags
    if args.sample:
        input_path = Path(f"./{day}.sample")
    elif args.input is not None:
        input_path = args.input
    else:
        input_path = Path(f"./{day}.in")

    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        return 3

    # Extract required functions from day module
    parse_input = getattr(mod, "parse_input", None)
    part_one = getattr(mod, "part_one", None)
    part_two = getattr(mod, "part_two", None)

    if parse_input is None or (part_one is None and part_two is None):
        print(f"Day {day} module must expose `parse_input` and at least one of `part_one` or `part_two`.")
        return 4

    data = parse_input(input_path)

    if args.test:
        sample_path = Path(f"./{day}.sample")
        if not sample_path.exists():
            print(f"Sample file not found: {sample_path}")
            return 5
        sample_data = parse_input(sample_path)
        try:
            if part_one is not None:
                assert part_one(sample_data) == 0, "part_one sample test failed"
            print("✓ Sample tests passed")
        except AssertionError as e:
            print(f"✗ {e}")
            return 6

    if args.part in ("1", "both") and part_one is not None:
        t0 = time.perf_counter()
        out1 = part_one(data)
        t1 = time.perf_counter()
        print(f"Part 1: {out1} (t={t1-t0:.4f}s)")

    if args.part in ("2", "both") and part_two is not None:
        t0 = time.perf_counter()
        out2 = part_two(data)
        t1 = time.perf_counter()
        print(f"Part 2: {out2} (t={t1-t0:.4f}s)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
