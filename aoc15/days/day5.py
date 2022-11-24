import re


def run_a(input_file):
    input = _read(input_file)

    return sum([1 for line in input if _is_nice_part_a(line)])


def run_b(input_file):
    input = _read(input_file)

    return sum([1 for line in input if _is_nice_part_b(line)])


def _is_nice_part_a(line):
    return _does_not_contain_strings(line) and _contains_letter_twice_in_a_row(line) and _contains_three_vowels(line)


def _is_nice_part_b(line):
    return _contains_pair_twice(line) and _contains_letter_with_another_letter_in_between(line)


def _contains_three_vowels(line):
    regex = r'(.*[aeiou].*){3}'
    result = re.match(regex, line)
    return bool(result)


def _contains_letter_twice_in_a_row(line):
    regex = r'.*([a-z])\1+'
    result = re.match(regex, line)
    return bool(result)


def _does_not_contain_strings(line):
    regex = r'^(?:(?!(ab)|(cd)|(pq)|(xy)).)*$'
    result = re.match(regex, line)
    return bool(result)


def _contains_pair_twice(line):
    regex = r'([a-z]{2}).*\1'
    result = re.findall(regex, line)
    return bool(result)


def _contains_letter_with_another_letter_in_between(line):
    regex = r'([a-z])[a-z]\1'
    result = re.findall(regex, line)
    return bool(result)


def _read(file_name):
    with open(file_name) as f:
        input = [line for line in f]
    return input


def run():
    input_file = 'input/5.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    run()
