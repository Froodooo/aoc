from utils import *
from collections import deque

INPUT_FILE = "./11.in"
SAMPLE_FILE = "./11.sample"

def blink(stones):
    for _ in range(len(stones)):
        stone = stones.popleft()
        if stone == 0:
            stones.append(1)
        elif len(str(stone)) % 2 == 0:
            digits = len(str(stone))
            half = 10 ** (digits // 2)
            left = stone // half
            right = stone % half
            stones.append(left)
            stones.append(right)
        else:
            stones.append(stone * 2024)

stones = deque(int(x) for x in read_to_line(SAMPLE_FILE).split())
print(stones)

for i in range(75):
    print(i + 1)
    blink(stones)

print(len(stones))