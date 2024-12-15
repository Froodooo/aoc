from utils import *

INPUT_FILE = "./15.in"
SAMPLE_FILE = "./15.sample"

directions = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0)
}

def read_objects(warehouse, object, double=False):
    objects = set()
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == object:
                if double:
                    if object == "@":
                        objects.add((x * 2, y))
                    else:
                        objects.add(((x * 2, y), (x * 2 + 1, y)))
                else:
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

def collision(locations, objects):
    collisions = set()
    for obj in objects:
        for location in locations:
            if location in obj:
                collisions.add(obj)
    if len(collisions) == 0:
        return None
    return collisions

def print_warehouse(warehouse, boxes, walls, rx, ry):
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y]) * 2):
            if collision([(x, y)], boxes) != None:
                print("O", end="")
            elif collision([(x, y)], walls) != None:
                print("#", end="")
            elif (x, y) == (rx, ry):
                print("@", end="")
            else:
                print(".", end="")
        print()

warehouse, moves = read_to_string(INPUT_FILE).split("\n\n")
warehouse = [list(x) for x in warehouse.split("\n")]
move_lines = [list(x) for x in moves.split("\n")]

walls = read_objects(warehouse, "#", True)
boxes = read_objects(warehouse, "O", True)
rx, ry = read_objects(warehouse, "@", True).pop()
counter = 0
# print_warehouse(warehouse, boxes, walls, rx, ry)
for move_line in move_lines:
    for move in move_line:
        # print(f"\nMove: {move}, Counter: {counter}")
        dx, dy = directions[move]
        xx, yy = rx + dx, ry + dy
        if collision([(xx, yy)], walls) != None:
            continue
        box_collision = collision([(xx, yy)], boxes)
        if box_collision != None:
            boxes_to_move = set()
            next_check = [(xx, yy)]
            while True:
                box_collision = collision(next_check, boxes)
                # print(f"Box collision: {box_collision}")
                if box_collision == None:
                    break
                boxes_to_move.update(box_collision)
                next_check = []
                for ((x1, y1), (x2, y2)) in box_collision:
                    ((cx1, cy1), (cx2, cy2)) = ((x1, y1), (x2, y2))
                    if x2 < x1:
                        cx1, cx2 = x2, x1
                    if move == ">":
                        next_check.append((cx1 + (dx * 2), cy1 + dy))
                    elif move == "<":
                        next_check.append((cx2 + (dx * 2), cy2 + dy))
                    else:
                        next_check.append((cx1 + (dx * 2), cy1 + dy))
                        next_check.append((cx2 + (dx * 2), cy2 + dy))
                    # next_check.append((x2 + (dx * 2), y2 + dy))
                # print(f"Next check: {next_check}")
            if collision(next_check, walls):
                continue
            # print(f"Boxes to move: {boxes_to_move} to dx {dx} dy {dy}")
            for box in boxes_to_move:
                boxes.remove(box)
            for ((x1, y1), (x2, y2)) in boxes_to_move:
                # print(f"Moving box: {box}")
                # boxes.remove(box)
                # box_parts_moved = set()
                # for box_part in box:
                #     box_parts_moved.add((box_part[0] + dx, box_part[1] + dy))
                # print(f"Box parts moved: {box_parts_moved}")
                ((cx1, cy1), (cx2, cy2)) = ((x1, y1), (x2, y2))
                if x2 < x1:
                    cx1, cx2 = x2, x1
                boxes.add(((cx1 + dx, cy1 + dy), (cx2 + dx, cy2 + dy)))
                # boxes.add(tuple(box_parts_moved))
        rx, ry = rx + dx, ry + dy
        # print_warehouse(warehouse, boxes, walls, rx, ry)
        counter += 1
        # if counter == 225:
        #     break

# print(boxes)
# print_warehouse(warehouse, boxes, walls, rx, ry)
print(sum([x + y * 100 for ((x, y), (_, _)) in boxes]))

# assert part_one(SAMPLE_FILE) == 10092
# assert part_one(INPUT_FILE) == 1438161

# part_one = part_one(INPUT_FILE)
# print(part_one)

# 1404990 too low