print('Задание №1')

from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        recipe = line.strip()
        ingredient_count = int(file.readline())
        ingredients = []
        for _ in range(ingredient_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append(
                {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            )
        file.readline()
        cook_book[recipe] = ingredients


print('cook-book - ')
pprint(cook_book, sort_dicts=False)
