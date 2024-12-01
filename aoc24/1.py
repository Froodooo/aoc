from utils import *

def setup(path):
  input = read_to_list(path)

  list_left = []
  list_right = []

  for numbers in input:
    left, right = numbers.split()
    list_left.append(int(left))
    list_right.append(int(right))

  list_left.sort()
  list_right.sort()

  return list_left, list_right

def part_one(path):
  list_left, list_right = setup(path)
  sum = 0
  for i in range(len(list_left)):
    sum += abs(list_left[i] - list_right[i])

  return sum

def part_two(path):
  list_left, list_right = setup(path)
  sum = 0
  seen = {}
  for number in list_left:
    if number not in seen:
      seen[number] = number * list_right.count(number)
    sum += seen[number]
  
  return sum

assert part_one("./1.sample") == 11
assert part_two("./1.sample") == 31

assert part_one("./1.in") == 2176849
assert part_two("./1.in") == 23384288

path = "./1.in"
result_one = part_one(path)
result_two = part_two(path)
print(result_one, result_two)