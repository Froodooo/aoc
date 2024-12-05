from utils import *

INPUT_FILE = "./5.in"
SAMPLE_FILE = "./5.sample"

input = read_to_string(INPUT_FILE)
ordering_rules, updates = input.split("\n\n")
ordering_rules = list(map(lambda x: [int(y) for y in x.split("|")], ordering_rules.splitlines()))
ordering_rules_dict = {}
for rule in ordering_rules:
    if rule[0] not in ordering_rules_dict:
        ordering_rules_dict[rule[0]] = []
    ordering_rules_dict[rule[0]].append(rule[1])
updates = [list(map(int, x.split(','))) for x in updates.splitlines()]

sum = 0
for update in updates:
    valid = True
    for i, page in enumerate(update):
       if any(page in ordering_rules_dict[x] for x in update[i:] if x in ordering_rules_dict):
           valid = False
           break
    if valid:
        sum += update[int(len(update) / 2)]
print(sum)