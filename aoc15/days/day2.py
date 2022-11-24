from functools import reduce
import operator


def run_a(input_file):
    input = _read(input_file)

    total_surface = 0
    for dimensions in input:
        sides = _sides(dimensions)
        total_surface += sum([side * 2 for side in sides]) + min(sides)

    return total_surface


def run_b(input_file):
    input = _read(input_file)

    total_length = 0
    for dimensions in input:
        total_length += _length(dimensions) + reduce(operator.mul, dimensions)

    return total_length


def _sides(dimensions):
    l, w, h = dimensions
    return [l*w, w*h, h*l]


def _length(dimensions):
    dimensions.sort()
    return sum([dimension * 2 for dimension in dimensions[:2]])


def _read(file_name):
    with open(file_name) as f:
        input = [
            [int(dimension) for dimension in line.rstrip().split('x')]
            for line in f
        ]
    return input


def run():
    input_file = 'input/2.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    run()
