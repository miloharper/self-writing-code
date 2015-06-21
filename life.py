class Death(Exception):
    pass

class LifeForm:


    def __init__(self, current_mutation, food_map, verbose):
        self.x = 5
        self.y = 5
        self.health = 100
        self.survival_time = 0
        self.current_mutation = current_mutation
        self.food_map = food_map
        self.verbose = verbose
        # A mutation uses more energy per move if it has a large brain size (lines of code)
        self.brain_size = len(current_mutation)
        self.metabolism = self.calculate_energy_required_to_maintain_brain()
        if self.verbose:
            print "New lifeform born"
            print "Brain size: " + str(self.brain_size)
            print "Metabolism: " + str(self.metabolism)


    def measure_survival_time(self):     
        try:
            forever = True
            while forever is True:
                if self.verbose:
                    print "Executing genetic behaviour: "
                exec self.current_mutation
                self.update_everything()
        except Death:
            if self.verbose:
                print "Lifeform died."
            return self.survival_time


    def update_everything(self):
        self.survival_time += 1
        self.health -= self.metabolism
        if self.health < 0:
            raise Death
        if self.verbose:
            print "Position = [" + str(self.x) + "," + str(self.y) + "], health = " + str(self.health)


    def calculate_energy_required_to_maintain_brain(self):
        minimum_loss = 1
        energy_loss = self.brain_size / float(1000)
        return minimum_loss + energy_loss


    def eat(self):
        if self.food_map[self.x][self.y] > 0:
            mouthful = min(self.food_map[self.x][self.y], 10)
            self.health += mouthful
            self.food_map[self.x][self.y] -= mouthful
            if self.verbose:
                print "Eating"
        self.update_everything()        


    def up(self):
        self.y -= 1
        self.y = max(self.y, 0)
        self.update_everything()


    def right(self):
        self.x += 1
        self.x = min(self.x, 9)
        self.update_everything()


    def down(self):
        self.y += 1
        self.y = min(self.y, 9)
        self.update_everything()


    def left(self):
        self.x -= 1
        self.x = max(self.x, 0)
        self.update_everything()


    def smells_food(self):
        return self.food_map[self.x][self.y] > 0
