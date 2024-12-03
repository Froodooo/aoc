from utils import *
import re

INPUT_FILE = "./3.in"
SAMPLE_FILE = "./3.sample"

def part_one(path):
  input = read_to_line(path)

  mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
  matches = re.finditer(mul_pattern, input)

  sum = 0
  for match in matches:
    sum += int(match.group(1)) * int(match.group(2))

  return sum

def part_two(path):
  input = read_to_line(path)

  mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)|don\'t\(\)|do\(\)')
  matches = re.finditer(mul_pattern, input)

  enabled = True
  sum = 0
  for match in matches:
    if match.group(0) == "don't()":
      enabled = False
    elif match.group(0) == "do()":
      enabled = True
    else:
      if enabled:
        sum += int(match.group(1)) * int(match.group(2))

  return sum

assert part_one(SAMPLE_FILE) == 161
assert part_two(SAMPLE_FILE) == 48

assert part_one(INPUT_FILE) == 187825547
assert part_two(INPUT_FILE) == 85508223

path = INPUT_FILE
result_one = part_one(path)
result_two = part_two(path)
print(result_one, result_two)