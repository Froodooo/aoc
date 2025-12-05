from pathlib import Path
from typing import List

from utils import read_to_string


def parse_input(path: Path) -> List[str]:
    [fresh_ranges, ingredient_ids] = [x.split('\n') for x in read_to_string(str(path)).split('\n\n')]
    ingredient_ids = [int(x) for x in ingredient_ids[1:]]
    return [fresh_ranges, ingredient_ids]


def part_one(data: List[str]) -> int:
    [fresh_ranges, ingredient_ids] = data
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        for fresh_range in fresh_ranges:
            start, end = [int(x) for x in fresh_range.split('-')]
            if start <= ingredient_id <= end:
                fresh_count += 1
                break

    return fresh_count


def part_two(data: List[str]) -> int:
    [fresh_ranges, _] = data
    fresh_ranges = sorted([tuple(map(int, fresh_range.split('-'))) for fresh_range in fresh_ranges])
    non_overlapping_ranges = fresh_ranges[:1]

    # Inspired by https://stackoverflow.com/a/15273749
    for begin, end in fresh_ranges[1:]:
        prev_begin, prev_end = non_overlapping_ranges[-1]
        if prev_end >= begin - 1:
            non_overlapping_ranges[-1] = (prev_begin, max(prev_end, end))
        else:
            non_overlapping_ranges.append((begin, end))

    fresh_ingredients_count = sum(end - begin + 1 for begin, end in non_overlapping_ranges)

    return fresh_ingredients_count
