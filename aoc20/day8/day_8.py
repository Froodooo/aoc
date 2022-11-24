class GameConsole:
    def __init__(self, input):
        self.input = input
        self.accumulator = 0
        self.finished = False
        self.index = 0
        self.visited = set()

    def run(self):
        while self.index not in self.visited:
            if self.index > len(self.input) - 1:
                self.finished = True
                break

            (operation, argument) = self.input[self.index]
            self._run_instruction(operation, argument)

    def _run_instruction(self, operation, argument):
        self.visited.add(self.index)

        if operation == 'acc':
            self.accumulator += argument
            self.index += 1
        elif operation == 'jmp':
            self.index += argument
        elif operation == 'nop':
            self.index += 1

    def get_accumulator(self):
        return self.accumulator

    def is_finished(self):
        return self.finished


def run_a(input_file):
    input = _read(input_file)

    return _run_game_console(input)


def run_b(input_file):
    input = _read(input_file)

    return _debug_game_console(input)


def _run_game_console(input):
    game_console = GameConsole(input)
    game_console.run()

    return game_console.get_accumulator()


def _debug_game_console(input):
    instruction_number = 0

    while True:
        updated_input = _update_input(input.copy(), instruction_number)
        game_console = GameConsole(updated_input)
        game_console.run()

        if game_console.is_finished():
            return game_console.get_accumulator()
        else:
            instruction_number += 1


def _read(file_name):
    with open(file_name) as f:
        input = [_read_line(line.rstrip()) for line in f]

    return input


def _read_line(line):
    operation, argument = line.split()
    
    return operation, int(argument)


def _update_input(input, instruction_number):
    index = [
        index
        for index, (operation, argument) in enumerate(input)
        if operation in ['jmp', 'nop']
    ][instruction_number]

    operation, argument = input[index]

    if operation == 'jmp':
        operation = 'nop'
    elif operation == 'nop':
        operation == 'jmp'

    input[index] = operation, argument

    return input


def run():
    input_file = 'day8/8.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    run()
