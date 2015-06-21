class LifeForm:


    def __init__(self, current_mutation, food_map, verbose):
        self.x = 50
        self.y = 50
        self.health = 100
        self.survival_time = 0
        self.current_mutation = current_mutation
        self.food_map = food_map
        self.verbose = verbose
        # A mutation uses more energy per move if it has a large brain size (lines of code)
        self.brain_size = len(current_mutation)


    def measure_survival_time(self):
        while self.health > 0:
            exec self.current_mutation
            self.update_everything()
            if self.verbose:
                print "Health: " + str(self.health)
        return self.survival_time


    def update_everything(self):
        self.survival_time += 1
        self.health -= self.calculate_energy_required_to_maintain_brain()
        if self.food_map[self.x][self.y] > 0:
            eat = min(self.food_map[self.x][self.y], 10)
            self.health += eat
            self.food_map[self.x][self.y] -= eat
        if self.verbose:
            print "Position = [" + str(self.x) + "," + str(self.y) + "], health = " + str(self.health)


    def calculate_energy_required_to_maintain_brain(self):
        minimum_loss = 1
        energy_loss = (4 * (self.brain_size / 100))
        return minimum_loss + energy_loss


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
