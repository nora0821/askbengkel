#!/usr/bin/env python

import random

def main():
    """Guess The Element."""
    print("What element are basic metal")

    rainbow = [
        "Alumininium",
        "Gallium",
        "Indium",
        "Tin",
        "Thalium",
        "Lead",
        "Bismuth",
        "Ununtrium",
        "Ununquadium",
        "Ununpentium"

        ]

    x = random.choice(rainbow)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What element is that? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
        

main()
       

