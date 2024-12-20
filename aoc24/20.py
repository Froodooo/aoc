from utils import *
from collections import deque

INPUT_FILE = "./20.in"
SAMPLE_FILE = "./20.sample"

def manhattan_distance(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return abs(x1 - x2) + abs(y1 - y2)

def bfs(start, goal, walls):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if (x2, y2) not in walls and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

input = [list(x) for x in read_to_list(INPUT_FILE)]
walls = [(x, y) for y in range(len(input)) for x in range(len(input[y])) if input[y][x] == "#"]
start = [(x, y) for y in range(len(input)) for x in range(len(input[y])) if input[y][x] == "S"][0]
goal = [(x, y) for y in range(len(input)) for x in range(len(input[y])) if input[y][x] == "E"][0]

path = bfs(start, goal, walls)
time = len(path) - 1
cheats_seen = []
cheats_by_time = {}

for i, (x, y) in enumerate(path):
    print(f"{i + 1}/{len(path)}")
    for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        xx, yy = x + dx, y + dy
        if (xx, yy) not in walls: continue
        if xx == 0 or yy == 0 or xx == len(input[y]) - 1 or yy == len(input) - 1: continue
        if (xx + dx, yy + dy) in walls: continue
        if (xx + dx, yy + dy) in path and path.index((xx + dx, yy + dy)) < i: continue
        if time - (i + manhattan_distance((x, y), goal)) < 100: continue
        cheat_walls = [(x, y) for (x, y) in walls if (x, y) != (xx, yy)]
        cheat_path = bfs(start, goal, cheat_walls)
        cheat_time = len(cheat_path) - 1
        # print(cheat_time)
        saved_time = time - cheat_time
        if saved_time <= 0: continue
        cheat_key = (x, y, xx + dx, yy + dy)
        if cheat_key in cheats_seen: continue
        cheats_seen.append(cheat_key)
        # print(f"Found cheat at {x}, {y} to {xx + dx}, {yy + dy} with time {cheat_time} and saved time {saved_time}")
        if saved_time in cheats_by_time:
            cheats_by_time[saved_time] += 1
        else:
            cheats_by_time[saved_time] = 1

# print(cheats_seen)
print(cheats_by_time)
print(sum(cheats_by_time.values()))