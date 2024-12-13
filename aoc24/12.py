from utils import *

INPUT_FILE = "./12.in"
SAMPLE_FILE = "./12.sample"

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
garden = [list(x) for x in read_to_list(INPUT_FILE)]
seen = set()
area = set()

def find_area(x, y):
    global seen

    if x < 0 or y < 0 or x >= len(garden[0]) or y >= len(garden): return
    if (x, y) in area: return
    if garden[y][x] != plot: return
    area.add((x, y))
    seen.add((x, y))
    for dx, dy in directions:
        find_area(x + dx, y + dy)
  
def find_perimeter(area):
    perimeter = 0
    for x, y in area:
        for dx, dy in directions:
            if (x + dx, y + dy) not in area:
                perimeter += 1
    return perimeter

price = 0
for y in range(len(garden)):
    for x in range(len(garden[y])):
        if (x, y) in seen: continue
        area = set()
        plot = garden[y][x]
        find_area(x, y)
        perimeter = find_perimeter(area)
        price += len(area) * perimeter
        # print(garden[y][x], len(area), perimeter, area)
print(price)