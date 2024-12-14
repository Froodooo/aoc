from utils import *
from math import prod

INPUT_FILE = "./14.in"
SAMPLE_FILE = "./14.sample"

def print_grid(positions, x_width, y_width):
    for i in range(y_width):
        for j in range(x_width):
            if (j, i) in positions:
                print(positions.count((j, i)), end="")
            else:
                print(".", end="")
        print()

def parse_robot(line):
    position, velocity = line.split(" ")
    pos_x, pos_y = [int(x) for x in position.replace("p=", "").split(",")]
    vel_x, vel_y = [int(x) for x in velocity.replace("v=", "").split(",")]
    return (pos_x, pos_y), (vel_x, vel_y)

def count_quadrants(positions, x_width, y_width):
    quadrants = [0, 0, 0, 0]
    for (x, y) in positions:
        # top left
        if x < x_width // 2 and y < y_width // 2:
            quadrants[0] += 1
        # top right
        elif x > x_width // 2 and y < y_width // 2:
            quadrants[1] += 1
        # bottom left
        elif x < x_width // 2 and y > y_width // 2:
            quadrants[2] += 1
        # bottom right
        elif x > x_width // 2 and y > y_width // 2:
            quadrants[3] += 1
    return quadrants

def part_one(path, x_width, y_width):
    input = read_to_list(path)
    positions = []
    for line in input:
        (pos_x, pos_y), (vel_x, vel_y) = parse_robot(line)
        for i in range(100):
            pos_x = (pos_x + vel_x) % x_width
            pos_y = (pos_y + vel_y) % y_width
        positions.append((pos_x, pos_y))
    quadrands = count_quadrants(positions, x_width, y_width)
    return prod(quadrands)

def part_two(path, x_width, y_width):
    input = read_to_list(path)
    total = len(input)
    seen = set()
    counter = 0
    while (len(seen) != total): # assuming all robots are at a different position means they form a christmas tree picture
        counter += 1
        seen = set()
        for line in input:
            (pos_x, pos_y), (vel_x, vel_y) = parse_robot(line)
            pos_x = (pos_x + vel_x * counter) % x_width
            pos_y = (pos_y + vel_y * counter) % y_width
            seen.add((pos_x, pos_y))
    print_grid(list(seen), x_width, y_width)
    return counter

assert part_one(SAMPLE_FILE, 11, 7) == 12
assert part_one(INPUT_FILE, 101, 103) == 217328832

assert part_two(INPUT_FILE, 101, 103) == 7412

part_one = part_one(INPUT_FILE, 101, 103)
part_two = part_two(INPUT_FILE, 101, 103)
print(part_one, part_two)