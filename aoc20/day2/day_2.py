class Day2:
    def run_a(self, input_file):
        input = self.__read(input_file)
        valid_password = self.__valid_passwords_policy_a(input)
        return valid_password

    def run_b(self, input_file):
        input = self.__read(input_file)
        valid_password = self.__valid_passwords_policy_b(input)
        return valid_password

    def __read(self, file_name):
        with open(file_name) as f:
            input = [self.__parse(line) for line in f]
        return input

    def __parse(self, line):
        [policy, password] = line.rstrip().split(':')
        [times, letter] = policy.split()
        [lower, upper] = times.split('-')
        return [int(lower), int(upper), letter, password.lstrip()]

    def __valid_passwords_policy_a(self, input):
        counter = 0
        for [lower, upper, letter, password] in input:
            if password.count(letter) in range(lower, upper + 1):
                counter += 1
        return counter

    def __valid_passwords_policy_b(self, input):
        counter = 0
        for [position_one, position_two, letter, password] in input:
            split_password = [char for char in password]
            position_one_contains_letter = split_password[position_one - 1] == letter
            position_two_contains_letter = split_password[position_two - 1] == letter
            if (position_one_contains_letter ^ position_two_contains_letter):
                counter += 1
        return counter


if __name__ == '__main__':
    day = Day2()

    result_a = day.run_a('day2/2.txt')
    print(result_a)

    result_b = day.run_b('day2/2.txt')
    print(result_b)
