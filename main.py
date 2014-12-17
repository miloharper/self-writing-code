import os
from food_map import create_random_food_map
from code_generation import create_code
x = 50
y = 50
life = 100

def main():
    code = create_code()
    food_map = create_random_food_map()
    while life > 0:
        code_as_string = convert_code_from_list_to_string(code)
        exec code_as_string
    print code_as_string


def convert_code_from_list_to_string(input_code):
    output_code = ""
    for line in input_code:
        output_code = output_code + os.linesep + line
    return output_code


def update_everything():
    global x
    global y
    global FoodMap
    global life
    life -= 1
    if FoodMap[x][y] > 0:
        eat = min(FoodMap[x][y], 10)
        life += eat
        FoodMap[x][y] -= eat
    print "Position = [" + str(x) + "," + str(y) + "], Life = " + str(life)


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
    return FoodMap[x][y] > 0


if __name__ == '__main__':
    main()

