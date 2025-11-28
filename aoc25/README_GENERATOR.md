Generator for per-day AoC scaffolding

This repository includes `generate_day.py`, a small script to scaffold per-day files.

Usage examples:

- Create files for day 2 in the current folder:

```bash
python generate_day.py 2
```

- Overwrite existing files:

```bash
python generate_day.py 2 --force
```

What it creates:
- `N.py` - a starter Python template that only exposes `parse_input`, `part_one`, and `part_two`.
- `N.sample` - a sample input placeholder.
- `N.in` - an input placeholder where you can paste your puzzle input.

Execution:
- Use the central runner `run_day.py` to execute days and pass the same CLI flags you used before:

```bash
python run_day.py --day 2            # runs ./2.in
python run_day.py --day 2 --sample   # runs ./2.sample
python run_day.py --day 2 --part 1   # runs only part 1
```

Next steps I can take:
- Add a `--git-commit` option to automatically commit scaffolds.
- Make a more featureful template (tests, CI, or package manifests).
- Add a `--year` option for multi-year projects.

Tell me if you want any of those added and I'll implement it.