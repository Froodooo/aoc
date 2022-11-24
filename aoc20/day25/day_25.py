def run_a(input_file):
    [card_public_key, door_public_key] = _read(input_file)
    subject_number = 7

    card_loop_size = _find_loop_size(subject_number, card_public_key)
    # door_loop_size = _find_loop_size(subject_number, door_public_key)

    card_encryption_key = _find_encryption_key(door_public_key, card_loop_size)
    # door_encryption_key = _find_encryption_key(card_public_key, door_loop_size)

    return card_encryption_key


def _find_loop_size(subject_number, public_key):
    loop_size = 0
    value = 1
    while value != public_key:
        value = _get_next_value(value, subject_number)
        loop_size += 1

    return loop_size


def _find_encryption_key(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = _get_next_value(value, subject_number)
    
    return value


def _get_next_value(value, subject_number):
    return (value * subject_number) % 20201227


def _read(file_name):
    with open(file_name) as f:
        input = [int(line) for line in f]

    return input


def solve():
    input_file = 'day25/25.txt'

    result_a = run_a(input_file)
    print(result_a)

    # result_b = run_b(input_file)
    # print(result_b)


if __name__ == '__main__':
    solve()
