from pathlib import Path
from typing import List

from utils import read_to_list

from polyomino.board import Rectangle


def parse_presents(lines: List[str]) -> list:
    presents_raw = [x for x in lines if '#' in x]
    presents = [presents_raw[i:i + 3] for i in range(0, len(presents_raw), 3)]
    presents_coordinates = []
    for present in presents:
        present_coordinates = []
        for y, row in enumerate(present):
            for x, c in enumerate(row):
                if c == '#':
                    present_coordinates.append((x, y))
        presents_coordinates.append(present_coordinates)
    return presents_coordinates


def parse_regions(lines: List[str]) -> list:
    regions_raw = [x for x in lines if 'x' in x]
    regions = []
    for region in regions_raw:
        dimensions, quantities = region.split(': ')
        (width, height) = tuple([int(x) for x in dimensions.split('x')])
        quantities = [int(x) for x in quantities.split()]
        regions.append(((width, height), quantities))
    return regions


def parse_input(path: Path) -> tuple:
    lines = [x for x in read_to_list(str(path)) if x]
    presents = parse_presents(lines)
    regions = parse_regions(lines)

    return (presents, regions)


def part_one(data: List[str]) -> int:
    (presents, regions) = data
    probably_fit = 0
    for region in regions:
        ((width, height), quantities) = region
        presents_for_region = []
        for i, quantity in enumerate(quantities):
            if quantity == 0:
                continue
            for _ in range(quantity):
                presents_for_region.append(presents[i])

        board = Rectangle(width, height)
        presents_for_region_length = sum(len(tile)
                                         for tile in presents_for_region)

        probably_fit += 1 if presents_for_region_length < board.count else 0

        # filler = []
        # if board.count > presents_for_region_length:
        #     for _ in range(board.count - presents_for_region_length):
        #         filler.append(MONOMINO)
        # tileset = Tileset(presents_for_region, filler, [])
        # problem = board.tile_with_set(tileset)
        # problem.solve()
    return probably_fit


def part_two(data: List[str]) -> int:
    '''Solve part two. Replace with puzzle logic.'''
    '''... if there would have been a part two, that is.'''
    return 0
