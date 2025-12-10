from itertools import combinations
from pathlib import Path
from re import sub
from typing import List

from pulp import LpMinimize, LpProblem, LpVariable, PULP_CBC_CMD, lpSum

from utils import read_to_list


def parse_light_diagram(line: str) -> str:
    return sub('[#]', '1', sub('[.]', '0', sub('[\\[\\]]', '', line)))


def parse_button_wirings(line: str, length: int) -> List[int]:
    return [[int(y) for y in x.split(',')] for x in [sub('[()]', '', c) for c in line[1:len(line)-1]]]


def parse_joltage_requirements(line: str) -> tuple[int]:
    return tuple([int(x) for x in sub('[\\{\\}]', '', line[-1]).split(',')])


def parse_input(path: Path) -> List[tuple]:
    data = [line.split(" ") for line in read_to_list(str(path))]
    lines = []
    for line in data:
        light_diagram = parse_light_diagram(line[0])
        button_wirings = parse_button_wirings(line, len(light_diagram))
        joltage_requirements = parse_joltage_requirements(line)
        lines.append((light_diagram, button_wirings, joltage_requirements))

    return lines


def bitmask_to_int(bitmask: str) -> int:
    return int(bitmask, 2)


def button_wiring_to_bitmask(button_wirings_list: List[int], length: int) -> List[str]:
    button_wirings = []
    for button_wiring in button_wirings_list:
        button_bitmap = ''
        for i in range(length):
            bit = '1' if i in button_wiring else '0'
            button_bitmap += bit
        button_wirings.append(button_bitmap)

    return button_wirings


def button_wiring_to_vector(button_wirings: List[int], length: int) -> List[int]:
    button_vectors = []
    for button in button_wirings:
        bitmask = [0] * length
        for bit in button:
            bitmask[bit] = 1
        button_vectors.append(bitmask)

    return button_vectors


def start_machine(button_wirings_bitmask: List[str], light_diagram: int) -> List[str]:
    button_wirings = [bitmask_to_int(b) for b in button_wirings_bitmask]
    buttons_length = len(button_wirings)

    for r in range(1, buttons_length + 1):
        for combo in combinations(range(buttons_length), r):
            xor_value = 0
            for i in combo:
                xor_value ^= button_wirings[i]
            if xor_value == light_diagram:
                return [button_wirings[i] for i in combo]


def configure_machine(vectors: List[tuple], target: List[int]) -> int:
    problem = LpProblem("configure_machine", LpMinimize)

    variables = [
        LpVariable(f"x_{i}", lowBound=0, cat="Integer")
        for i in range(len(vectors))
    ]

    problem += lpSum(variables)

    for i in range(len(target)):
        problem += lpSum(vectors[j][i] * variables[j] for j in range(len(vectors))) == target[i]

    problem.solve(PULP_CBC_CMD(msg=False))

    return sum(int(var.value()) for var in variables)


def part_one(data: List[str]) -> int:
    button_presses = 0

    for (light_diagram, button_wirings, _) in data:
        button_wirings_bitmask = button_wiring_to_bitmask(button_wirings, len(light_diagram))
        result = start_machine(button_wirings_bitmask, bitmask_to_int(light_diagram))
        button_presses += len(result)

    return button_presses


def part_two(data: List[str]) -> int:
    button_presses = 0
    for (_, button_wirings, joltage_requirements) in data:
        button_vectors = button_wiring_to_vector(button_wirings, len(joltage_requirements))
        button_presses += configure_machine(button_vectors, joltage_requirements)

    return button_presses
