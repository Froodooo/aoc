from pathlib import Path
from typing import List
from math import dist

from utils import read_to_list


def parse_input(path: Path) -> List[tuple]:
    return [tuple(map(int, line.split(','))) for line in read_to_list(str(path))]


def connect(circuits: List[set], point1: int, point2: int) -> None:
    set1 = set2 = None

    for s in circuits:
        if point1 in s:
            set1 = s
        if point2 in s:
            set2 = s

    if set1 is not set2:
        set1.update(set2)
        circuits.remove(set2)


def init_circuits(num_points: int) -> List[set]:
    return [{i} for i in range(num_points)]


def calculate_distances(points: List[str]) -> List[tuple]:
    distances = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1, p2 = points[i], points[j]
            d = dist(p1, p2)
            distances.append(((i, j), d))

    distances.sort(key=lambda x: x[1])

    return distances


def part_one(points: List[str]) -> int:
    distances = calculate_distances(points)
    circuits = init_circuits(len(points))

    for i in range(1000):
        ((p1, p2), _) = distances[i]
        connect(circuits, p1, p2)

    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def part_two(points: List[str]) -> int:
    distances = calculate_distances(points)
    circuits = init_circuits(len(points))

    i = 0
    p1 = p2 = -1
    while len(circuits) != 1:
        ((p1, p2), _) = distances[i]
        connect(circuits, p1, p2)
        i += 1

    return points[p1][0] * points[p2][0]
