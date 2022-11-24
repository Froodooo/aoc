def run_a(input_file):
    return _run(input_file, 2020)


def run_b(input_file):
    return _run(input_file, 30000000)


def _run(input_file, max_turns):
    numbers = _read(input_file)

    state = {}
    turns = len(numbers)
    previous = numbers[-1]

    for turn, number in enumerate(numbers[:-1]):
        state[number] = turn + 1

    while turns < max_turns:
        new = turns - state[previous] if previous in state else 0
        state[previous] = turns
        turns += 1
        previous = new

    return previous


def _read(file_name):
    input = {}
    with open(file_name) as f:
        input = [int(number) for number in f.readline().split(',')]

    return input


def solve():
    input_file = 'day15/15.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
