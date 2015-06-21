import random


def with_probability(probability):
    if random.randrange(0, 100) < probability:
        return True
    else:
        return False