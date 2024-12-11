from utils import *

INPUT_FILE = "./11.in"
SAMPLE_FILE = "./11.sample"

def blink(stones):
    stones_copy = dict(stones)
    current_stones = list(stones.keys())
    for stone in current_stones:
        stone_count = stones_copy[stone]
        stones[stone] -= stones_copy[stone]
            
        if stone == 0:
            if stones.get(1) is None:
                stones[1] = 0
            stones[1] += stone_count
        elif len(str(stone)) % 2 == 0:
            digits = len(str(stone))
            half = 10 ** (digits // 2)
            left = stone // half
            right = stone % half
            if stones.get(left) is None:
                stones[left] = 0
            stones[left] += stone_count
            if stones.get(right) is None:
                stones[right] = 0
            stones[right] += stone_count
        else:
            if stones.get(stone * 2024) is None:
                stones[stone * 2024] = 0
            stones[stone * 2024] += stone_count
    return stones

def part_one(path):
    stones = {int(x): 1 for x in read_to_line(path).split()}
    for i in range(25):
        stones = blink(stones)
    return sum(stones.values())

def part_two(path):
    stones = {int(x): 1 for x in read_to_line(path).split()}
    for i in range(75):
        stones = blink(stones)
    return sum(stones.values())


assert part_one(SAMPLE_FILE) == 55312
# assert part_two(SAMPLE_FILE) == 81

assert part_one(INPUT_FILE) == 203609
assert part_two(INPUT_FILE) == 240954878211138

path = INPUT_FILE
result_one = part_one(path)
result_two = part_two(path)
print(result_one, result_two)