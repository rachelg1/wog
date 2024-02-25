SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 400


def screen_cleaner():
    print("\033[A                             \033[A")


def integer_input_validation(prompt, min_val, max_val):
    while True:
        value = integer_input(prompt)
        if min_val <= value <= max_val:
            return value
        else:
            prompt = f'Please insert a valid value, a number between {min_val} and {max_val}\n'


def integer_input(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            prompt = f'invalid input, please enter a number\n'
