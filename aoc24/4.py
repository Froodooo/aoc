from utils import *

INPUT_FILE = "./4.in"
SAMPLE_FILE = "./4.sample"

WORD = list("XMAS")

def rotate(matrix):
  return [list(x) for x in list(zip(*matrix[::-1]))]

def count_diagonal(matrix):
  word_count = 0
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if i + len(WORD) <= len(matrix) and j + len(WORD) <= len(matrix[i]):
        word = []
        for k in range(len(WORD)):
          word.append(matrix[i+k][j+k])
        if word == WORD:
          word_count += 1
      if i - len(WORD) >= -1 and j - len(WORD) >= -1:
        word = []
        for k in range(len(WORD)):
          word.append(matrix[i-k][j-k])
        if word == WORD:
          word_count += 1
      if i + len(WORD) <= len(matrix) and j - len(WORD) >= -1:
        word = []
        for k in range(len(WORD)):
          word.append(matrix[i+k][j-k])
        if word == WORD:
          word_count += 1
      if i - len(WORD) >= -1 and j + len(WORD) <= len(matrix[i]):
        word = []
        for k in range(len(WORD)):
          word.append(matrix[i-k][j+k])
        if word == WORD:
          word_count += 1
  return word_count

def count_horizontal(line):
  word_count = 0
  for i in range(len(line)):
    if line[i:i+len(WORD)] == WORD:
      word_count += 1
  return word_count

def count_line(line):
  return count_horizontal(line)

def read_input(path):
  input = read_to_list(path)
  return [list(x) for x in input]

def part_one(path):
  matrix = read_input(path)
  word_count = 0
  for i in range(4):
    for line in matrix:
      word_count += count_line(line)
    matrix = rotate(matrix)
  word_count += count_diagonal(matrix)

  return word_count

def part_two(path):
  matrix = read_input(path)

  word_count = 0
  for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[i]) - 1):
      if matrix[i][j] == "A":
        cross = matrix[i-1][j-1] + matrix[i-1][j+1] + matrix[i+1][j-1] + matrix[i+1][j+1]
        if cross in ["MSMS", "MMSS", "SSMM", "SMSM"]:
          word_count += 1

  return word_count
            
assert part_one(SAMPLE_FILE) == 18
assert part_two(SAMPLE_FILE) == 9

assert part_one(INPUT_FILE) == 2633
assert part_two(INPUT_FILE) == 1936

path = INPUT_FILE
result_one = part_one(path)
result_two = part_two(path)
print(result_one, result_two)