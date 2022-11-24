from re import match, search


def run_a(input_file):
    rules, lines = _read(input_file)

    resolved_rule_0 = _resolve('0', rules)
    resolved_regex = f'^{resolved_rule_0}$'

    return sum([1 for line in lines if match(resolved_regex, line)])


def run_b(input_file):
    rules, lines = _read(input_file)

    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'

    resolved_rule_42 = _resolve('42', rules)
    resolved_rule_31 = _resolve('31', rules)
    resolved_regex = f'^(?P<match_42>({resolved_rule_42})+)(?P<match_31>({resolved_rule_31})+)$'

    result = 0
    for line in lines:
        matches = search(resolved_regex, line)
        if matches and len(matches.group('match_42')) > len(matches.group('match_31')):
            result += 1

    return result


def _resolve(rule_number, rules):
    rule = rules[rule_number]
    return ''.join(_resolve_char(char, rules) for char in rule)


def _resolve_char(char, rules):
    if char in 'ab|':
        return char
    else:
        return f'({_resolve(char, rules)})'


def _read(file_name):
    with open(file_name) as f:
        rules, input = f.read().split('\n\n')
        rules = _read_rules(rules)
        input = _read_input(input)

    return rules, input


def _read_rules(rules):
    rules_dict = {}
    for rule in rules.split('\n'):
        rule_number, rule_content = rule.split(': ')
        rules_dict[rule_number] = rule_content.replace('"', '').split()

    return rules_dict


def _read_input(input):
    return [line for line in input.split('\n')]


def solve():
    input_file = 'day19/19.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
