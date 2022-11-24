from copy import deepcopy
from functools import reduce
from operator import mul


def run_a(input_file):
    tiles = _read(input_file)
    tile_neighbours = _find_edge_tiles(tiles)
    corner_tiles = [tile_id for tile_id,
                    tile_matches in tile_neighbours.items() if len(tile_matches) == 2]
    return reduce(mul, corner_tiles)


def run_b(input_file):
    tiles = _read(input_file)
    print('Finding tile neighbours')
    tile_neighbours = _find_edge_tiles(tiles)
    corner_tiles = [tile_id for tile_id,
                    tile_matches in tile_neighbours.items() if len(tile_matches) == 2]
    print('Creating tiles image')
    tiles_image = _create_tiles_image(tile_neighbours, corner_tiles)
    print('Creating image')
    image = _create_image(tiles_image, tiles)
    print('Creating borderless image')
    image = _create_borderless_image(image)
    print('Creating gapless image')
    image = _create_gapless_image(image)
    print(image)
    print('Finding monsters')
    monsters = _find_monsters(image)
    print(f'Found {monsters} monsters')
    monster_spaces = 15 * monsters
    all_spaces = _get_all_spaces(image)

    return all_spaces - monster_spaces


def _get_all_spaces(image):
    spaces = 0
    for row in image:
        for char in row:
            if char == '#':
                spaces += 1

    return spaces


def _find_monsters(image):
    for rotation in range(0, 4):
        rotated_image = _rotate_tile(image, rotation)
        for flip in ['horizontal', 'vertical', 'none']:
            flipped_image = _flip_tile(rotated_image, flip)
            monsters = 0
            for i in range(len(flipped_image) - 1):
                previous_row = flipped_image[i-1]
                row = flipped_image[i]
                next_row = flipped_image[i+1]
                for j in range(len(row) - 20):
                    if _contains_monster_middle(row[j:]) and _contains_monster_top(previous_row[j:]) and _contains_monster_bottom(next_row[j:]):
                        monsters += 1

            if monsters > 0:
                return monsters


def _contains_monster_middle(row_next):
    positions = [0, 5, 6, 11, 12, 17, 18, 19]
    for position in positions:
        if row_next[position] != '#':
            return False
    return True


def _contains_monster_top(row_next):
    result = row_next[18] == '#'
    return result


def _contains_monster_bottom(row_next):
    positions = [1, 4, 7, 10, 13, 16]
    for position in positions:
        if row_next[position] != '#':
            return False
    return True


def _create_gapless_image(image):
    result_rows = [[None] * (len(image[0]) * len(image[0][0]))
                   for _ in range(len(image[0]) * len(image[0][0]))]

    for i, row in enumerate(image):
        for j, tile in enumerate(row):
            for k, tile_row in enumerate(tile):
                for l, char in enumerate(tile_row):
                    row = i * len(tile_row) + k
                    col = j * len(tile_row) + l
                    result_rows[row][col] = char

    return result_rows


def _create_borderless_image(image):
    for i, row in enumerate(image):
        for j, tile in enumerate(row):
            tile = tile[1:len(tile) - 1]
            image[i][j] = tile
            for k, tile_row in enumerate(tile):
                tile_row = tile_row[1:len(tile_row) - 1]
                image[i][j][k] = tile_row

    return image


def _create_image(tiles_image, tiles):
    image = []
    for tiles_image_row in tiles_image:
        image_row = []
        seen = []
        for i in range(len(tiles_image_row) - 1):
            (rotate_1, flip_1, rotate_2, flip_2) = _flip_two_tiles(
                tiles[tiles_image_row[i]], tiles[tiles_image_row[i+1]])
            tile_1 = _rotate_tile(tiles[tiles_image_row[i]], rotate_1)
            tile_2 = _rotate_tile(tiles[tiles_image_row[i+1]], rotate_2)
            tile_1 = _flip_tile(tile_1, flip_1)
            tile_2 = _flip_tile(tile_2, flip_2)

            if tiles_image_row[i] not in seen:
                image_row.append(tile_1)
                seen.append(tiles_image_row[i])
            if tiles_image_row[i+1] not in seen:
                image_row.append(tile_2)
                seen.append(tiles_image_row[i + 1])

        image.append(image_row)

    return image


