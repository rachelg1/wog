import time
from random import randint

from utils import integer_input, screen_cleaner


def generate_sequence(difficulty):
    numbers = []
    for i in range(difficulty):
        numbers.append(randint(0, 101))
    return numbers


def get_list_from_user(difficulty):
    numbers = []
    for i in range(difficulty):
        numbers.append(integer_input(f'Please enter a number (#{i + 1})\n'))
    return numbers


def is_list_equal(secret_list, entered_list):
    return secret_list == entered_list


def play(difficulty):
    secret_list = generate_sequence(difficulty)
    print(secret_list)
    time.sleep(0.7)
    screen_cleaner()
    entered_list = get_list_from_user(difficulty)
    return is_list_equal(secret_list, entered_list)
