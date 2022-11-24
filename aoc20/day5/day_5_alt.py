class Day5Alt:
    def run_a(self, input_file):
        input = self.__read(input_file)
        seat_ids = self.__get_seat_ids(input)
        return max(seat_ids)

    def run_b(self, input_file):
        input = self.__read(input_file)
        seat_ids = self.__get_seat_ids(input)
        seat_ids.sort()
        return self.__get_missing_seat_id(seat_ids)

    def __get_seat_ids(self, input):
        seat_ids = []
        for boarding_pass in input:
            seat_ids.append(self.__calculate_seat_id(boarding_pass))
        return seat_ids

    def __calculate_seat_id(self, input):
        binary_input = input.replace('F', '0').replace(
            'B', '1').replace('L', '0').replace('R', '1')
        row = int(binary_input[:7], 2)
        column = int(binary_input[7:], 2)
        seat_id = row * 8 + column
        return seat_id

    def __get_missing_seat_id(self, sorted_seat_ids):
        for index in range(sorted_seat_ids[0], sorted_seat_ids[-1]):
            if (index not in sorted_seat_ids and (index - 1) in sorted_seat_ids and (index + 1) in sorted_seat_ids):
                return index

    def __read(self, file_name):
        with open(file_name) as f:
            input = [line.rstrip() for line in f]
        return input


if __name__ == '__main__':
    day = Day5Alt()

    input_file = 'day5/5.txt'

    result_a = day.run_a(input_file)
    print(result_a)

    result_b = day.run_b(input_file)
    print(result_b)
