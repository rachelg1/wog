from random import randint
from currency_converter import CurrencyConverter

from utils import integer_input


def get_money_interval(usd_value, difficulty):
    converter = CurrencyConverter()
    ils_value = converter.convert(usd_value, 'USD', 'ILS')
    interval = 10 - difficulty
    min_value = ils_value - interval
    max_value = ils_value + interval

    return min_value, max_value


def get_guess_from_user(usd_value):
    prompt = f'Please enter your guess: if the value is {usd_value} USD, how many ILS is it?\n'
    return integer_input(prompt)


def compare_results(min_value, max_value, entered_value):
    return min_value <= entered_value <= max_value


def play(difficulty):
    usd_value = randint(0, 100)
    min_value, max_value = get_money_interval(usd_value, difficulty)
    entered_value = get_guess_from_user(usd_value)
    return compare_results(min_value, max_value, entered_value)
