import os
import random 
from food_map import create_random_food_map
from code_generation import create_code
from probability import with_probability
x = None
y = None
food_map = None
health = None
total_moves = None


def main():
    global x
    global y
    global health
    global total_moves
    global food_map
    #Create a thousand genetic code mutations and fifty food_maps
    code_mutations = []
    food_maps = []
    for _ in range(50):
        code_mutations.append(create_code());
    for _ in range(50):
        food_maps.append(create_random_food_map());
    results = [] # Contains tuples of each mutation along with how long mutation survived
    #Run each mutation with ten random food maps and then take it's average healthtime.
    for code_mutation in code_mutations:
        current_mutation = convert_code_from_list_to_string(code_mutation)
        total_moves = 0 
        for _ in range(10):
            x = 50
            y = 50
            health = 100
            food_map = random.choice(food_maps)
            exec current_mutation
    
        results.append((current_mutation, (total_moves / 10)) ) # Take the average 
        total_moves = 0
    sorted(results, key=lambda result: result[1], reverse=True) #sort by length of health
    print "The top mutation was as follows: \n" + results[0][0] + " which lasted for " + str(results[0][1])



def convert_code_from_list_to_string(input_code):
    output_code = ""
    for line in input_code:
        output_code = output_code + os.linesep + line
    return output_code


def update_everything():
    global total_moves
    global health
    total_moves += 1
    health -= 1
    if food_map[x][y] > 0:
        eat = min(food_map[x][y], 10)
        health += eat
        food_map[x][y] -= eat
    print "Position = [" + str(x) + "," + str(y) + "], health = " + str(health) 


def up():
    global y
    y -= 1
    y = max(y, 0)
    update_everything()


def right():
    global x
    x += 1
    x = min(x, 99)
    update_everything()


def down():
    global y
    y += 1
    y = min(y, 99)
    update_everything()


def left():
    global x
    x -= 1
    x = max(x, 0)
    update_everything()


def on_food_square():
    return food_map[x][y] > 0


if __name__ == '__main__':
    main()