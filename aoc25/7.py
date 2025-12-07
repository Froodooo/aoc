from pathlib import Path
from typing import List
from functools import lru_cache

from utils import read_to_list

SEEN_SPLITS = set()


def parse_input(path: Path) -> List[List[str]]:
    return [list(line) for line in read_to_list(str(path))]


def beam(manifold: List[List[str]], start: tuple[int, int]) -> int:
    (sr, sc) = start

    @lru_cache(maxsize=None)
    def dp(sr: int, sc: int) -> int:
        if sr >= len(manifold):
            return 1
        
        if manifold[sr][sc] == '^':
            if (sr, sc) not in SEEN_SPLITS:
                SEEN_SPLITS.add((sr, sc))

            return dp(sr, sc - 1) + dp(sr, sc + 1)
        else:
            return dp(sr + 1, sc)
    
    return dp(sr, sc)


def find_start(manifold: List[List[str]]) -> tuple[int, int]:
    for r, row in enumerate(manifold):
        for c, val in enumerate(row):
            if val == 'S':
                return r, c


def part_one(data: List[str]) -> int:
    (sr, sc) = find_start(data)
    beam(data, (sr, sc))

    return len(SEEN_SPLITS)


def part_two(data: List[str]) -> int:
    (sr, sc) = find_start(data)

    return beam(data, (sr, sc))
