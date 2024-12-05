from utils import *
from functools import cmp_to_key

INPUT_FILE = "./5.in"
SAMPLE_FILE = "./5.sample"

def setup(path):
    ordering_rules, updates = read_to_string(path).split("\n\n")
    ordering_rules = list(map(lambda x: [int(y) for y in x.split("|")], ordering_rules.splitlines()))
    ordering_rules_dict = {}
    for rule in ordering_rules:
        if rule[0] not in ordering_rules_dict:
            ordering_rules_dict[rule[0]] = []
        ordering_rules_dict[rule[0]].append(rule[1])
    updates = [list(map(int, x.split(','))) for x in updates.splitlines()]
    return updates, ordering_rules_dict

def is_valid_update(update, ordering_rules_dict):
    for i, page in enumerate(update):
        if any(page in ordering_rules_dict[x] for x in update[i:] if x in ordering_rules_dict):
            return False
    return True

def page_sort(x, y, ordering_rules_dict):
    return 1 if x in ordering_rules_dict and y in ordering_rules_dict[x] else -1

def part_one(path):
    updates, ordering_rules_dict = setup(path)
    sum = 0
    for update in updates:
        if(is_valid_update(update, ordering_rules_dict)):
            sum += update[int(len(update) / 2)]
    return sum

def part_two(path):
    updates, ordering_rules_dict = setup(path)
    sum = 0
    for update in updates:
        if(not is_valid_update(update, ordering_rules_dict)):
            update.sort(key=cmp_to_key(lambda x, y: page_sort(x, y, ordering_rules_dict)))
            sum += update[int(len(update) / 2)]
    return sum


assert part_one(SAMPLE_FILE) == 143
assert part_two(SAMPLE_FILE) == 123

assert part_one(INPUT_FILE) == 6384
assert part_two(INPUT_FILE) == 5353

path = INPUT_FILE
result_one = part_one(path)
result_two = part_two(path)
print(result_one, result_two)