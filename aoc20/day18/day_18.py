def run_a(input_file):
    options = {'part': 'a'}
    return _run(input_file, options)


def run_b(input_file):
    options = {'part': 'b'}
    return _run(input_file, options)


def _run(input_file, options):
    input = _read(input_file)
    return sum([_evaluate(line, options) for line in input])


def _is_number(str):
    return str.isdigit()


def _peek(stack):
    return stack[-1] if stack else None


def _apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    values.append(eval("{0}{1}{2}".format(left, operator, right)))


def _greater_precedence(op1, op2):
    precedences = {'+': 1, '*': 0}
    return precedences[op1] > precedences[op2]


def _use_precedence(top, token, options):
    part = options['part']
    if part == 'a':
        return True
    elif part == 'b':
        return _greater_precedence(top, token)


# http://www.martinbroadhurst.com/shunting-yard-algorithm-in-python.html
def _evaluate(tokens, options):
    values = []
    operators = []
    for token in tokens:
        if _is_number(token):
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = _peek(operators)
            while top is not None and top != '(':
                _apply_operator(operators, values)
                top = _peek(operators)
            operators.pop()  # Discard the '('
        else:
            # Operator
            top = _peek(operators)
            while top is not None and top not in '()' and _use_precedence(top, token, options):
                _apply_operator(operators, values)
                top = _peek(operators)
            operators.append(token)
    while _peek(operators) is not None:
        _apply_operator(operators, values)

    return values[0]


def _read(file_name):
    with open(file_name) as f:
        input = [[char for char in line if char.strip() != ''] for line in f]

    return input


def solve():
    input_file = 'day18/18.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
