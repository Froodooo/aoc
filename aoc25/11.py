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


def dfs_with_required_servers(rack, start, required_nodes=('dac', 'fft')):
    required_index = {server: idx for idx, server in enumerate(required_nodes)}
    required_mask = (1 << len(required_nodes)) - 1

    def visit_mask(server: str) -> int:
        return 1 << required_index[server] if server in required_index else 0

    start_mask = visit_mask(start)

    @lru_cache(maxsize=None)
    def dfs(server: str, mask: int) -> int:
        total_paths = 0
        for neighbour in rack[server]:
            new_mask = mask | visit_mask(neighbour)
            if neighbour == 'out':
                if new_mask == required_mask:
                    total_paths += 1
                continue
            total_paths += dfs(neighbour, new_mask)
        return total_paths

    return dfs(start, start_mask)


def part_one(rack: dict) -> int:
    paths = bfs(rack, 'you')
    return paths


def part_two(rack: List[str]) -> int:
    paths = dfs_with_required_servers(rack, 'svr')
    return paths
