from functools import lru_cache
from pathlib import Path
from typing import List

from utils import read_to_list


def parse_input(path: Path) -> dict:
    lines = read_to_list(str(path))
    device_outputs = {}
    for line in lines:
        device, output = line.split(": ")
        output = output.split(" ")
        device_outputs[device] = output
    return device_outputs


def bfs(rack, start):
    queue = [start]
    paths = 0

    while queue:
        m = queue.pop(0)

        for neighbour in rack[m]:
            if neighbour == 'out':
                paths += 1
                continue
            queue.append(neighbour)

    return paths


def dfs_with_required_servers(rack, start):

    @lru_cache(maxsize=None)
    def dfs(server: str, seen_dac=False, seen_fft=False) -> int:
        total_paths = 0
        for neighbour in rack[server]:
            new_seen_dac = neighbour == 'dac' or seen_dac
            new_seen_fft = neighbour == 'fft' or seen_fft
            if neighbour == 'out':
                if new_seen_fft and new_seen_dac:
                    total_paths += 1
                continue
            total_paths += dfs(neighbour, new_seen_dac, new_seen_fft)
        return total_paths

    return dfs(start)


def part_one(rack: dict) -> int:
    paths = bfs(rack, 'you')
    return paths


def part_two(rack: List[str]) -> int:
    paths = dfs_with_required_servers(rack, 'svr')
    return paths
