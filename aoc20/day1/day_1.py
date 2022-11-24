import itertools


class Day1:
    def run_a(self, input_file):
        input = self.__read(input_file)

        (x, y) = self.__get_numbers(input, 2)

        return x * y

    def run_b(self, input_file):
        input = self.__read(input_file)

        (x, y, z) = self.__get_numbers(input, 3)

        return x * y * z

    def __read(self, file_name):
        with open(file_name) as f:
            input = [int(line.rstrip()) for line in f]
        return input

    def __get_numbers(self, input, amount):
        for numbers in itertools.combinations(input, amount):
            if sum(list(numbers)) == 2020:
                return numbers


if __name__ == '__main__':
    day = Day1()

    result_a = day.run_a('day1/1.txt')
    print(result_a)

    result_b = day.run_b('day1/1.txt')
    print(result_b)
