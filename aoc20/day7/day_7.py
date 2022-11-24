class Bag:
    def __init__(self, amount, shade, color):
        self.amount = amount
        self.shade = shade
        self.color = color

    def key(self):
        return self.shade + '-' + self.color


def run_a(input_file):
    bags = _read(input_file)
    bag_to_find = Bag(1, 'shiny', 'gold')

    found_bags = 0

    for key in bags.keys():
        if key == bag_to_find.key():
            continue

        if _find_bag(bags, key, bag_to_find):
            found_bags += 1

    return found_bags


def run_b(input_file):
    bags = _read(input_file)
    start_bag = Bag(1, 'shiny', 'gold')

    return _count_bags(start_bag, bags, 0)


def _find_bag(bags, key, bag_to_find):
    if key == bag_to_find.key():
        return True

    keys = [bag.key() for bag in bags[key]]
    for key in keys:
        if _find_bag(bags, key, bag_to_find):
            return True

    return False


def _count_bags(bag, bags, count):
    contained_bags = bags[bag.key()]

    return sum([bag.amount + (bag.amount * _count_bags(bag, bags, count)) for bag in contained_bags])


def _read(file_name):
    bags = {}
    with open(file_name) as f:
        for line in f:
            bag_key, contained_bags = _read_line(line.rstrip())
            bags[bag_key] = contained_bags

    return bags


def _read_line(line):
    words = line.split()

    shade, color = words[0], words[1]
    bag = Bag(1, shade, color)

    contained_bags = []
    index = 4

    while (index < len(words)):
        if words[index] != 'no':
            amount = int(words[index])
            shade = words[index + 1]
            color = words[index + 2]
            contained_bags.append(Bag(amount, shade, color))
        index += 4

    return bag.key(), contained_bags


def run():
    input_file = 'day7/7.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    run()
