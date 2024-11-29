def read_to_list(path):
    with open(path) as f:
        lines = f.read().splitlines()
        return lines