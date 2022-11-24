class Day3:
    def run_a(self, input_file):
        input = self.__read(input_file)
        trees_count = self.__traverse(3, 1, input)
        return trees_count

    def run_b(self, input_file):
        input = self.__read(input_file)
        traversals = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        trees_count = 1
        for x, y in traversals:
            trees_count *= self.__traverse(x, y, input)
        return trees_count

    def __traverse(self, x_interval, y_interval, input):
        trees_count = 0
        input = input[0::y_interval]
        for index, row in enumerate(input):
            x_coordinate = self.__x_coordinate(row, x_interval, index)
            chars = [char for char in row]
            if (chars[x_coordinate] == '#'):
                trees_count += 1
        return trees_count

    def __x_coordinate(self, row, x_interval, index):
        row_length = len(row)
        return (index * x_interval) % row_length

    def __read(self, file_name):
        with open(file_name) as f:
            input = [line.rstrip() for line in f]
        return input


if __name__ == '__main__':
    day = Day3()

    input_file = 'day3/3.txt'

    result_a = day.run_a(input_file)
    print(result_a)

    result_b = day.run_b(input_file)
    print(result_b)
