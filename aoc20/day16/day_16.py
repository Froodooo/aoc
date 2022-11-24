from functools import reduce
from operator import mul


def run_a(input_file):
    input = _read(input_file)
    _, invalid_values = _invalid_values(
        input['nearby_tickets'], input['rules'])

    return sum(invalid_values)


def run_b(input_file):
    input = _read(input_file)
    valid_tickets, _ = _invalid_values(
        input['nearby_tickets'], input['rules'])
    input['nearby_tickets'] = valid_tickets

    fields = _determine_fields(input['nearby_tickets'], input['rules'], {}, [])
    departure_values = _departure_values(input['your_ticket'], fields)

    return reduce(mul, departure_values, 1)


def _departure_values(ticket, fields):
    values = []

    for index, field in fields.items():
        if field.startswith('departure'):
            values.append(ticket[index])

    return values


def _determine_fields(tickets, rules, fields, seen_indices):
    if len(seen_indices) == len(tickets[0]):
        return fields

    for rule, numbers in rules.items():
        valid_indices = _determine_valid_indices(
            tickets, numbers, seen_indices)
        intersected_indices = _indices_intersection(valid_indices)
        if len(intersected_indices) == 1:
            seen_indices.append(intersected_indices[0])
            fields[intersected_indices[0]] = rule
            break

    return _determine_fields(tickets, rules, fields, seen_indices)


def _determine_valid_indices(tickets, rule_numbers, seen_indices):
    return [[index for index, number in enumerate(
        ticket) if number in rule_numbers and index not in seen_indices] for ticket in tickets]


def _indices_intersection(indices_list):
    return list(reduce(set.intersection, [set(indices) for indices in indices_list]))


def _invalid_values(tickets, rules):
    invalid_values = []
    valid_tickets = []

    for ticket in tickets:
        invalid_ticket_numbers = _invalid_ticket_numbers(ticket, rules)
        if len(invalid_ticket_numbers) > 0:
            invalid_values = invalid_values + invalid_ticket_numbers
        else:
            valid_tickets.append(ticket)

    return valid_tickets, invalid_values


def _invalid_ticket_numbers(ticket, rules):
    invalid_numbers = []

    for number in ticket:
        if not _is_valid_number(number, rules):
            invalid_numbers.append(number)

    return invalid_numbers


def _is_valid_number(number, rules):
    for rule in rules.values():
        if number in rule:
            return True

    return False


def _read(file_name):
    result = {}

    with open(file_name) as f:
        input = f.read()
        split_notes = _split_notes(input)
        result['rules'] = _parse_rules(split_notes[0])
        result['your_ticket'] = _parse_ticket(split_notes[1])
        result['nearby_tickets'] = _parse_tickets(split_notes[2])

    return result


def _split_notes(input):
    return [note.rstrip() for note in input.split('\n\n')]


def _parse_rules(input):
    rules = {}
    for line in input.split('\n'):
        rule, criteria = line.split(': ')
        criteria = _parse_criteria(criteria)
        rules[rule] = criteria

    return rules


def _parse_criteria(input):
    criteria = input.split(' or ')
    valid_set = set()
    for c in criteria:
        lower, upper = c.split('-')
        numbers = range(int(lower), int(upper) + 1)
        valid_set.update(numbers)

    return list(sorted(valid_set))


def _parse_ticket(input):
    return [int(number) for number in input.split('\n')[1].split(',')]


def _parse_tickets(input):
    tickets = input.split('\n')[1:]
    return [[int(number) for number in ticket.split(',')] for ticket in tickets]


def solve():
    input_file = 'day16/16.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
