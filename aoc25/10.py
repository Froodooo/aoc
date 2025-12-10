from pathlib import Path
from typing import List
from re import sub
from itertools import combinations
from collections import deque

from utils import read_to_list


def parse_line_diagram(line: str) -> str:
    return sub('[#]', '1', sub('[.]', '0', sub('[\\[\\]]', '', line)))


def parse_button_wirings(line: str, length: int) -> List[int]:
    return [[int(y) for y in x.split(',')] for x in [sub('[()]', '', c) for c in line[1:len(line)-1]]]


def parse_joltage_requirements(line: str) -> tuple:
    return tuple([int(x) for x in sub('[\\{\\}]', '', line[-1]).split(',')])


def parse_input(path: Path) -> List[str]:
    data = [line.split(" ") for line in read_to_list(str(path))]
    lines = []
    for line in data:
        light_diagram = parse_line_diagram(line[0])
        button_wirings = parse_button_wirings(line, len(light_diagram))
        joltage_requirements = parse_joltage_requirements(line)
        lines.append((light_diagram, button_wirings, joltage_requirements))

    return lines


def bitmask_to_int(b):
    return int(b, 2)


def find_shortest_xor_combo(button_wirings, target):
    target_int = bitmask_to_int(target)
    values = [bitmask_to_int(b) for b in button_wirings]

    for r in range(1, len(button_wirings) + 1):
        for combo in combinations(range(len(button_wirings)), r):
            xor_value = 0
            for i in combo:
                xor_value ^= values[i]
            if xor_value == target_int:
                return [button_wirings[i] for i in combo]


def button_wiring_to_bitmask(button_wirings_list: List[int], length: int) -> str:
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


def configure_machine(button_vectors: List[tuple], joltage_requirements: List[int], start: tuple):
    length = len(joltage_requirements)

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, dist = queue.popleft()

        for vector in button_vectors:
            new_state = tuple(state[i] + vector[i] for i in range(length))

            if any(new_state[i] > joltage_requirements[i] for i in range(length)):
                continue

            if new_state == joltage_requirements:
                return dist + 1

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, dist + 1))


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
