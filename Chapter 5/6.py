#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Week Five Lab Practice Problems - Program 6
#Date Assigned: 9/27 @ 9AM
#Due Date and Time: 10/4 @ 9AM
#Description: Creates a dice game and looks for certain values.
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

playing = input("Would you like to play a game? (Y/N): ").lower()

count = 0
while playing == "y":
    dice_first_value = random.randint(1, 7)
    dice_second_value = random.randint(1, 7)

    dice_total = dice_first_value + dice_second_value

    if dice_total in (7, 11):
        print("You rolled a " + str(dice_total) + ". YOU WIN with only " + str(count) + " rolls.")
        playing = input("Would you like to play the game again? (Y/N): ").lower()
        count = 0
    else:
        count += 1
        print("You rolled a " + str(dice_total) + ". This is attempt number " + str(count) + ". You must roll a 7 or 11 to win.")
        playing = input("Roll again? (Y/N): ").lower()
