import os
import random
from life import LifeForm
from food_map import create_food_maps
from code_generation import create_code_mutations

def main():
    number_of_tests = 10
    code_mutations = create_code_mutations(1000)
    food_maps = create_food_maps(100)
    best_average_survival_time = 0
    best_code_mutation = ""
    mutation_number = 0
    last_update = 0
    for code_mutation in code_mutations:
        current_mutation = convert_code_from_list_to_string(code_mutation)
        average_survival_time = measure_average_survival_time(current_mutation, food_maps, number_of_tests)
        if average_survival_time > best_average_survival_time:
            best_average_survival_time = average_survival_time
            best_code_mutation = current_mutation
        mutation_number += 1
        if mutation_number == last_update + 100:
            last_update = mutation_number
            print "Mutation number " + str(mutation_number) + " - Best average survival time: " + str(best_average_survival_time) + " units of time."
    print "The top mutation was as follows: \n" + best_code_mutation + "\n\nWhich on average survived for " + str(best_average_survival_time) + " units of time."


def measure_average_survival_time(current_mutation, food_maps, number_of_tests):
    cumulative_survival_time = 0
    for _ in range(number_of_tests):
        food_map = random.choice(food_maps)
        life_form = LifeForm(current_mutation, food_map, False)
        cumulative_survival_time += life_form.measure_survival_time()
    return (cumulative_survival_time / number_of_tests)


def convert_code_from_list_to_string(input_code):
    output_code = ""
    for line in input_code:
        output_code = output_code + os.linesep + line
    return output_code

if __name__ == '__main__':
    main()