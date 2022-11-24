def run_b(input_file):
    active_space = _read(input_file)

    rounds = 6
    loops = 10
    for _ in range(6):
        active_space = _cycle(active_space, loops)

    return len(active_space)


def _cycle(active_space, loops):
    print(len(active_space))
    new_active_space = set()
    for x in range(-15, 15):
        for y in range(-15, 15):
            for z in range(-8, 8):
                for w in range(-8, 8):
                    active_neighbours = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):
                                for dw in range(-1, 2):
                                    if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                                        position = (x+dx, y+dy, z+dz, w+dw)
                                        if position in active_space:
                                            active_neighbours += 1
                    position = (x, y, z, w)
                    if position not in active_space and active_neighbours == 3:
                        new_active_space.add(position)
                    elif position in active_space and active_neighbours in [2, 3]:
                        new_active_space.add(position)

    return new_active_space


def _read(file_name):
    active_space = set()
    with open(file_name) as f:
        input = [[cube for cube in line.rstrip()] for line in f]
        for row, y in enumerate(input):
            for col, char in enumerate(y):
                if char == '#':
                    active_space.add((row, col, 0, 0))

    return active_space


def solve():
    input_file = 'day17/17.txt'

    # result_a = run_a(input_file)
    # print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
