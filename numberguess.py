# This is a game. First you will try to guess the computer's number. Then, the computer will try to guess yours!

import random
from re import X
from readline import set_completion_display_matches_hook

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low!')
        elif guess > random_number:
            print('Sorry, guess again. Too high!')

    print('Yay, congrats! You have guesssed the number correctly!')

def computer_guess(x):
    low = 1 
    high = X
    feedback = ''
    while feedback !='c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print('Yay! I guessed your number correctly! I am so smart! Next task...')
    time.sleep(2)
    print('Take over the world!')

guess(100)
import time
time.sleep(3)
print('Now you pick a number!')
time.sleep(2)
print('Let me guess...')
time.sleep(4)
computer_guess(100)

