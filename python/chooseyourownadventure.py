# This is a choose your own adventure style game.

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You find yourself lost in the woods... there are two trails in front of you. Do you go 'left' or 'right'? It looks like there has been more foot traffic to the right...   ").lower()

if answer == "right":
    print("You head down the trail to the right... You are immediately confronted by a troll. The troll towers over you. You can feel his hot breath as he lets out a ROAR! 'What are you doing on my trail!?'")
    answer = input("You must answer him quickly. Choose: 'talk my way out' or 'run away' ")
    
    if answer == "talk my way out":
        print("You bravely say... 'I have brought you a gift!'. Trolls love gifts... this should go over well! ")
        answer = input("The troll squeals, 'What is this gift?', you don't have much... do you give him your 'jewels' or your 'apple'? ")

        if answer == "jewels":
            print("'It's a sack of emeralds and rubies!' you exclaim... This pleases the troll, he accepts your jewels... but eats you anyway! YOU LOSE!")
        elif answer =="apple":
            print("'It's this delicious apple! I picked it off of a tree!'... This angers the troll, 'I only eat fruit as an appetizer!' He laughs, eats the apple, and then eats you. YOU LOSE!")

    elif answer == "run away":
        print("You turn around and run as fast as you can back down the trail... but the troll is much faster... YOU LOSE!")

elif answer == "left":
    answer = input("You head down the left trail... It is very tranquil. You come up to a fresh water spring. Will you 'walk' past the spring? Or 'drink' from it? ")

    if answer == "walk":
        print("You walk past the spring, up a hill, and see a cave entrance.")
        answer = input("Do you go in the cave? 'yes' or 'no'    ")

        if answer == "yes":
                print("It's very dark in here... you can't see anything... except those two red eyes? Now it's 4? 6! 22!! Giant vampire bats swarm all around you and eat you! YOU LOSE! ")

        elif answer == "no":
                print("You walk right past the cave mouth and off a cliff and fall to your death! Yikes! YOU LOSE! ")

    elif answer == "drink":
        print("Wow that's refreshing! As you fill your belly and canteen with the fresh crystal water, millions of tiny bubbles begin to dance on the surface... something is there... ")
        answer = input("Do you 'run' or 'stay'  ?")
    
        if answer == 'run':
            print("You quickly flee, trip over a branch, and off a cliff to your death! YOU LOSE! ")

        elif answer == "stay":
            print("A beautiful mermaid appears behind the bubbles! Her scales are green and they gleam with a golden glow. 'Hello traveler, welcome to my grotto. I don't like visitors, but if you can make me laugh... I can let you pass..'   ")
            answer = input("Do you tell the mermaid a joke about an 'octopus' or about a 'manatee'? ")

            if answer == "octopus":
                print("'How many tickles does it take to make an octopus laugh?'... 'Ten-tickles!' ")
                print("The mermaid laughs with delight! And lets you live! YOU WIN!!!!! ")

            elif answer =="manatee":
                print("'What do you call a fat mermaid?'...'a manatee!'")
                print("The mermaid finds this extremely rude... so she drowns you. YOU LOSE!!!!")

else: 
    print("Uh oh, you made an invalid choice! If you didn't want to play... just say that! ")

print("END OF GAME")