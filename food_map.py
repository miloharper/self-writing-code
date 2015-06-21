from probability import with_probability
import random


def create_food_maps(number_of_food_maps):
    food_maps = []
    for _ in range(number_of_food_maps):
        food_maps.append(create_random_food_map());
    return food_maps


def create_random_food_map():
    food_map = [[0 for x in xrange(10)] for x in xrange(10)]
    for row_number, row in enumerate(food_map):
        for col_number, _ in enumerate(row):
            if with_probability(25):
                food_map[row_number][col_number] = random.randrange(50, 100)
    return food_map