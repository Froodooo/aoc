from pathlib import Path
from typing import List

from utils import read_to_list


def parse_input(path: Path) -> List[str]:
    return [tuple(int(x) for x in line.split(',')) for line in read_to_list(str(path))]


def part_one(data: List[str]) -> int:
    largest = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1 = data[i]
            x2, y2 = data[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > largest:
                largest = area
    return largest


def part_two(data: List[str]) -> int:
    largest = 0
    for i in range(len(data)):
        x1, y1 = data[i]
        if i == 0:
            x0, y0 = data[-1]
        else:
            x0, y0 = data[i - 1]
        if i == len(data) - 1:
            x2, y2 = data[0]
        else:
            x2, y2 = data[i + 1]

        
    return largest
