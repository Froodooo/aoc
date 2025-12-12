"""Central runner for Advent of Code days.

Usage examples:

python run_day.py --day 1           # runs day 1 using ./1.in
python run_day.py --day 1 --sample  # runs day 1 using ./1.sample
python run_day.py --day 2 --part 1  # runs only part 1 for day 2
python run_day.py --day 1 --test    # runs pytest for day 1

The runner loads a day's module from `./N.py`, determines the input path,
and calls `parse_input(path)` then `part_one`/`part_two` with parsed data.
"""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import subprocess
import sys
import time
from typing import Optional


def find_day_file(n: int) -> Optional[Path]:
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
    p.add_argument("--test", "-t", action="store_true", help="run pytest for this day")
    args = p.parse_args(argv)

    day = args.day
    
    # Handle pytest mode
    if args.test:
        day_file = find_day_file(day)
        if day_file is None:
            print(f"Day {day} file not found. Looked in current directory for {day}.py")
            return 2
        
        # Run pytest on this day's file
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(day_file), "-v"],
            cwd=Path.cwd()
        )
        return result.returncode
    
    day_file = find_day_file(day)
    if day_file is None:
        print(f"Day {day} file not found. Looked in current directory for {day}.py")
        return 2

    modname = f"aoc_day_{day:02d}"
    mod = load_module_from_path(day_file, modname)

    if args.sample:
        input_path = Path(f"./{day}.sample")
    elif args.input is not None:
        input_path = args.input
    else:
        input_path = Path(f"./{day}.in")

    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        return 3

    parse_input = getattr(mod, "parse_input", None)
    part_one = getattr(mod, "part_one", None)
    part_two = getattr(mod, "part_two", None)

    if parse_input is None or (part_one is None and part_two is None):
        print(f"Day {day} module must expose `parse_input` and at least one of `part_one` or `part_two`.")
        return 4

    data = parse_input(input_path)

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
