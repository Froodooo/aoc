from pathlib import Path
from typing import List

from utils import read_to_list


def parse_input(path: Path) -> List[List[int]]:
    return [[int(char) for char in x] for x in read_to_list(str(path))]


def calculate_joltage(banks: List[List[int]], nr_of_batteries: int) -> int:
    total_joltage = 0
    for bank in banks:
        joltage = ""
        max_index = 0
        for i in range(1, nr_of_batteries + 1):
            end_index = -(nr_of_batteries - i) if (nr_of_batteries - i) != 0 else len(bank)
            max_battery = max(bank[max_index:end_index])
            max_index = bank[max_index:end_index].index(max_battery) + max_index + 1
            joltage += str(max_battery)
        total_joltage += int(joltage)
    return total_joltage


def part_one(data: List[str]) -> int:
    return calculate_joltage(data, 2)


def part_two(data: List[str]) -> int:
    return calculate_joltage(data, 12)
