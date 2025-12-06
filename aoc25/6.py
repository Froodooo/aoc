from pathlib import Path
from typing import List
from math import prod

from utils import read_to_list


def parse_input(path: Path) -> List[str]:
    return read_to_list(str(path))


def part_one(data: List[str]) -> int:
    lines = [item.split() for item in data]
    problems = [[int(item) for item in line] for line in lines[:-1]]

    operations = lines[-1]
    columns = problems[0]

    for line in problems[1:]:
        for i in range(len(columns)):
            if operations[i] == '+':
                columns[i] += line[i]
            elif operations[i] == '*':
                columns[i] *= line[i]

    return sum(columns)


def part_two(data: List[str]) -> int:
    problems = data[:-1]
    operations = data[-1].split()

    total = 0
    numbers = []

    for i in range(len(problems[0]) - 1, -2, -1):
        if all(problem[i] == ' ' for problem in problems) or i == -1:
            operation = operations.pop()
            if operation == '+':
                total += sum(numbers)
            elif operation == '*':
                total += prod(numbers)
            numbers = []
        else:
            column = ''.join(problem[i] for problem in problems).strip()
            numbers.append(int(column))

    return total
