from pathlib import Path
from typing import List
from re import sub
from itertools import combinations

from utils import read_to_list


def parse_line_diagram(line: str) -> str:
    return sub('[#]', '1', sub('[.]', '0', sub('[\\[\\]]', '', line)))


def parse_button_schematics(line: str, length: int) -> List[int]:
    button_wirings_list = [[int(y) for y in x.split(',')] for x in [sub('[()]', '', c) for c in line[1:len(line)-1]]]
    button_wirings = []
    for button_wiring in button_wirings_list:
        button_bitmap = ''
        for i in range(length):
            bit = '1' if i in button_wiring else '0'
            button_bitmap += bit
        button_wirings.append(button_bitmap)
    return button_wirings


def parse_joltage_requirements(line: str) -> str:
    return line[-1]

def parse_input(path: Path) -> List[str]:
    data = [line.split(" ") for line in read_to_list(str(path))]
    lines = []
    for line in data:
        light_diagram = parse_line_diagram(line[0])
        button_schematics = parse_button_schematics(line, len(light_diagram))
        joltage_requirements = parse_joltage_requirements(line)
        lines.append((light_diagram, button_schematics, joltage_requirements))
    return lines


def bitmask_to_int(b):
    return int(b, 2)


def find_shortest_xor_combo(bits, target):
    target_int = bitmask_to_int(target)
    values = [bitmask_to_int(b) for b in bits]

    for r in range(1, len(bits) + 1):
        for combo in combinations(range(len(bits)), r):
            xor_value = 0
            for i in combo:
                xor_value ^= values[i]
            if xor_value == target_int:
                return [bits[i] for i in combo]


def part_one(data: List[str]) -> int:
    button_presses = 0
    for (light_diagram, button_schematics, _) in data:
        result = find_shortest_xor_combo(button_schematics, light_diagram)
        button_presses += len(result)

    return button_presses


def part_two(data: List[str]) -> int:
    '''Solve part two. Replace with puzzle logic.'''
    # TODO: implement
    return 0
