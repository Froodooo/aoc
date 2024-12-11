from utils import *
from collections.abc import Iterable

INPUT_FILE = "./11.in"
SAMPLE_FILE = "./11.sample"

stones = [int(x) for x in read_to_line(INPUT_FILE).split()]

def blink(stones):
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == 0:
            new_stones.append(1)
        elif len(str(stones[i])) % 2 == 0:
            string_stone = str(stones[i])
            left = string_stone[:len(string_stone) // 2]
            right = string_stone[len(string_stone) // 2:]
            new_stones.append(int(left))
            new_stones.append(int(right))
        else:
            new_stones.append(stones[i] * 2024)
    return new_stones

for _ in range(75):
    stones = blink(stones)
    # print(stones)
print(len(stones))