from pathlib import Path
from typing import List
import pytest

from utils import read_to_list


def parse_input(path: Path) -> List[List[int]]:
    return [[int(char) for char in x] for x in read_to_list(str(path))]


def calculate_joltage(banks: List[List[int]], nr_of_batteries: int) -> int:
    total_joltage = 0
    for bank in banks:
        joltage = ""
        start_index = 0
        for i in range(1, nr_of_batteries + 1):
            end_index = -(nr_of_batteries - i) if (nr_of_batteries - i) != 0 else len(bank)
            max_battery = max(bank[start_index:end_index])
            start_index = bank[start_index:end_index].index(max_battery) + start_index + 1
            joltage += str(max_battery)
        total_joltage += int(joltage)
    return total_joltage


def part_one(data: List[str]) -> int:
    return calculate_joltage(data, 2)


def part_two(data: List[str]) -> int:
    return calculate_joltage(data, 12)


class TestDay3:
    @pytest.fixture
    def sample_data(self):
        return parse_input(Path("3.sample"))

    @pytest.fixture
    def actual_data(self):
        return parse_input(Path("3.in"))

    def test_sample_part_one(self, sample_data):
        assert part_one(sample_data) == 357

    def test_actual_part_one(self, actual_data):
        assert part_one(actual_data) == 17316

    def test_sample_part_two(self, sample_data):
        assert part_two(sample_data) == 3121910778619

    def test_actual_part_two(self, actual_data):
        assert part_two(actual_data) == 171741365473332