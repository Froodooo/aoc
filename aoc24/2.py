from utils import *

INPUT_FILE = "./2.in"
SAMPLE_FILE = "./2.sample"

MAX_GAP = 3

def is_safe_increasing(numbers, max_gap):
  return all(i < j and abs(i - j) <= max_gap for i, j in zip(numbers, numbers[1:]))

def is_safe_decreasing(numbers, max_gap):
  return all(i > j and abs(i - j) <= max_gap for i, j in zip(numbers, numbers[1:]))

def is_safe(numbers):
  return True if is_safe_increasing(numbers, MAX_GAP) else is_safe_decreasing(numbers, MAX_GAP)

def part_one(path):
  lines = read_to_list(path)
  safe = 0

  for line in lines:
    numbers = [int(number) for number in line.split()]
    safe += 1 if is_safe(numbers) else 0

  return safe

def part_two(path):
  lines = read_to_list(path)
  safe = 0

  for line in lines:
    numbers = [int(number) for number in line.split()]
    if (is_safe(numbers)):
      safe += 1
      continue
    
    for i in range(len(numbers)):
      new_numbers = numbers.copy()
      new_numbers.pop(i)
      if (is_safe(new_numbers)):
        safe += 1
        break

  return safe

assert part_one(SAMPLE_FILE) == 2
assert part_two(SAMPLE_FILE) == 4

assert part_one(INPUT_FILE) == 359
assert part_two(INPUT_FILE) == 418

path = INPUT_FILE
result_one = part_one(path)
result_two = part_two(path)
print(result_one, result_two)