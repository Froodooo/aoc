from pathlib import Path
from typing import List
from shapely.geometry import Polygon

from utils import read_to_list


def parse_input(path: Path) -> List[tuple]:
    return [tuple(int(x) for x in line.split(',')) for line in read_to_list(str(path))]


def area_size(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def poly_rectangle_area(x1: int, y1: int, x2: int, y2: int) -> Polygon:
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    return Polygon([(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)])


def part_one(data: List[str]) -> int:
    largest = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1 = data[i]
            x2, y2 = data[j]
            area = area_size(x1, y1, x2, y2)
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
            rectangle = poly_rectangle_area(x1, y1, x2, y2)
            if rectangle.within(poly_area):
                area = area_size(x1, y1, x2, y2)
                if area > largest:
                    largest = area
    return largest
