from utils import *
from re import findall

INPUT_FILE = "./17.in"
SAMPLE_FILE = "./17.sample"

def combo(operand, registers):
    if operand in [0, 1, 2, 3]:
        return operand
    elif operand == 4:
        return registers[0]
    elif operand == 5:
        return registers[1]
    elif operand == 6:
        return registers[2]
    else:
        raise Exception("Invalid operand")

def part_one(path):
    info = read_to_string(path)
    registers, program = info.split("\n\n")
    registers = [int(findall(r'\d+', x)[0]) for x in registers.split("\n")]
    program = [int(x) for x in findall(r'\d+', program)]

    instruction_pointer = 0
    output = []
    while (instruction_pointer < len(program)):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        instruction_pointer += 2
        if opcode == 0: #adv
            registers[0] = registers [0] // pow(2, combo(operand, registers))
        elif opcode == 1:
            registers[1] = registers[1] ^ operand
        elif opcode == 2:
            registers[1] = combo(operand, registers) % 8
        elif opcode == 3:
            if registers[0] != 0:
                instruction_pointer = operand
        elif opcode == 4:
            registers[1] = registers[1] ^ registers[2]
        elif opcode == 5:
            output.append(combo(operand, registers) % 8)
        elif opcode == 6:
            registers[1] = registers [0] // pow(2, combo(operand, registers))
        elif opcode == 7:
            registers[2] = registers [0] // pow(2, combo(operand, registers))

    return ",".join([str(x) for x in output])

assert part_one(SAMPLE_FILE) == "4,6,3,5,6,3,5,2,1,0"
assert part_one(INPUT_FILE) == "2,7,2,5,1,2,7,3,7"

part_one = part_one(INPUT_FILE)
print(part_one)