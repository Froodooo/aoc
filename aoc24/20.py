from utils import *
from collections import deque

INPUT_FILE = "./20.in"
SAMPLE_FILE = "./20.sample"

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

def part_one(input_path, minimal_save = 100):
  input = [list(x) for x in read_to_list(input_path)]
  walls = [(x, y) for y in range(len(input)) for x in range(len(input[y])) if input[y][x] == "#"]
  start = [(x, y) for y in range(len(input)) for x in range(len(input[y])) if input[y][x] == "S"][0]
  goal = [(x, y) for y in range(len(input)) for x in range(len(input[y])) if input[y][x] == "E"][0]

  path = bfs(start, goal, walls)
  cheats_seen = []
  cheats_by_time = {}

  for i, (x, y) in enumerate(path):
      for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
          xx, yy = x + dx, y + dy
          if (xx, yy) not in walls: continue
          if xx == 0 or yy == 0 or xx == len(input[y]) - 1 or yy == len(input) - 1: continue
          if (xx + dx, yy + dy) in walls: continue
          if (xx + dx, yy + dy) in path and path.index((xx + dx, yy + dy)) < i: continue
          saved_time = path.index((xx + dx, yy + dy)) - i - 2
          if saved_time < minimal_save: continue
          if saved_time <= 0: continue
          cheat_key = (x, y, xx + dx, yy + dy)
          if cheat_key in cheats_seen: continue
          cheats_seen.append(cheat_key)
          if saved_time in cheats_by_time:
              cheats_by_time[saved_time] += 1
          else:
              cheats_by_time[saved_time] = 1

  return sum(cheats_by_time.values())

assert part_one(SAMPLE_FILE, 0) == 44
assert part_one(INPUT_FILE) == 1429

part_one = part_one(INPUT_FILE)
print(part_one)