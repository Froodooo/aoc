from utils import *

INPUT_FILE = "./10.in"
SAMPLE_FILE = "./10.sample"

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

nine_heights = set()
total = 0

def get_trails(x, y, prev, map):
    global trails
    global total

    if prev == 8 and map[y][x] == 9:
        nine_heights.add((x, y))
        total += 1
    prev = map[y][x]
    for direction in directions:
        xx = x + direction[1]
        yy = y + direction[0]
        if xx >= 0 and xx < len(map[0]) and yy >= 0 and yy < len(map):
          if map[yy][xx] == prev + 1:
              get_trails(xx, yy, map[y][x], map)

def solve(path, p1=True):
    global nine_heights
    global total

    nine_heights.clear()
    total = 0

    map = [[int(y) for y in list(x)] for x in read_to_list(path)]
    total_trails = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                get_trails(x, y, 0, map)
                total_trails += len(nine_heights)
                nine_heights.clear()
    
    return total_trails if p1 else total


assert solve(SAMPLE_FILE) == 36
assert solve(SAMPLE_FILE, False) == 81

assert solve(INPUT_FILE) == 496
assert solve(INPUT_FILE, False) == 1120

path = INPUT_FILE
result_one = solve(path)
result_two = solve(path, False)
print(result_one, result_two)