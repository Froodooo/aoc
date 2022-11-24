from copy import deepcopy


def run_a(input_file):
    input = _read(input_file)
    parsed = _parse(input)

    ingredients_with_potential_allergen = set()
    [ingredients_with_potential_allergen.update(
        ingredient) for ingredient in parsed['allergen_contains_ingredients'].values()]

    ingredients_without_allergen = [
        ingredient for ingredient in parsed['all_ingredients'] if ingredient not in ingredients_with_potential_allergen]

    count_of_ingredients_without_allergen = sum([parsed['all_ingredient_occurences'].count(
        ingredient) for ingredient in ingredients_without_allergen])

    return count_of_ingredients_without_allergen


def run_b(input_file):
    input = _read(input_file)
    parsed = _parse(input)

    allergen_contains_ingredients = parsed['allergen_contains_ingredients']
    updates = 1
    while updates > 0:
        updates = 0
        single_ingredients = [
            ingredients[0] for _, ingredients in allergen_contains_ingredients.items() if len(ingredients) == 1]
        for allergen, ingredients in allergen_contains_ingredients.items():
            if len(ingredients) == 1:
                continue
            for single_ingredient in single_ingredients:
                if single_ingredient in ingredients:
                    ingredients.remove(single_ingredient)
                    allergen_contains_ingredients[allergen] = ingredients
                    updates += 1

    sorted_ingredients = [allergen_contains_ingredients[key][0]
                          for key in sorted(allergen_contains_ingredients)]

    return ','.join(sorted_ingredients)


def _parse(input):
    allergen_contains_ingredients = {}
    all_ingredients = set()
    all_ingredient_occurences = []

    for allergens_dict in input:
        for i, (allergen, ingredients) in enumerate(allergens_dict.items()):
            all_ingredients.update(ingredients)
            if i == 0:
                all_ingredient_occurences += ingredients
            if allergen in allergen_contains_ingredients:
                current_list = allergen_contains_ingredients[allergen]
                intersected_list = [
                    ingredient for ingredient in ingredients if ingredient in current_list]
                if len(intersected_list) > 0:
                    allergen_contains_ingredients[allergen] = intersected_list
            else:
                allergen_contains_ingredients[allergen] = ingredients

    return {'allergen_contains_ingredients': allergen_contains_ingredients, 'all_ingredients': all_ingredients, 'all_ingredient_occurences': all_ingredient_occurences}


def _read(file_name):
    with open(file_name) as f:
        input = [_read_line(line) for line in f]

    return input


def _read_line(line):
    ingredients, allergens = line.split(' (contains ')
    ingredients = ingredients.split()
    allergens = allergens.rstrip().replace(')', '').split(', ')

    allergens_dict = {}
    for allergen in allergens:
        allergens_dict[allergen] = ingredients

    return allergens_dict


def solve():
    input_file = 'day21/21.txt'

    result_a = run_a(input_file)
    print(result_a)

    result_b = run_b(input_file)
    print(result_b)


if __name__ == '__main__':
    solve()
