from pathlib import Path
from typing import List
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD
from re import sub
from itertools import combinations

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


def find_shortest_xor_combo(button_wirings: List[str], target: str) -> List[str]:
    target_int = bitmask_to_int(target)
    values = [bitmask_to_int(b) for b in button_wirings]

    for r in range(1, len(button_wirings) + 1):
        for combo in combinations(range(len(button_wirings)), r):
            xor_value = 0
            for i in combo:
                xor_value ^= values[i]
            if xor_value == target_int:
                return [button_wirings[i] for i in combo]


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


def configure_machine(vectors: List[tuple], target: List[int], start: tuple) -> int:
    """
    Solve: minimize sum x_j
    s.t.   sum_j x_j * vectors[j][i] = target[i]  for each coordinate i
           x_j >= 0 and integer

    Returns the minimal number of vectors (sum x_j) or None if impossible.
    """
    # Define problem
    problem = LpProblem("configure_machine", LpMinimize)

    # Decision vars: x_i >= 0, integer
    variables = [
        LpVariable(f"x_{i}", lowBound=0, cat="Integer")
        for i in range(len(vectors))
    ]

    # Objective: minimize total number of vectors used
    problem += lpSum(variables)

    # Constraints: component-wise equality to target
    for i in range(len(target)):
        problem += lpSum(vectors[j][i] * variables[j]
                         for j in range(len(vectors))) == target[i]

    # Solve
    problem.solve(PULP_CBC_CMD(msg=False))

    # Sum of all chosen counts = number of vectors used
    return sum(int(var.value()) for var in variables)


def part_one(data: List[str]) -> int:
    button_presses = 0
    for (light_diagram, button_wirings, _) in data:
        button_wirings = button_wiring_to_bitmask(
            button_wirings, len(light_diagram))
        result = find_shortest_xor_combo(button_wirings, light_diagram)
        button_presses += len(result)

    return button_presses


def part_two(data: List[str]) -> int:
    button_presses = 0
    for (_, button_wirings, joltage_requirements) in data:
        button_vectors = button_wiring_to_vector(
            button_wirings, len(joltage_requirements))
        joltage_start = tuple([0] * len(joltage_requirements))
        button_presses += configure_machine(button_vectors,
                                            joltage_requirements, joltage_start)

    return button_presses
