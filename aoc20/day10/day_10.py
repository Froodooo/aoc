import copy
from functools import lru_cache


def run_a(input_file):
    adapters = _read(input_file)
    differences = {}

    def _connect_adapters(start):
        if len(adapters) == 0:
            differences[3] += 1
            return differences

        adapter = adapters.pop(0)
        difference = adapter - start

        if difference in differences:
            differences[difference] += 1
        else:
            differences[difference] = 1

        return _connect_adapters(adapter)

    differences = _connect_adapters(0)

    return differences[1] * differences[3]


def run_b(input_file):
    adapters = _read(input_file)
    end = max(adapters)

    @lru_cache
    def _count_configurations(start):
        if start == end:
            return 1

        count = 0
        for step in range(1, 4):
            if start + step not in adapters:
                continue
            count += _count_configurations(start + step)

        return count

    return _count_configurations(0)


def _read(file_name):
    with open(file_name) as f:
        input = [int(line.rstrip()) for line in f]

    return sorted(input)


def run():
    input_file = 'day10/10.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    run()
