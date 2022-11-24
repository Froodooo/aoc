from functools import reduce
import re

ANY = 'ANY'
ALL = 'ALL'


class Day6:
    def run_a(self, input_file):
        groups = self.__read(input_file)
        result = self.__count_groups(groups, ANY)
        return result

    def run_b(self, input_file):
        groups = self.__read(input_file)
        result = self.__count_groups(groups, ALL)
        return result

    def __count_groups(self, groups, count_type):
        return sum(map(lambda group: self.__count_group(group, count_type), groups))

    def __count_group(self, group, count_type):
        if count_type == ANY:
            unique = set()
            for person in group:
                [unique.add(answer) for answer in person]
            return len(unique)
        else:
            intersection = set(group[0]).intersection(*group)
            return len(intersection)

    def __read(self, file_name):
        with open(file_name) as f:
            input = f.read().rstrip().split('\n\n')
            input = [re.split('\n| ', line) for line in input]
        return input


if __name__ == '__main__':
    day = Day6()

    input_file = 'day6/6.txt'

    result_a = day.run_a(input_file)
    print(result_a)

    result_b = day.run_b(input_file)
    print(result_b)
