import os
import random
import sys
x = 50
y = 50

def main():
    code = []
    last_working_code = ""
    time = 0
    while time < 100:
        try:
            code_as_string = convert_code_from_list_to_string(code)
            print code_as_string
            exec code_as_string
            last_working_code = code
            code = modify_code(code)
        except:
            print "An exception occurred. Reverting to last working code, and mutating: " + str(sys.exc_info())
            code = modify_code(last_working_code)
        finally:
            time += 1


def modify_code(code):
    available_commands = ["if on_food_square() == True:", "if on_food_square() == False:","up()", "down()", "left()", "right()"]
    random_number = random.randrange(0, len(available_commands))
    indents = get_current_number_of_indents(code)
    if last_command_is_pass(code) == True:
        code[-1] = whitespace(indents) + available_commands[random_number]
    else:
        if with_probability(50):
            indents = max(0, indents - 1)
        code.append(whitespace(indents) + available_commands[random_number])
    if random_number == 0 or random_number == 1:
        code.append(whitespace(indents + 1) + "pass")
    return code


def with_probability(probability):
    if random.randrange(0,100) < probability:
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

def print_position():
    global x
    global y
    print "[" + str(x) + "," + str(y) + "]"


def up():
    global y
    y -= 1
    y = max(y, 0)
    print_position()

def right():
    global x
    x += 1
    x = min(x, 100)
    print_position()

def down():
    global y
    y += 1
    y = min(y, 100)
    print_position()

def left():
    global x
    x -= 1
    x = max(x, 0)
    print_position()

def on_food_square():
    return False

if __name__ == '__main__':
    main()

