from utils import *
from collections import deque

INPUT_FILE = "./16.in"
SAMPLE_FILE = "./16.sample"

def bfs(start, goal, walls):
    sx, sy = start
    queue = deque([([[(sx, sy, (1, 0))], 0])])
    # print(queue.popleft())
    scores = {start: 0}
    results = []
    while queue:
        path, score = queue.popleft()
        # print(path)
        # print(path, score)
        # pdx, pdy = queue_dir.popleft()
        x, y, dir = path[-1]
        if (x, y) == goal:
            results.append((path, score))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            direction_score = 0 if (dx, dy) == dir else 1000
            if (nx, ny) not in walls and (nx, ny, dir) not in path:
                # print(scores)
                if (nx, ny) in scores:
                    new_score = scores[(x, y)] + direction_score + 1
                    if new_score > scores[(nx, ny)]:
                        continue
                queue.append((path + [(nx, ny, (dx, dy))], score + direction_score + 1))
                scores[(nx, ny)] = scores[(x, y)] + direction_score + 1
    print([x[1] for x in results])
    path = min(results, key=lambda x: x[1])
    for loc in path[0]:
        x, y, _ = loc
        # print(f"({x}, {y}), {score[loc]}")
    return path[1]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

maze = [list(x) for x in read_to_list(INPUT_FILE)]

walls = {(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "#"}
start = [(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "S"][0]
end = [(x, y) for y in range(len(maze)) for x in range(len(maze[y])) if maze[y][x] == "E"][0]

result = bfs(start, end, walls)
print(result)

# 83480 too low
# 85480 correct