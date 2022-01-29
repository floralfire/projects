# This is a simple color mixing quiz! 

print("Welcome to my color quiz!")

playing = input("Do you want to play?   ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play! You'll need to know my favorite color. It's yellow!    ")
score = 0

answer = input("What is my favorite color?      ").lower()
if answer == "yellow":
    print("Nice! Glad you were paying attention!")
    score += 1
else:
    print("Weren't you paying attention? I just told you the answer...!")

answer = input("What do you add to my favorite color to make green?     ").lower()
if answer == "blue":
    print("That's right!")
    score += 1
else:
    print("Hmm... that's not right...!    ")

answer = input("If you add red to blue what do you get?     ").lower()
if answer == "purple":
    print("Good job!")
    score += 1
else:
    print("Hmm... that's not right...!    ")

answer = input("If you mix red and my favorite color... what do you get?    ").lower()
if answer == "orange":
    print("You got it!")
    score += 1
else:
    print("Hmm... that's not right...!    ")

answer = input("If I want to make pink... what should I add to red?     ").lower()
if answer == "white":
    print("Great job!")
    score += 1
else:
    print("Hmm... that's not right...!    ")

answer = input("What is the acronym for 'red, orange, yellow, green, blue, indigo, violet'? ").lower()
if answer == "roygbiv":
    print("You really know your colors!")
    score += 1
else:
    print("Hmm... that's not right...!    ")   

print("You got " + str(score) + " out of 6 questions correct!")

if score == 6:
    print("That's perfect!")
else:
    print("Better luck next time!")

