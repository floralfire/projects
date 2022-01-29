# This is a game based on rock, paper, scissors... but cooler! 
import random

user_wins = 0
computer_wins = 0

options = ["cowboy", "ninja", "bear"]
while True:
    user_input = input("Let's play! Choose your fighter: cowboy, ninja, or bear! Press 'q' to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    # cowboy: 0, ninja: 1, bear: 2
    # bear beats ninja, ninja beats cowboy, cowboy beats bear

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "bear" and computer_pick == "ninja":
        print("RAAAWWWWRR!!! The bear mauls the ninja! You win!")
        user_wins += 1

    elif user_input == "ninja" and computer_pick == "cowboy":
        print("*swoosh* The ninja sneaks up on the cowboy! You win!")
        user_wins += 1

    elif user_input == "cowboy" and computer_pick == "bear":
        print("BANG! The cowboy kills the bear! You win!")
        user_wins += 1

    elif user_input == "bear" and computer_pick == "cowboy":
        print("BANG! The cowboy kills the bear! You lose!")
        computer_wins += 1
    
    elif user_input =="cowboy" and computer_pick == "ninja":
        print("*swoosh* The ninja sneaks up on the cowboy! You lose!")
        computer_wins += 1

    elif user_input =="ninja" and computer_pick == "bear":
        print("RAAAWWWWRR!!! The bear mauls the ninja! You lose!")
        computer_wins += 1

    elif user_input =="ninja" and computer_pick == "ninja":
        print("Oops! You guys are on the same team! Try again :) ")

    elif user_input =="bear" and computer_pick == "bear":
        print("Oops! You guys are on the same team! Try again :) ")

    elif user_input =="cowboy" and computer_pick == "cowboy":
        print("Oops! You guys are on the same team! Try again :) ")

print("You won", user_wins, "times!")
print("The computer won", computer_wins, "times!")
print("Thanks for playing! Bye!")
