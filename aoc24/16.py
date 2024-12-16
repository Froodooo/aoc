from utils import *
from collections import deque

INPUT_FILE = "./16.in"
SAMPLE_FILE = "./16.sample"

def bfs(start, goal, walls):
    queue = deque([[start]])
    queue_dir = deque([(1, 0)])
    score = {start: 0}
    results = []
    while queue:
        path = queue.popleft()
        pdx, pdy = queue_dir.popleft()
        x, y = path[-1]
        if (x, y) == goal:
            results.append((path, score[(x, y)]))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            direction_score = 0 if (dx, dy) == (pdx, pdy) else 1000
            if (nx, ny) not in walls:
                if (nx, ny) not in score or score[(nx, ny)] > score[(x, y)] + direction_score + 1:
                    # print(f"Checking: {nx}, {ny}")
                    # print(f"Path: {path}")
                    # if (nx, ny) in score and score[(nx, ny)] > score[(x, y)] + direction_score + 1: print(f"Lower score, replacing {score[(nx, ny)]} with {score[(x, y)] + direction_score + 1}")
                    # print(f"Score: {score[(x, y)] + direction_score + 1}")
                    # print("---")
                    queue.append(path + [(nx, ny)])
                    queue_dir.append((dx, dy))
                    score[(nx, ny)] = score[(x, y)] + direction_score + 1
    return results

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

maze = [list(x) for x in read_to_list(INPUT_FILE)]

walls = {(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "#"}
start = [(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "S"][0]
end = [(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "E"][0]

results = bfs(start, end, walls)
min_result = min(results, key=lambda x: x[1])
points = min_result[1]
points += 1000 if (start[0] + 1, start[1]) in walls else 0
print(points)
# print(f"Path: {path}")
# print(f"Length: {len(path) - 1}")
# print(score[(end)])

# queue = deque([start])
# visited = set()
# visited.add(start)
# steps = {start: 0}
# while queue:
#     x, y = queue.popleft()
#     print(f"Position: {x}, {y}")
#     if (x, y) == end:
#         print(f"Finished in {steps[(x, y)]} steps")
#         break
#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if ((nx, ny) in walls) or ((nx, ny) in visited and steps[(nx, ny)] <= steps[(x, y)] + 1):
#             continue
#         visited.add((nx, ny))
#         queue.append((nx, ny))
#         steps[(nx, ny)] = steps[(x, y)] + 1

# 83480 too low