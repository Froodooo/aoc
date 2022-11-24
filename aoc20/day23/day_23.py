class Cup:
    def __init__(self, label):
        self.label = label
        self.next = None


def run_a(input_file, moves):
    labels = _read(input_file)
    cups = [Cup(label) for label in labels]
    cups_dict = {}
    for i in range(len(cups)):
        cups[i].next = cups[(i + 1) % len(cups)]
        cups_dict[labels[i]] = cups[i]

    _play(cups, labels, moves, cups_dict)
    cup_1 = cups_dict[1]
    next_cup = cup_1.next
    output = []
    for _ in range(len(cups) - 1):
        output.append(str(next_cup.label))
        next_cup = next_cup.next

    return ''.join(output)


def run_b(input_file, moves):
    labels = _read(input_file)
    labels = labels + [int(label) for label in range(len(labels) + 1, 1000001)]

    cups = [Cup(label) for label in labels]
    cups_dict = {}
    for i in range(len(cups)):
        cups[i].next = cups[(i + 1) % len(cups)]
        cups_dict[labels[i]] = cups[i]

    _play(cups, labels, moves, cups_dict)
    cup_1 = cups_dict[1]

    return cup_1.next.label * cup_1.next.next.label


def _play(cubs, labels, moves, cups_dict):
    min_label = min(labels)
    max_label = max(labels)
    current = cups_dict[labels[0]]

    for move in range(moves):
        picked_up = []
        picked_up_labels = []

        next_pick = current
        for _ in range(3):
            picked_up.append(next_pick.next)
            picked_up_labels.append(next_pick.next.label)
            next_pick = next_pick.next

        current.next = next_pick.next

        destination_label = current.label - 1
        if destination_label < min_label:
            destination_label = max_label
        while destination_label in picked_up_labels:
            destination_label -= 1
            if destination_label < min_label:
                destination_label = max_label

        destination = cups_dict[destination_label]
        picked_up[-1].next = destination.next
        destination.next = picked_up[0]
        current = current.next

    return current


def _read(file_name):
    with open(file_name) as f:
        labels = [int(label) for label in f.readline()]

    return labels


def solve():
    input_file = 'day23/23.txt'

    result_a = run_a(input_file, 100)
    print(result_a)

    result_b = run_b(input_file, 10000000)
    print(result_b)


if __name__ == '__main__':
    solve()
