from utils import *

INPUT_FILE = "./11.in"
SAMPLE_FILE = "./11.sample"

def split_stone(stone):
    digits = len(str(stone))
    half = 10 ** (digits // 2)
    left = stone // half
    right = stone % half
    return left, right

def blink(stones):
    stones_copy = dict(stones)
    for stone in stones_copy.keys():
        stone_value = stones_copy[stone]
        stones[stone] -= stone_value   
        if stone == 0:
            stones[1] = stones.get(1, 0) + stone_value
        elif len(str(stone)) % 2 == 0:
            left, right = split_stone(stone)
            stones[left] = stones.get(left, 0) + stone_value
            stones[right] = stones.get(right, 0) + stone_value
        else:
            stones[stone * 2024] = stones.get(stone * 2024, 0) + stone_value          
    return stones

def solve(path, iterations):
    stones = {int(x): 1 for x in read_to_line(path).split()}
    for i in range(iterations):
        stones = blink(stones)
    return sum(stones.values())

def part_one(path):
    return solve(path, 25)

def part_two(path):
    return solve(path, 75)


assert part_one(SAMPLE_FILE) == 55312
# assert part_two(SAMPLE_FILE) == 240954878211138

assert part_one(INPUT_FILE) == 203609
assert part_two(INPUT_FILE) == 240954878211138

path = INPUT_FILE
result_one = part_one(path)
result_two = part_two(path)
print(result_one, result_two)