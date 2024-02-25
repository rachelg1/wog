from games import guess_game, memory_game, currency_roulette_game
from score import add_score
from utils import integer_input_validation


def welcome():
    user_name = input('Please enter your name:\n')
    print(f'Hi {user_name} and welcome to the World of Games: The Epic Journey')


def start_play():
    prompt = 'Please choose a game to play: \n' \
             '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back. \n' \
             '2. Guess Game - guess a number and see if you chose like the computer. \n' \
             '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'

    game_num = integer_input_validation(prompt, 1, 3)

    prompt = 'Please select difficulty level between 1 and 5:\n'
    level = integer_input_validation(prompt, 1, 5)

    if game_num == 1:
        result = memory_game.play(level)
    elif game_num == 2:
        result = guess_game.play(level)
    else:
        result = currency_roulette_game.play(level)

    if result:
        print('You Win!')
        add_score(level)
    else:
        print('Oh, you lose')
