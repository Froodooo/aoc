from utils import *
from collections import deque

INPUT_FILE = "./21.in"
SAMPLE_FILE = "./21.sample"

keypad_dimensions = {
    'numeric': (4, 3),
    'directional': (2, 3)
}

keypad_forbidden = {
    'numeric': (3, 0),
    'directional': (0, 0)
}

numeric_keypad = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '0': (3, 1), 'A': (3, 2)
}

directional_keypad = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

def get_moves(path):
    moves = []
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i+1]
        if r2 > r1:
            moves.append('v')
        elif r2 < r1:
            moves.append('^')
        elif c2 > c1:
            moves.append('>')
        else:
            moves.append('<')
    return moves

def is_valid(keypad_type, r, c):
    rows, cols = keypad_dimensions[keypad_type]
    forbidden_row, forbidden_col = keypad_forbidden[keypad_type]
    return r >= 0 and c >= 0 and r < rows and c < cols and (r, c) != (forbidden_row, forbidden_col)

def bfs(start, goal, keypad_type):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        r, c = path[-1]
        if (r, c) == goal:
            return path
        for r2, c2 in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
            if is_valid(keypad_type, r2, c2) and (r2, c2) not in seen:
                queue.append(path + [(r2, c2)])
                seen.add((r2, c2))

def move_keypad(keypad_type, start, goal):
    path = bfs(start, goal, keypad_type)
    moves = get_moves(path) + ['A']
    return moves

def get_move_path(keypad_type, current, path):
    moves = []
    for button in path:
        goal = numeric_keypad[button] if keypad_type == 'numeric' else directional_keypad[button]
        button_moves = move_keypad(keypad_type, current, goal)
        current = goal
        moves += button_moves
    return current, moves

door_codes = [list(x) for x in read_to_list(SAMPLE_FILE)]
for door_code in door_codes:
    current = numeric_keypad['A']
    current, moves = get_move_path('numeric', current, door_code)
    for i in range(2):
        current = directional_keypad['A']
        current, moves = get_move_path('directional', current, moves)
    print(''.join(moves))
    print(len(moves))