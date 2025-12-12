from pathlib import Path
from typing import List
import pytest

from utils import read_to_line


def parse_input(path: Path) -> List[str]:
    return read_to_line(str(path)).split(',')


def part_one(data: List[str]) -> int:
    invalid_sum = 0
    for id_range in data:
        start, end = map(int, id_range.split('-'))
        for id in range(start, end + 1):
            if len(str(id)) % 2 == 1:
                continue
            id_s = str(id)
            mid = len(id_s) // 2
            left = id_s[:mid]
            right = id_s[mid:]
            if left == right:
                invalid_sum += id
    return invalid_sum


def part_two(data: List[str]) -> int:
    invalid_sum = 0
    for id_range in data:
        start, end = map(int, id_range.split('-'))
        for id in range(start, end + 1):
            id_s = str(id)
            # https://blog.finxter.com/5-best-ways-to-check-if-a-string-is-a-repeated-pattern-in-python/
            if id_s in (id_s + id_s)[1:-1]:
                invalid_sum += id
    return invalid_sum


class TestDay2:
    @pytest.fixture
    def sample_data(self):
        return parse_input(Path("2.sample"))

    @pytest.fixture
    def actual_data(self):
        return parse_input(Path("2.in"))

    def test_sample_part_one(self, sample_data):
        assert part_one(sample_data) == 1227775554

    def test_actual_part_one(self, actual_data):
        assert part_one(actual_data) == 41294979841

    def test_sample_part_two(self, sample_data):
        assert part_two(sample_data) == 4174379265

    def test_actual_part_two(self, actual_data):
        assert part_two(actual_data) == 66500947346