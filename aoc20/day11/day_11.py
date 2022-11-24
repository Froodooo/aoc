from copy import deepcopy
from time import time

ADJACENTS = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
             (0, 1), (1, -1), (1, 0), (1, 1)]

EMPTY_CHAIR = 'L'
OCCUPIED_CHAIR = '#'
FLOOR = '.'


def run_a(input_file):
    options = {'part': 'a', 'occupied_count': 4}
    return _run(input_file, options)


def run_b(input_file):
    options = {'part': 'b', 'occupied_count': 5}
    return _run(input_file, options)


def _run(input_file, options):
    seats = _read(input_file)
    changed = True

    while changed:
        seats, changed = _round(seats, options)

    return _occupied(seats)


def _round(seats, options):
    rows, cols = len(seats), len(seats[0])
    seats_copy = deepcopy(seats)
    changed = False

    for row in range(rows):
        for col in range(cols):
            adjacent_seats = _adjacent_seats(row, col, seats, options)
            new_seat = seats[row][col]
            if new_seat == EMPTY_CHAIR and OCCUPIED_CHAIR not in adjacent_seats:
                new_seat = OCCUPIED_CHAIR
                changed = True
            elif new_seat == OCCUPIED_CHAIR and adjacent_seats.count(OCCUPIED_CHAIR) >= options['occupied_count']:
                new_seat = EMPTY_CHAIR
                changed = True

            seats_copy[row][col] = new_seat

    return seats_copy, changed


def _adjacent_seats(row, col, seats, options):
    adjacent_seats = []
    rows, cols = len(seats), len(seats[0])

    for adjacent_row, adjacent_col in ADJACENTS:
        row_delta = row + adjacent_col
        col_delta = col + adjacent_row

        if options['part'] == 'b':
            row_delta, col_delta = _indirect_adjacent_seat_position(
                row_delta, col_delta, adjacent_row, adjacent_col, seats)

        if 0 <= row_delta < rows and 0 <= col_delta < cols:
            adjacent_seats.append(seats[row_delta][col_delta])

    return adjacent_seats


def _indirect_adjacent_seat_position(row, col, adjacent_row, adjacent_col, seats):
    while _seat_is_floor(row, col, seats):
        row += adjacent_col
        col += adjacent_row

    return row, col


def _seat_is_floor(row, col, seats):
    rows, cols = len(seats), len(seats[0])

    return 0 <= row < rows and 0 <= col < cols and seats[row][col] == FLOOR


def _occupied(seats):
    occupied = 0
    for row in seats:
        for seat in row:
            if seat == OCCUPIED_CHAIR:
                occupied += 1

    return occupied


def _read(file_name):
    with open(file_name) as f:
        input = [list(line.rstrip()) for line in f]

    return input


def solve():
    input_file = 'day11/11.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
