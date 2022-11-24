# Using cube coordinates
# https://www.redblobgames.com/grids/hexagons/#coordinates
COORDINATES = [(1, -1, 0), (0, -1, 1), (-1, 0, 1),
               (-1, 1, 0), (0, 1, -1), (1, 0, -1)]


def run_a(input_file):
    tiles = _read(input_file)
    tiles_dict = _flip_tiles(tiles, {})
    flipped_tile_colors = list(tiles_dict.values())
    black = flipped_tile_colors.count(1)

    return black


def run_b(input_file):
    tiles = _read(input_file)
    tiles_dict = _flip_tiles(tiles, {})

    for _ in range(100):
        tiles_dict = _flip_day_tiles(tiles_dict)

    flipped_tile_colors = list(tiles_dict.values())
    black = flipped_tile_colors.count(1)

    return black


def _flip_day_tiles(tiles_dict):
    flipped_tiles_dict = {}
    tiles_dict = _new_neighbours(tiles_dict)
    for tile, color in tiles_dict.items():
        new_color, tiles_dict = _flip_day_tile(tile, color, tiles_dict)
        flipped_tiles_dict[tile] = new_color

    return flipped_tiles_dict


def _new_neighbours(tiles_dict):
    new_neighbours = {}
    for tile in tiles_dict.keys():
        (x, y, z) = tile
        for (dx, dy, dz) in COORDINATES:
            neighbour_coordinate = (x + dx, y + dy, z + dz)
            if neighbour_coordinate not in tiles_dict:
                new_neighbours[neighbour_coordinate] = -1  # white

    return tiles_dict | new_neighbours


def _flip_day_tile(tile, color, tiles_dict):
    (x, y, z) = tile
    black = white = 0
    for (dx, dy, dz) in COORDINATES:
        neighbour_coordinate = (x + dx, y + dy, z + dz)
        if neighbour_coordinate in tiles_dict:
            if tiles_dict[neighbour_coordinate] == 1:  # black
                black += 1
            elif tiles_dict[neighbour_coordinate] == -1:  # white
                white += 1

    if color == 1 and (black == 0 or black > 2):  # currently black
        color = -1  # white
    elif color == -1 and black == 2:  # currently white
        color = 1  # black

    return color, tiles_dict


def _flip_tiles(tiles, tiles_dict):
    for tile in tiles:
        (x, y, z) = _flip_tile(tile)
        if (x, y, z) in tiles_dict:
            tiles_dict[(x, y, z)] = -tiles_dict[(x, y, z)]  # flip color
        else:
            tiles_dict[(x, y, z)] = 1  # black

    return tiles_dict


def _flip_tile(tile):
    (x, y, z) = (0, 0, 0)
    for (dx, dy, dz) in tile:
        x += dx
        y += dy
        z += dz

    return (x, y, z)


def _read(file_name):
    with open(file_name) as f:
        tiles = [_read_tile(tile.rstrip()) for tile in f]

    return tiles


def _read_tile(line):
    chars = [char for char in line]
    tile = []
    i = 0
    while i < len(chars):
        if chars[i] == 'e':
            tile.append((1, -1, 0))
            i += 1
        elif chars[i] == 's':
            if chars[i+1] == 'e':
                tile.append((0, -1, 1))
            elif chars[i+1] == 'w':
                tile.append((-1, 0, 1))
            i += 2
        elif chars[i] == 'w':
            tile.append((-1, 1, 0))
            i += 1
        elif chars[i] == 'n':
            if chars[i+1] == 'w':
                tile.append((0, 1, -1))
            elif chars[i+1] == 'e':
                tile.append((1, 0, -1))
            i += 2

    return tile


def solve():
    input_file = 'day24/24.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
