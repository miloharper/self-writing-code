from probability import with_probability
import random

def create_code_mutations(number_of_mutations):
    code_mutations = []
    for _ in range(number_of_mutations):
        code_mutations.append(create_code());
    return code_mutations

def create_code():
    code = []
    available_commands = ["if self.smells_food():", "if not self.smells_food():", "self.up()", "self.down()", "self.left()", "self.right()", "self.eat()"]
    for _ in range(random.randrange(0, 10)):
        command = random.choice(available_commands)
        indents = get_current_number_of_indents(code)
        # If the last command was a 'pass' replace it with a new command
        if last_command_is_pass(code):
            code[-1] = whitespace(indents) + command
        # Otherwise either add the command within the current block, or outside it by using one less indent
        else:        
            indents = randomly_reduce_indentation_level(indents)
            code.append(whitespace(indents) + command)
        # If an 'if' command was just added, also add a 'pass' to make it valid Python code
        if command[:2] == "if":
            code.append(whitespace(indents + 1) + "pass")
    return code


def randomly_reduce_indentation_level(indents):
    if with_probability(50):
        return max(0, indents - 1)
    else:
        return indents


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

