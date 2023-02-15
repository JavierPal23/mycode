#!/usr/bin/env python3
""" TLG | Javier Palacios
    What 'Drum and Bass' DJ you'll like based on your favorite color."""

print("What is your name? ")
answer= ""
user_name = input()


while answer not in ["yellow", "green", "blue", "orange", "black", "red"]:
    print("Hello", user_name , "what is your favorite color? ")
    answer = input()
    answer = answer.lower()


if answer == "yellow":

    print("You picked", answer , "you'll more than likely like Subtronics")

if answer == "green":
    print("You picked", answer , "you'll more than likely like Level Up") 

if answer == "blue":                                             print("You picked", answer , "you'll more than likely like Kai Wachi")

if answer == "orange":
    print("You picked", answer , "you'll more than likely like Illenium")

if answer == "black":
    print("You picked", answer , "you'll more than likely like Excision")

if answer == "red":
    print("You picked", answer , "you'll more than likely like Sullivan King")

else:
   print("You should check them out.")