def _create_tiles_image(tile_neighbours, corner_tiles):
    used_tiles = []

    image = []
    print('Creating first row')
    first_row = _create_first_row(
        corner_tiles[0], tile_neighbours, corner_tiles)
    image.append(first_row)
    used_tiles = used_tiles + first_row

    continue_create_image = True
    next_row = [None]
    last_row_corner_tile = None
    previous_row = first_row
    while continue_create_image:
        print('Creating next row')
        next_row = _create_next_row(previous_row, tile_neighbours, used_tiles)
        image.append(next_row)
        used_tiles = used_tiles + next_row
        previous_row = next_row

        for corner_tile in corner_tiles:
            if corner_tile in tile_neighbours[previous_row[0]] and corner_tile not in used_tiles:
                last_row_corner_tile = corner_tile
                continue_create_image = False
                break

    print('Creating last row')
    last_row = _create_last_row(
        last_row_corner_tile, tile_neighbours, corner_tiles, used_tiles)
    image.append(last_row)
    return image


def _create_next_row(previous_row, tile_neighbours, used_tiles):
    left_edge_tile = _get_edge_tile(
        previous_row, tile_neighbours[previous_row[0]], tile_neighbours, used_tiles)
    right_edge_tile = _get_edge_tile(
        previous_row, tile_neighbours[previous_row[-1]], tile_neighbours, used_tiles)

    next_row = [left_edge_tile]
    previous_tile = left_edge_tile
    next_tile = None
    position = 1
    while next_tile not in tile_neighbours[right_edge_tile]:
        for possible_next_tile, neighbours in tile_neighbours.items():
            if previous_tile in neighbours and possible_next_tile in tile_neighbours[previous_row[position]] and len(neighbours) == 4 and possible_next_tile not in next_row and possible_next_tile not in used_tiles:
                next_tile = possible_next_tile
                next_row.append(next_tile)
                previous_tile = next_tile
                position += 1
                break

    next_row.append(right_edge_tile)

    return next_row


def _get_edge_tile(previous_row, possible_edge_tiles, tile_neighbours, used_tiles):
    edge_tile = None
    for possible_edge_tile in possible_edge_tiles:
        if possible_edge_tile not in previous_row and len(tile_neighbours[possible_edge_tile]) == 3 and possible_edge_tile not in used_tiles:
            edge_tile = possible_edge_tile
            break

    return edge_tile


def _create_first_row(first_tile, tile_neighbours, corner_tiles):
    first_row = [first_tile]
    next_tile = None

    while next_tile not in corner_tiles:
        possible_next_tiles = tile_neighbours[first_row[-1]]
        for possible_next_tile in possible_next_tiles:
            if len(tile_neighbours[possible_next_tile]) not in [2, 3] or possible_next_tile == corner_tiles[0] or possible_next_tile in first_row:
                continue
            next_tile = possible_next_tile
            first_row.append(next_tile)
            break

    return first_row


def _create_last_row(first_tile, tile_neighbours, corner_tiles, used_tiles):
    last_row = [first_tile]
    next_tile = None

    while next_tile not in corner_tiles:
        possible_next_tiles = tile_neighbours[last_row[-1]]
        for possible_next_tile in possible_next_tiles:
            if len(tile_neighbours[possible_next_tile]) not in [2, 3] or possible_next_tile == first_tile or possible_next_tile in last_row or possible_next_tile in used_tiles:
                continue
            next_tile = possible_next_tile
            last_row.append(next_tile)
            break

    return last_row


