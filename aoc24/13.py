from utils import *
from collections import deque

INPUT_FILE = "./13.in"
SAMPLE_FILE = "./13.sample"

def parse_machine(machine):
    button_a, button_b, prize = machine.split("\n")
    button_ax, button_ay = button_a.split(": ")[1].split(",")
    button_ax = int(button_ax.replace("X+", ""))
    button_ay = int(button_ay.replace("Y+", ""))
    button_bx, button_by = button_b.split(": ")[1].split(",")
    button_bx = int(button_bx.replace("X+", ""))
    button_by = int(button_by.replace("Y+", ""))
    prize_x, prize_y = prize.split(": ")[1].split(", ")
    prize_x = int(prize_x.replace("X=", ""))
    prize_y = int(prize_y.replace("Y=", ""))
    return button_ax, button_ay, button_bx, button_by, prize_x, prize_y

def get_pushes(parsed_machine):
    button_ax, button_ay, button_bx, button_by, prize_x, prize_y = parsed_machine
    queue = deque([(0, 0)])
    seen = set()
    while queue:
        press_a, press_b = queue.popleft()
        if (press_a, press_b) in seen:
            continue
        seen.add((press_a, press_b))
        # print(press_a, press_b)
        value_x = press_a * button_ax + press_b * button_bx
        value_y = press_a * button_ay + press_b * button_by
        if value_x == prize_x and value_y == prize_y:
            return press_a, press_b
        if press_a > 100 or press_b > 100:
            continue
        if value_x > prize_x or value_y > prize_y:
            continue

        queue.append((press_a+1, press_b))
        queue.append((press_a, press_b+1))
    return None

input = read_to_string(INPUT_FILE)
machines = input.split("\n\n")
sum = 0
for i, machine in enumerate(machines):
    # print(i+1)
    parsed_machine = parse_machine(machine)
    pushes = get_pushes(parsed_machine)
    if pushes:
        press_a, press_b = pushes
        sum += press_a * 3 + press_b
print(sum)