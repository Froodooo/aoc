def run_a(input_file):
    input = _read(input_file)

    return input.count('(') - input.count(')')


def run_b(input_file):
    input = _read(input_file)
    floor = 0
    for index, instruction in enumerate(input):
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1

        if floor == -1:
            return index + 1


def _read(file_name):
    with open(file_name) as f:
        input = list(f.read())
    return input


def run():
    input_file = 'input/1.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    run()
