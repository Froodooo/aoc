import hashlib


def run_a(input_file):
    input = _read(input_file)
    m = ''
    count = 0
    while m[0:5] != '00000':
        count += 1
        md5 = hashlib.md5(f'{input}{str(count)}'.encode())
        m = md5.hexdigest()

    return count


def run_b(input_file):
    input = _read(input_file)
    m = ''
    count = 0
    while m[0:6] != '000000':
        count += 1
        md5 = hashlib.md5(f'{input}{str(count)}'.encode())
        m = md5.hexdigest()

    return count


def _read(file_name):
    with open(file_name) as f:
        input = f.readline()
    return input


def run():
    input_file = 'input/4.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    run()
