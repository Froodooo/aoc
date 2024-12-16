from utils import *
import heapq

INPUT_FILE = "./16.in"
SAMPLE_FILE = "./16.sample"

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
directions_inverted = {
    (1, 0): (-1, 0),
    (0, 1): (0, -1),
    (-1, 0): (1, 0),
    (0, -1): (0, 1)
}

def bfs(start, end, walls):
    sx, sy = start
    queue = [(0, sx, sy, 1, 0)]
    visited = {(sx, sy, 1, 0)}
    while queue:
        cost, x, y, cdx, cdy = heapq.heappop(queue)
        visited.add((x, y, cdx, cdy))
        if (x, y) == end:
            return cost
        for dx, dy in directions:
            if directions_inverted[(dx, dy)] == (cdx, cdy):
                continue
            ndx = cdx if (dx, dy) == (cdx, cdy) else dx
            ndy = cdy if (dx, dy) == (cdx, cdy) else dy
            nx = x + dx if (cdx, cdy) == (dx, dy) else x
            ny = y + dy if (cdx, cdy) == (dx, dy) else y
            if (nx, ny) in walls:
                continue
            if (nx, ny, ndx, ndy) in visited:
                continue
            cost_add = 1 if (cdx, cdy) == (dx, dy) else 1000
            heapq.heappush(queue, (cost + cost_add, nx, ny, ndx, ndy))

def part_one(path):
    maze = [list(x) for x in read_to_list(path)]

    walls = {(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "#"}
    start = [(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "S"][0]
    end = [(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "E"][0]

    return bfs(start, end, walls)

assert part_one(SAMPLE_FILE) == 11048
assert part_one(INPUT_FILE) == 85480

part_one = part_one(INPUT_FILE)
print(part_one)