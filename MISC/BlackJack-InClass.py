#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment:
#Date Assigned:
#Due Date and Time:
#Description: Black Jack Game
###
#Certification of Authenticity:  I certify that this is entirely my own work,
#except where I have given fully-documented references to the work of others.
#I understand the definition and consequences of plagiarism and acknowledge
#that the assessor of this assignment may, for the purpose of assessing
#this assignment: - Reproduce this assignment and provide a copy
#to another member of academic staff; and/or Communicate a copy
#of this assignment to a plagiarism checking service (which may then retain
#a copy of this assignment on its database for the purpose of
#future plagiarism checking)
###

import random

faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = [" of clubs", " of hearts", " of spades", " of diamonds"]
deck = []
for suit in suits:
    for face in faces:
        deck.append(face + suit)

random.shuffle(deck)

hand = []
hand.append(deck.pop(0))
hand.append(deck.pop(0))

hand_value = 0
for card in hand:
    value = card[0]
    if value == "A":
        value = 11
    elif value in ("J", "Q", "K", "1"):
        value = 10
    else:
        value = int(value)

    hand_value += value
    print("Card: " + card)
print("Your hand value is:" , hand_value)