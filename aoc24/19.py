from utils import *

INPUT_FILE = "./19.in"
SAMPLE_FILE = "./19.sample"

cache = {}

def parse_input(path):
    input = read_to_string(path)
    patterns, designs = input.split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.split("\n")
    return patterns, designs

def count_designs(design, patterns):
    if design in cache:
        return cache[design]
    
    sum = 0
    if not design:
        return 1
    
    for pattern in patterns:
        if design.startswith(pattern):
            sum += count_designs(design[len(pattern):], patterns)

    cache[design] = sum
    return sum

def solve(path, count_total = False):
    global cache
    cache = {}

    patterns, designs = parse_input(path)
    sum = 0
    for design in designs:
        is_valid = count_designs(design, patterns)
        if count_total:
            sum += is_valid
        else:
            sum += 1 if is_valid > 0 else 0
    return sum

def part_one(path):
    return solve(path)

def part_two(path):
    return solve(path, True)


assert part_one(SAMPLE_FILE) == 6
assert part_one(INPUT_FILE) == 315

assert part_two(SAMPLE_FILE) == 16
assert part_two(INPUT_FILE) == 625108891232249

part_one = part_one(INPUT_FILE)
part_two = part_two(INPUT_FILE)
print(part_one, part_two)