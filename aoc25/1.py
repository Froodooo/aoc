from __future__ import annotations

from pathlib import Path
from typing import List

from utils import read_to_list


def parse_input(path: Path) -> List[str]:
  """Read the puzzle input and return as a list of lines.

  Use `read_to_list` from `utils.py` so this is easy to swap later.
  """
  return [int(line) for line in read_to_list(str(path))]


def part_one(data: List[str]) -> int:
  """Solve part one.

  Replace the body with puzzle logic. Accepts parsed input rather than a
  path so it's easy to call from tests.
  """
  # TODO: implement
  return 0


def part_two(data: List[str]) -> int:
  """Solve part two.

  Optional: implement when needed.
  """
  # TODO: implement
  return 0