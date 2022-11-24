import math

DIRECTIONS = ['N', 'E', 'S', 'W']
TURNS = ['L', 'R']


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, action, value):
        if action == 'N':
            self.y += value
        elif action == 'E':
            self.x += value
        elif action == 'S':
            self.y -= value
        elif action == 'W':
            self.x -= value

    def waypoint(self, value, waypoint):
        self.x += waypoint.x * value
        self.y += waypoint.y * value

    def rotate(self, action, value):
        # https://gist.github.com/LyleScott/e36e08bfb23b1f87af68c9051f985302
        sign = -1 if action == 'L' else 1
        radians = math.radians(sign * value)

        x = round(self.x * math.cos(radians) + self.y * math.sin(radians))
        y = round(-self.x * math.sin(radians) + self.y * math.cos(radians))

        self.x = x
        self.y = y

    def manhattan(self):
        return abs(self.x) + abs(self.y)


def run_a(input_file):
    options = {'part': 'a'}
    position = Coordinate(0, 0)
    waypoint = Coordinate(1, 0)

    return _run(input_file, position, waypoint, options)


def run_b(input_file):
    options = {'part': 'b'}
    position = Coordinate(0, 0)
    waypoint = Coordinate(10, 1)

    return _run(input_file, position, waypoint, options)


def _run(input_file, position, waypoint, options):
    directions = _read(input_file)
    position = _navigate(directions, waypoint, position, options)

    return position.manhattan()


def _navigate(directions, waypoint, position, options):
    if len(directions) == 0:
        return position

    part = options['part']
    action, value = directions[0]

    if action in DIRECTIONS:
        position.move(action, value) if part == 'a' else waypoint.move(
            action, value)
    elif action in TURNS:
        waypoint.rotate(action, value)
    else:  # forward
        position.waypoint(value, waypoint)

    return _navigate(directions[1:], waypoint, position, options)


def _read(file_name):
    with open(file_name) as f:
        input = [[line[0], int(line[1:])] for line in f]

    return input


def solve():
    input_file = 'day12/12.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
