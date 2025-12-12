from pathlib import Path
from typing import List
import pytest

from utils import read_to_list


def zero_passes(pointer: int, direction: str, clicks: int) -> int:
    count = 0

    for _ in range(clicks):
        pointer = (pointer + 1) % 100 if direction == 'R' else (pointer - 1) % 100
        count += 1 if pointer == 0 else 0

    return count


def zero_point(pointer: int) -> int:
    return 1 if pointer == 0 else 0


def rotate(pointer: int, direction: str, clicks: int) -> int:
    return (pointer + clicks) % 100 if direction == 'R' else (pointer - clicks) % 100


def parse_input(path: Path) -> List[str]:
    '''Read the puzzle input and return as a list of lines.'''
    return read_to_list(str(path))


def part_one(data: List[str]) -> int:
    pointer = 50
    zero_pointer = 0

    for line in data:
        direction = line[0]
        clicks = int(line[1:])
        pointer = rotate(pointer, direction, clicks)
        zero_pointer += zero_point(pointer)

    return zero_pointer


def part_two(data: List[str]) -> int:
    pointer = 50
    zero_pointer = 0

    for line in data:
        direction = line[0]
        clicks = int(line[1:])
        zero_pointer += zero_passes(pointer, direction, clicks)
        pointer = rotate(pointer, direction, clicks)

    return zero_pointer


class TestDay1:
    @pytest.fixture
    def sample_data(self):
        return parse_input(Path("1.sample"))

    @pytest.fixture
    def actual_data(self):
        return parse_input(Path("1.in"))

    def test_sample_part_one(self, sample_data):
        assert part_one(sample_data) == 3

    def test_actual_part_one(self, actual_data):
        assert part_one(actual_data) == 1040

    def test_sample_part_two(self, sample_data):
        assert part_two(sample_data) == 6

    def test_actual_part_two(self, actual_data):
        assert part_two(actual_data) == 6027
