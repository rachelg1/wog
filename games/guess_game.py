from random import randint


def generate_number(difficulty):
    return randint(0, difficulty)


def get_guess_from_user(difficulty):
    num = input(f'Please input a number between 0 and {difficulty}:\n')
    return num


def compare_results(secret_number, entered_number):
    return str(secret_number) == entered_number


def play(difficulty):
    secret_number = generate_number(difficulty)
    entered_number = get_guess_from_user(difficulty)
    return compare_results(secret_number, entered_number)
