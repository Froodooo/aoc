from pathlib import Path
from typing import List

from utils import read_to_list


SEEN_SPLITS = set()
SEEN = set()

def beam(manifold: List[List[str]], start: tuple[int, int], path: str = ""):
    (sr, sc) = start

    if sr >= len(manifold):
        return
    
    if (sr, sc) not in SEEN:
        SEEN.add((sr, sc))

    if manifold[sr][sc] == '^':
        if (sr, sc) not in SEEN_SPLITS:
            SEEN_SPLITS.add((sr, sc))
        split_left = (sr, sc - 1)
        split_right = (sr, sc + 1)

        if split_left not in SEEN and split_right not in SEEN:
            beam(manifold, split_left, path + f"({sr},{sc - 1})")
            beam(manifold, split_right, path + f"({sr},{sc + 1})")
        if split_left not in SEEN and split_right in SEEN:
            beam(manifold, split_left, path + f"({sr},{sc - 1})")
        if split_right not in SEEN and split_left in SEEN:
            beam(manifold, split_right, path + f"({sr},{sc + 1})")
    else:
        beam(manifold, (sr + 1, sc), path)


def find_start(manifold: List[List[str]]) -> tuple[int, int]:
    for r, row in enumerate(manifold):
        for c, val in enumerate(row):
            if val == 'S':
                return r, c
    raise ValueError("Start position 'S' not found")


def parse_input(path: Path) -> List[List[str]]:
    return [list(line) for line in read_to_list(str(path))]


def part_one(data: List[str]) -> int:
    (sr, sc) = find_start(data)
    beam(data, (sr, sc))
    return len(SEEN_SPLITS)


def part_two(data: List[str]) -> int:
    (sr, sc) = find_start(data)
    beam(data, (sr, sc))
    return 0
