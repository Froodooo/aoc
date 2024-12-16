from utils import *
from collections import deque

INPUT_FILE = "./16.in"
SAMPLE_FILE = "./16.sample"

def bfs(start, goal, walls):
    queue = deque([([start], 0)])
    # print(queue.popleft())
    queue_dir = deque([(1, 0)])
    scores = {start: 0}
    results = []
    while queue:
        path, score = queue.popleft()
        # print(path, score)
        pdx, pdy = queue_dir.popleft()
        x, y = path[-1]
        if (x, y) == goal:
            results.append((path, score))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            direction_score = 0 if (dx, dy) == (pdx, pdy) else 1000
            if (nx, ny) not in walls:
                if (nx, ny) not in path:
                    # print(scores)
                    new_score = scores[(x, y)] + direction_score + 1
                    if (nx, ny) in scores and new_score >= scores[(nx, ny)]:
                        continue
                    queue.append((path + [(nx, ny)], score + direction_score + 1))
                    queue_dir.append((dx, dy))
                    scores[(nx, ny)] = scores[(x, y)] + direction_score + 1
    # print(results)
    path = min(results, key=lambda x: x[1])
    for loc in path[0]:
        x, y = loc
        # print(f"({x}, {y}), {score[loc]}")
    return path[1]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

maze = [list(x) for x in read_to_list(SAMPLE_FILE)]

walls = {(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "#"}
start = [(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "S"][0]
end = [(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "E"][0]

result = bfs(start, end, walls)
print(result)

# 83480 too low