from probability import with_probability
import random

def create_random_food_map():
    food_map = [[0 for x in xrange(100)] for x in xrange(100)]
    for row_number, row in enumerate(food_map):
        for col_number, _ in enumerate(row):
            if with_probability(5):
                food_map[row_number][col_number] = random.randrange(0, 100)
    return food_map