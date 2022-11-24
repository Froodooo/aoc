from math import prod


def run_a(input_file):
    input = _read(input_file)
    timestamp = input['timestamp']
    bus_ids = [int(bus_id) for bus_id in input['bus_ids'] if bus_id != 'x']

    bus_mods = {}
    for bus_id in bus_ids:
        previous_iteration = timestamp // bus_id
        next_timestamp = bus_id * (previous_iteration + 1)
        next_bus_in = next_timestamp - timestamp
        bus_mods[bus_id] = next_bus_in

    sorted_bus_mods = dict(sorted(bus_mods.items(), key=lambda item: item[1]))
    first_bus = list(sorted_bus_mods.keys())[0]
    first_bus_in = sorted_bus_mods[first_bus]

    return first_bus * first_bus_in


def run_b(input_file):
    input = _read(input_file)

    # Chinese remainder theorem
    # https://www.geeksforgeeks.org/chinese-remainder-theorem-set-2-implementation/
    bus_ids = [int(bus_id) for bus_id in input['bus_ids'] if bus_id != 'x']
    bus_remainders = [int(bus_id) - index for index,
                      bus_id in enumerate(input['bus_ids']) if bus_id != 'x']

    bus_ids_prod = prod(bus_ids)
    result = 0

    for bus_id, bus_remainder in zip(bus_ids, bus_remainders):
        pp = bus_ids_prod // bus_id
        result += bus_remainder * pp * pow(pp, -1, bus_id)

    return result % bus_ids_prod


def _read(file_name):
    input = {}
    with open(file_name) as f:
        input['timestamp'] = int(f.readline())
        input['bus_ids'] = f.readline().split(',')

    return input


def solve():
    input_file = 'day13/13.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
