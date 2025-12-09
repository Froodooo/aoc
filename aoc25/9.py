from pathlib import Path
from typing import List
from shapely.geometry import Polygon

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
    poly_area = Polygon(data)
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1 = data[i]
            x2, y2 = data[j]
            x_min, x_max = min(x1, x2), max(x1, x2)
            y_min, y_max = min(y1, y2), max(y1, y2)
            rectangle = Polygon([(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)])
            if rectangle.within(poly_area):
                area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
                if area > largest:
                    largest = area
    return largest
