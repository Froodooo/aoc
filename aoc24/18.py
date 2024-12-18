from utils import *
from collections import deque

INPUT_FILE = "./18.in"
SAMPLE_FILE = "./18.sample"

def bfs(start, goal, width, height, corrupted):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 <= width and 0 <= y2 <= height and (x2, y2) not in corrupted and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def part_one(path, max_x = 70, max_y = 70, sample_size = 1024):
    start = (0, 0)
    end = (max_x, max_y)

    bytes = [tuple(int(y) for y in x.split(",")) for x in read_to_list(path)]
    bytes_sample = bytes[:sample_size]

    memory = set(bytes_sample)
    path = bfs(start, end, max_x, max_y, memory)
    return len(path) - 1

def part_two(path, max_x = 70, max_y = 70, sample_size = 1024):
    start = (0, 0)
    end = (max_x, max_y)

    bytes = [tuple(int(y) for y in x.split(",")) for x in read_to_list(path)]
    bytes_sample = bytes[:sample_size]

    memory = set(bytes_sample)
    while bfs(start, end, max_x, max_y, memory):
        memory.add(bytes[sample_size])
        sample_size += 1
    (x, y) =  bytes[sample_size - 1]
    return f"{x},{y}"

assert part_one(SAMPLE_FILE, 6, 6, 12) == 22
assert part_one(INPUT_FILE) == 246

assert part_two(SAMPLE_FILE, 6, 6, 12) == "6,1"
assert part_two(INPUT_FILE) == "22,50"

part_one = part_one(INPUT_FILE)
part_two = part_two(INPUT_FILE)
print(part_one, part_two)

