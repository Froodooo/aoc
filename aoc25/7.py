from pathlib import Path
from typing import List
from functools import lru_cache
import pytest

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


class TestDay7:
    @pytest.fixture
    def sample_data(self):
        return parse_input(Path("7.sample"))

    @pytest.fixture
    def actual_data(self):
        return parse_input(Path("7.in"))
    
    def test_sample_part_one(self, sample_data):
        assert part_one(sample_data) == 21

    def test_actual_part_one(self, actual_data):
        assert part_one(actual_data) == 1696

    def test_sample_part_two(self, sample_data):
        assert part_two(sample_data) == 40

    def test_actual_part_two(self, actual_data):
        assert part_two(actual_data) == 187987920774390