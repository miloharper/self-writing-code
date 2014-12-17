from probability import with_probability
import random

def create_code():
    code = []
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


def whitespace(indents):
    return indents * "    "


def get_current_number_of_indents(code):
    if len(code) > 0:
        white_space_characters = len(code[-1]) - len(code[-1].lstrip(' '))
        return white_space_characters / 4
    else:
        return 0


def last_command_is_pass(code):
    if len(code) > 0:
        if code[-1][len(code[-1])-4:] == "pass":
            return True
        else:
            return False
    else:
        return False

