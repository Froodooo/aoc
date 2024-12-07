from utils import *
from itertools import product

INPUT_FILE = "./7.in"
SAMPLE_FILE = "./7.sample"

def read_input(path):
  return [[int(x[0]), list(map(int, x[1].split()))] for x in (line.split(": ") for line in read_to_list(path))]

def calculate_operator_sequence_result(operator_sequence, equation, test_value):
  test_result = equation[0]

  for i, operator in enumerate(operator_sequence):
    if operator == '+':
      test_result += equation[i+1]
    elif operator == '*':
      test_result *= equation[i+1]
    elif operator == '|':
      test_result = int(f"{test_result}{equation[i+1]}")
    if test_result > test_value:
      break

  return test_result

def calculate_calibrated_result(input, operators):
  calibration_result = 0

  for test_value, equation in input:
    operator_sequences = [list(sequence) for sequence in product(operators, repeat=(len(equation))-1)]
    for operator_sequence in operator_sequences:
      test_result = calculate_operator_sequence_result(operator_sequence, equation, test_value)
      if test_result == test_value:
        calibration_result += test_result
        break

  return calibration_result

def part_one(path):
  return calculate_calibrated_result(read_input(path), "*+")

def part_two(path):
  return calculate_calibrated_result(read_input(path), "*+|")


assert part_one(SAMPLE_FILE) == 3749
assert part_two(SAMPLE_FILE) == 11387

assert part_one(INPUT_FILE) == 2501605301465
assert part_two(INPUT_FILE) == 44841372855953

path = INPUT_FILE
result_one = part_one(path)
result_two = part_two(path)
print(result_one, result_one)