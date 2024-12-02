from utils import *


def part_one(path):
  lines = read_to_list(path)
  safe = 0

  for line in lines:
    numbers = [int(number) for number in line.split()]
    increasing = all(i < j and abs(i - j) <= 3 for i, j in zip(numbers, numbers[1:]))
    decreasing = all(i > j and abs(i - j) <= 3 for i, j in zip(numbers, numbers[1:]))
    safe += 1 if (increasing or decreasing) else 0

  return safe

def part_two(path):
  lines = read_to_list(path)
  safe = 0

  for line in lines:
    numbers = [int(number) for number in line.split()]
    increasing = all(i < j and abs(i - j) <= 3 for i, j in zip(numbers, numbers[1:]))
    if increasing:
      safe += 1
      continue
    decreasing = all(i > j and abs(i - j) <= 3 for i, j in zip(numbers, numbers[1:]))
    if decreasing:
      safe += 1
      continue
    
    for i in range(len(numbers)):
      new_numbers = numbers.copy()
      new_numbers.pop(i)
      increasing = all(i < j and abs(i - j) <= 3 for i, j in zip(new_numbers, new_numbers[1:]))
      if increasing:
        safe += 1
        break
      decreasing = all(i > j and abs(i - j) <= 3 for i, j in zip(new_numbers, new_numbers[1:]))
      if decreasing:
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