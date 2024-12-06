from utils import *

INPUT_FILE = "./6.in"
SAMPLE_FILE = "./6.sample"

directions = {
  'U': (0, -1),
  'D': (0, 1),
  'L': (-1, 0),
  'R': (1, 0)
}

turn = {
  'U': 'R',
  'D': 'L',
  'L': 'U',
  'R': 'D'
}

obstacle = {
  'U': 'L',
  'D': 'R',
  'L': 'D',
  'R': 'U'
}

def get_start(map):
  for i in range(len(map)):
      for j in range(len(map[i])):
          if map[i][j] == '^':
              return (i, j)

def part_one(path):
  map = [list(x) for x  in read_to_list(path)]
  (pos_y, pos_x) = get_start(map)
  (dir_x, dir_y) = directions['U']
  direction = 'U'
  path = set()
  path.add((pos_x, pos_y))

  while pos_x + dir_x >= 0 and pos_x + dir_x < len(map) and pos_y + dir_y >= 0 and pos_y + dir_y < len(map[pos_x]):
    while map[pos_y + dir_y][pos_x + dir_x] == "#":
      direction = turn[direction]
      (dir_x, dir_y) = directions[direction]
    pos_x += dir_x
    pos_y += dir_y
    path.add((pos_x, pos_y))

  print(len(path))

map = [list(x) for x  in read_to_list(SAMPLE_FILE)]
(pos_y, pos_x) = get_start(map)
(dir_x, dir_y) = directions['U']
direction = 'U'
path = set()
obstructions = set()
path.add((pos_x, pos_y, direction))

while pos_x + dir_x >= 0 and pos_x + dir_x < len(map) and pos_y + dir_y >= 0 and pos_y + dir_y < len(map[pos_x]):
  if any(x == pos_x and y == pos_y for (x, y, direction) in path):
     print("Found obstruction at: ", pos_x, pos_y)
  while map[pos_y + dir_y][pos_x + dir_x] == "#":
    direction = turn[direction]
    (dir_x, dir_y) = directions[direction]
  pos_x += dir_x
  pos_y += dir_y
  path.add((pos_x, pos_y, direction))

print(len(path))