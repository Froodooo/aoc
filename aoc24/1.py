from utils import *

input = read_to_list("./1.in")

list_left = []
list_right = []

for numbers in input:
  left, right = numbers.split()
  list_left.append(int(left))
  list_right.append(int(right))

list_left.sort()
list_right.sort()

def part_one():
  sum = 0
  for i in range(len(list_left)):
    sum += abs(list_left[i] - list_right[i])

  print(sum)

def part_two():
  sum = 0
  for number in list_left:
    sum += number * list_right.count(number)
  
  print(sum)

part_one()
part_two()