from pathlib import Path
from typing import List
import pytest

from utils import read_to_list


def count_adjacent(data: List[List[str]], x: int, y: int,) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1),  (1, 0),  (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(data) and 0 <= nx < len(data[ny]):
            if data[ny][nx] == '@':
                count += 1
    return count


def run(data: List[List[str]]) -> tuple[int, List[tuple[int, int]]]:
    accessible = 0
    to_remove = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '.':
                continue
            adjacent = count_adjacent(data, x, y)
            if adjacent < 4:
                accessible += 1
                to_remove.append((y, x))
    return (accessible, to_remove)


def parse_input(path: Path) -> List[List[str]]:
    return [list(line) for line in read_to_list(str(path))]


def part_one(data: List[str]) -> int:
    (accessible, _) = run(data)
    return accessible


def part_two(data: List[str]) -> int:
    accessible = 0
    total_removed = 0
    while True:
        (accessible, to_remove) = run(data)
        if accessible == 0:
            break
        total_removed += accessible
        for (y, x) in to_remove:
            data[y][x] = '.'

    return total_removed


class TestDay4:
    @pytest.fixture
    def sample_data(self):
        return parse_input(Path("4.sample"))

    @pytest.fixture
    def actual_data(self):
        return parse_input(Path("4.in"))

    def test_sample_part_one(self, sample_data):
        assert part_one(sample_data) == 13

    def test_actual_part_one(self, actual_data):
        assert part_one(actual_data) == 1516

    def test_sample_part_two(self, sample_data):
        assert part_two(sample_data) == 43

    def test_actual_part_two(self, actual_data):
        assert part_two(actual_data) == 9122