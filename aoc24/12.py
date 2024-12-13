from utils import *

INPUT_FILE = "./12.in"
SAMPLE_FILE = "./12.sample"

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
seen = set()
area = set()
sides = {}
sides_count = 0

def find_area(x, y, plot, garden):
    global seen

    if x < 0 or y < 0 or x >= len(garden[0]) or y >= len(garden): return
    if (x, y) in area: return
    if garden[y][x] != plot: return
    area.add((x, y))
    seen.add((x, y))
    for dx, dy in directions:
        find_area(x + dx, y + dy, plot, garden)
  
def find_perimeter(area):
    perimeter = 0
    for x, y in area:
        for dx, dy in directions:
            if (x + dx, y + dy) not in area:
                perimeter += 1
    return perimeter

def find_sides(area):
    global sides_count

    for x, y in area:
        for dx, dy in directions:
            if (x + dx, y + dy) not in area:
                if (dx in [-1, 1]):
                    sides[('x', x, dx)] = sides.get(('x', x, dx), []) + [y]
                if (dy in [-1, 1]):
                    sides[('y', y, dy)] = sides.get(('y', y, dy), []) + [x]
    for values in sides.values():
        values.sort()
        sides_count += 1
        for i in range(1, len(values)):
            if values[i] - values[i - 1] > 1:
                sides_count += 1
        

def solve(path):
  global area
  global sides
  global sides_count
  global seen

  garden = [list(x) for x in read_to_list(path)]

  seen = set()
  price = 0
  price_discount = 0
  for y in range(len(garden)):
      for x in range(len(garden[y])):
          if (x, y) in seen: continue
          area = set()
          sides = {}
          sides_count = 0
          plot = garden[y][x]
          find_area(x, y, plot, garden)
          perimeter = find_perimeter(area)
          find_sides(area)
          price += len(area) * perimeter
          price_discount += len(area) * sides_count
  return price, price_discount

price, price_discount = solve(SAMPLE_FILE)
assert price == 1930
assert price_discount == 1206

price, price_discount = solve(INPUT_FILE)
assert price == 1465112
assert price_discount == 893790

print(price, price_discount)