def _next_border_tile(tile_neighbours, tile_id, seen):
    return [neighbour_tile_id
            for neighbour_tile_id, neighbour_tiles in tile_neighbours.items()
            if tile_id in neighbour_tiles
            and len(neighbour_tiles) == 3
            and neighbour_tile_id not in seen]


def _find_edge_tiles(tiles):
    tile_neighbours = {}
    for tile_id, tile in tiles.items():
        borders = _get_tile_borders(tile)
        edges = []
        for other_tile_id, other_tile in tiles.items():
            if tile_id == other_tile_id:
                continue
            other_borders = _get_tile_borders(other_tile)
            touching_edges = 0
            for rotation in range(0, 4):
                rotated_other_borders = _rotate_borders(
                    other_borders, rotation)
                for flip in ['horizontal', 'vertical', 'none']:
                    flipped_other_borders = _flip_borders(
                        rotated_other_borders, flip)
                    intersection = [
                        (other_tile_id) for border in borders if border in flipped_other_borders]
                    touching_edges += len(intersection)
            if touching_edges > 0:
                edges.append(other_tile_id)
        tile_neighbours[tile_id] = edges

    return tile_neighbours


def _flip_two_tiles(tile_one, tile_two):
    tile_one_borders = _get_tile_borders(tile_one)
    tile_two_borders = _get_tile_borders(tile_two)

    for rotation_1 in range(0, 4):
        rotated_tile_one_borders = _rotate_borders(
            tile_one_borders, rotation_1)
        for flip_1 in ['horizontal', 'vertical', 'none']:
            flipped_tile_one_borders = _flip_borders(
                rotated_tile_one_borders, flip_1)
            for rotation_2 in range(0, 4):
                rotated_tile_two_borders = _rotate_borders(
                    tile_two_borders, rotation_2)
                for flip_2 in ['horizontal', 'vertical', 'none']:
                    flipped_tile_two_borders = _flip_borders(
                        rotated_tile_two_borders, flip_2)

                    if flipped_tile_one_borders[1] == flipped_tile_two_borders[3]:
                        return (rotation_1, flip_1, rotation_2, flip_2)


def _rotate_borders(borders, times):
    if times == 0:
        return borders
    return borders[-times:] + borders[:-times]


def _rotate_tile(tile, times):
    for _ in range(times):
        tile = list(zip(*tile[::-1]))
    for i in range(len(tile) - 1):
        tile[i] = list(tile[i])

    return tile


def _flip_borders(borders, orientation):
    [top, right, bottom, left] = borders
    if orientation == 'horizontal':
        return [top[::-1], left, bottom[::-1], right]
    elif orientation == 'vertical':
        return [bottom, right[::-1], top, left[::-1]]
    else:
        return borders


def _flip_tile(tile, orientation):
    flipped_tile = deepcopy(tile)
    if orientation == 'horizontal':
        for i in range(len(tile) - 1):
            flipped_tile[i].reverse()
    elif orientation == 'vertical':
        return list(reversed(tile))

    return flipped_tile


def _get_tile_borders(tile):
    top = ''.join([pixel for pixel in tile[0]])
    bottom = ''.join([pixel for pixel in tile[len(tile) - 1]])
    left = ''.join([tile[row][0] for row in range(len(tile))])
    right = ''.join([tile[row][len(tile) - 1] for row in range(len(tile))])

    return [top, right, bottom, left]


def _read(file_name):
    with open(file_name) as f:
        input = f.read().split('\n\n')
        tiles = {}
        for tile in input:
            tiles = _read_tile(tile, tiles)

    return tiles


def _read_tile(tile, tiles):
    tile_lines = tile.rstrip().split('\n')
    tiles[int(tile_lines[0].split()[1][0:-1])] = \
        [[col for col in row] for row in tile_lines[1:]]

    return tiles


def solve():
    input_file = 'day20/20.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
