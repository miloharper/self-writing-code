import os
import random 
from food_map import create_food_maps
from code_generation import create_code_mutations

class genetics:
    x = None
    y = None
    food_map = None
    health = None
    survival_time = None
    brain_size = None # A mutation uses more energy per move if it has a large brain size (lines of code)

    def __init__(self, verbose):
        self.verbose = verbose

    def run(self):
        number_of_tests = 50
        code_mutations = create_code_mutations(100)
        food_maps = create_food_maps(50)
        results = [] # Contains tuples of each mutation along with how long mutation survived
        for code_mutation in code_mutations:
            if self.verbose:
                print "Testing a new code mutation across 10 food maps:"
            current_mutation = self.convert_code_from_list_to_string(code_mutation)
            self.brain_size = len(code_mutation)
            average_survival_time = self.measure_average_survival_time(current_mutation, food_maps, number_of_tests)
            results.append((current_mutation, average_survival_time, self.brain_size))
        sorted(results, key=lambda result: result[1], reverse=True) #Rank the best average survival times
        print "The top mutation was as follows: \n" + results[0][0] + "\n\nWhich on average survived for " + str(results[0][1]) + " units of time and had a brain size of " + str(results[0][2]) + " lines of code."


    def measure_average_survival_time(self, current_mutation, food_maps, number_of_tests):
        cumulative_survival_time = 0
        for _ in range(number_of_tests):
            self.food_map = random.choice(food_maps)
            cumulative_survival_time += self.measure_survival_time(current_mutation)
        return (cumulative_survival_time / number_of_tests)


    def measure_survival_time(self, current_mutation):
        self.x = 50
        self.y = 50
        self.health = 100
        self.survival_time = 0
        while self.health > 0:
            exec current_mutation
            self.update_everything()
            if self.verbose:
                print "Health: " + str(health)
        return self.survival_time


    def convert_code_from_list_to_string(self, input_code):
        output_code = ""
        for line in input_code:
            output_code = output_code + os.linesep + line
        return output_code


    def update_everything(self):
        self.survival_time += 1
        self.health -= self.calculate_energy_required_to_maintain_brain() # loses 0.1 to 2.1 health per move
        if self.food_map[self.x][self.y] > 0:
            eat = min(self.food_map[self.x][self.y], 10)
            self.health += eat
            self.food_map[self.x][self.y] -= eat
        if self.verbose:
            print "Position = [" + str(self.x) + "," + str(self.y) + "], health = " + str(self.health) 


    def calculate_energy_required_to_maintain_brain(self):
        minimum_loss = 1
        energy_loss = (4*(self.brain_size / 100))
        return minimum_loss+energy_loss


    def up(self):
        self.y -= 1
        self.y = max(self.y, 0)
        self.update_everything()


    def right(self):
        self.x += 1
        self.x = min(self.x, 99)
        self.update_everything()


    def down(self):
        self.y += 1
        self.y = min(self.y, 99)
        self.update_everything()


    def left(self):
        self.x -= 1
        self.x = max(self.x, 0)
        self.update_everything()


    def stay(self):
        self.update_everything()


    def on_food_square(self):
        return self.food_map[self.x][self.y] > 0
