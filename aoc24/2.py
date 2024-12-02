from utils import *

def is_safe(numbers):
  increasing = all(i < j and abs(i - j) <= 3 for i, j in zip(numbers, numbers[1:]))
  decreasing = all(i > j and abs(i - j) <= 3 for i, j in zip(numbers, numbers[1:]))
  return increasing or decreasing

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

assert part_one("./2.sample") == 2
assert part_two("./2.sample") == 4

assert part_one("./2.in") == 359
assert part_two("./2.in") == 418

path = "./2.in"
result_one = part_one(path)
result_two = part_two(path)
print(result_one, result_two)