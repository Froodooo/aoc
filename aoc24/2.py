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

assert part_one("./2.sample") == 2

assert part_one("./2.in") == 359

path = "./2.in"
result_one = part_one(path)
print(result_one)