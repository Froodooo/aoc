from utils import *

def setup(path):
  input = read_to_list(path)

  return input

def part_one(path):
  input = setup(path)
  
  return 0

# def part_two(path):
#   input = setup(path)
  
#   return 0

assert part_one("./1.sample") == 0
# assert part_two("./1.sample") == 0

assert part_one("./1.in") == 0
# assert part_two("./1.in") == 0

path = "./1.in"
result_one = part_one(path)
# result_two = part_two(path)
print(result_one)