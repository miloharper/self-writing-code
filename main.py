import os
import random
FoodMap = [[0 for x in xrange(100)] for x in xrange(100)]
x = 50
y = 50
life = 100

def main():
    code = []
    seed_environment_with_food()
    while life > 0:
        code_as_string = convert_code_from_list_to_string(code)
        exec code_as_string
        code = modify_code(code)
    print code_as_string


def modify_code(code):
    available_commands = ["if on_food_square():", "if not on_food_square():", "up()", "down()", "left()", "right()"]
    random_number = random.randrange(0, len(available_commands))
    indents = get_current_number_of_indents(code)
    if last_command_is_pass(code):
        # Replace pass with new command
        code[-1] = whitespace(indents) + available_commands[random_number]
    else:
        # Either add the command within the current block, or outside it by using one less indent
        if with_probability(50):
            indents = max(0, indents - 1)
        code.append(whitespace(indents) + available_commands[random_number])

    # If an 'if' command was added, also add a 'pass' to make it valid Python
    if random_number == 0 or random_number == 1:
        code.append(whitespace(indents + 1) + "pass")
    return code


def with_probability(probability):
    if random.randrange(0, 100) < probability:
        return True
    else:
        return False


def convert_code_from_list_to_string(input_code):
    output_code = ""
    for line in input_code:
        output_code = output_code + os.linesep + line
    return output_code


def last_command_is_pass(code):
    if len(code) > 0:
        if code[-1][len(code[-1])-4:] == "pass":
            return True
        else:
            return False
    else:
        return False


def whitespace(indents):
    return indents * "    "


def get_current_number_of_indents(code):
    if len(code) > 0:
        white_space_characters = len(code[-1]) - len(code[-1].lstrip(' '))
        return white_space_characters / 4
    else:
        return 0


def seed_environment_with_food():
    for row_number, row in enumerate(FoodMap):
        for col_number, _ in enumerate(row):
            if with_probability(5):
                FoodMap[row_number][col_number] = random.randrange(0, 100)


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

