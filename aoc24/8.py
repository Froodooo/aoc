from utils import *

INPUT_FILE = "./8.in"
SAMPLE_FILE = "./8.sample"

def get_antennas(rooftop):
  antennas = {}
  for y in range(len(rooftop)):
    for x in range(len(rooftop[y])):
      frequency = rooftop[y][x]
      if frequency != ".":
        if frequency not in antennas:
          antennas[frequency] = []
        antennas[frequency].append((y, x))
  return antennas

def get_antinodes(antenna1, antenna2, rooftop, resonant=False):
  (y1, x1) = antenna1
  (y2, x2) = antenna2

  resonance_level = 1
  resume = True
  antinodes = set()

  if resonant:
    antinodes.add(antenna1)
    antinodes.add(antenna2)

  while resume:
    antinodes_length = len(antinodes)
    
    (a1y, a1x) = ((y1 + ((y1 - y2) * resonance_level)), (x1 + ((x1 - x2) * resonance_level)))
    (a2y, a2x) = ((y2 + ((y2 - y1) * resonance_level)), (x2 + ((x2 - x1) * resonance_level)))
    
    if a1y >= 0 and a1y < len(rooftop) and a1x >= 0 and a1x < len(rooftop[0]): antinodes.add((a1y, a1x))
    if a2y >= 0 and a2y < len(rooftop) and a2x >= 0 and a2x < len(rooftop[0]): antinodes.add((a2y, a2x))

    if resonant and len(antinodes) > antinodes_length:
      resonance_level += 1
    else:
      resume = False

  return antinodes

def get_all_antinodes(rooftop, antennas, resonant=False):
  antinodes = set()
  for positions in antennas.values():
    pairs = [(a, b) for idx, a in enumerate(positions) for b in positions[idx + 1:]]
    for (antenna1, antenna2) in pairs:
      antinodes = antinodes.union(get_antinodes(antenna1, antenna2, rooftop, resonant))
  return antinodes

def part_one(path):
  rooftop = [list(x) for x in read_to_list(path)]
  antennas = get_antennas(rooftop)
  antinodes = get_all_antinodes(rooftop, antennas)
  return len(antinodes)

def part_two(path):
  rooftop = [list(x) for x in read_to_list(path)]
  antennas = get_antennas(rooftop)
  antinodes = get_all_antinodes(rooftop, antennas, True)
  return len(antinodes)


assert part_one(SAMPLE_FILE) == 14
assert part_two(SAMPLE_FILE) == 34

assert part_one(INPUT_FILE) == 392
assert part_two(INPUT_FILE) == 1235

path = INPUT_FILE
result_one = part_one(path)
result_two = part_two(path)
print(result_one, result_two)