#!/usr/bin/env python3
####ROCK PAPER SCISSORS CODE####
#Import random module
import random

def game():
    #Create a list of play options
    play = ["Rock", "Paper", "Scissors"]


    #Set the player to False
    camper = False
    victory= False

    while True:
        #Assign a random play to the system
        bigfoot = play[random.randint(0,2)]

        camper = input("Rock, Paper, Scissors?").capitalize()
        if camper == bigfoot:
            print("Tie!")
            continue
        elif camper == "Rock":
            if bigfoot == "Paper":
                print("You lose!", bigfoot, "covers", camper)
            else:
                print("You win!", camper, "smashes", bigfoot)
                victory= True
        elif camper == "Paper":
            if bigfoot == "Scissors":
                print("You lose!", bigfoot, "cuts", camper)
            else:
                print("You win!", camper, "covers", bigfoot)
                victory= True
        elif camper == "Scissors":
            if camper == "Rock":
                print("You lose...", camper, "smashes", camper)
            else:
                print("You win!", camper, "cuts", bigfoot)
                victory= True
        else:
            print("That's not a valid play. Check the spelling!")
            continue
        #Player was set to True, but we want it to be False so the loop continues
        camper = False
        bigfoot = play[random.randint(0,2)]
        return victory

if __name__ == "__main__":
    game()
