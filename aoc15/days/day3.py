class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == '^':
            self.y += 1
        elif direction == '>':
            self.x += 1
        elif direction == 'v':
            self.y -= 1
        elif direction == '<':
            self.x -= 1

    def set_input(self):
        return (self.x, self.y)


def run_a(input_file):
    input = _read(input_file)
    house = Coordinate(0, 0)
    visited = set()
    visited.add(house.set_input())

    for direction in input:
        house.move(direction)
        visited.add(house.set_input())

    return len(visited)


def run_b(input_file):
    input = _read(input_file)
    input = [input[i:i + 2] for i in range(0, len(input), 2)]

    houses = [Coordinate(0, 0), Coordinate(0, 0)]
    visited = [set(), set()]

    for index, house in enumerate(houses):
        visited[index].add(house.set_input())

    for directions in input:
        for index, direction in enumerate(directions):
            house = houses[index]
            house.move(direction)
            visited[index].add(house.set_input())

    result = set()
    for v in visited:
        result = result.union(v)

    return len(result)


def _read(file_name):
    with open(file_name) as f:
        input = list(f.read())
    return input


def run():
    input_file = 'input/3.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    run()
