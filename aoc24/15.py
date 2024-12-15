from utils import *

INPUT_FILE = "./15.in"
SAMPLE_FILE = "./15.sample"

directions = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0)
}

def read_objects(warehouse, object):
    objects = set()
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == object:
                objects.add((x, y))
    return objects

def part_one(path):
    warehouse, moves = read_to_string(path).split("\n\n")
    warehouse = [list(x) for x in warehouse.split("\n")]
    moves = list(moves.replace("\n", ""))

    walls = read_objects(warehouse, "#")
    boxes = read_objects(warehouse, "O")
    rx, ry = read_objects(warehouse, "@").pop()
    for move in moves:
        dx, dy = directions[move]
        xx, yy = rx + dx, ry + dy
        if (xx, yy) in walls:
            continue
        if (xx, yy) in boxes:
            while (xx, yy) in boxes:
                xx += dx
                yy += dy
            if (xx, yy) in walls:
                continue
            boxes.remove((rx + dx, ry + dy))
            boxes.add((xx, yy))
        rx, ry = rx + dx, ry + dy

    return sum([x + y * 100 for x, y in boxes])

assert part_one(SAMPLE_FILE) == 10092
assert part_one(INPUT_FILE) == 1438161

part_one = part_one(INPUT_FILE)
print(part_one)