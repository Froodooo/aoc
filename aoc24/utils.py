def read_to_list(path):
    with open(path) as f:
        lines = f.read().splitlines()
        return lines

def read_to_line(path):
    with open(path) as f:
        line = f.read()
        return line