import os
import random
from life import LifeForm
from food_map import create_food_maps
from code_generation import create_code_mutations

def main():
    number_of_tests = 1
    code_mutations = create_code_mutations(1)
    food_maps = create_food_maps(1)
    results = []  # Contains tuples of each mutation along with how long mutation survived
    for code_mutation in code_mutations:
        current_mutation = convert_code_from_list_to_string(code_mutation)
        brain_size = len(current_mutation)
        average_survival_time = measure_average_survival_time(current_mutation, food_maps, number_of_tests)
        results.append((current_mutation, average_survival_time, brain_size))
    sorted(results, key=lambda result: result[1], reverse=True)  # Rank the best average survival times
    print "The top mutation was as follows: \n" + results[0][0] + "\n\nWhich on average survived for " + str(
        results[0][1]) + " units of time and had a brain size of " + str(results[0][2]) + " characters of code."


def measure_average_survival_time(current_mutation, food_maps, number_of_tests):
    cumulative_survival_time = 0
    for _ in range(number_of_tests):
        food_map = random.choice(food_maps)
        life_form = LifeForm(current_mutation, food_map, True)
        cumulative_survival_time += life_form.measure_survival_time()
    return (cumulative_survival_time / number_of_tests)


def convert_code_from_list_to_string(input_code):
    output_code = ""
    for line in input_code:
        output_code = output_code + os.linesep + line
    return output_code

if __name__ == '__main__':
    main()