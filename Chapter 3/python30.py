#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python 3.0
#Date Assigned: Sep 13 at 11am
#Due Date and Time: Monday, September 18 by 12:30pm
#Description: This program takes a number input from the user and uses a while loop to add up numbers approaching the user's input.
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

# Defines if the user would like to participate in the game.
playing = input("Would you like to play the number game?: (Y/N)").lower()

# Is only played / looped when the user says they would like to play the game.
while playing == "y":
    counter = 1
    new_number = 0

    # User inputs the number  they would like to have calculated.
    user_number = int(input("Please enter a number to have added up: "))

    # Adds the numbers below the one that was inputted by the user by keeping a counter along the way and storing the information in a new variable.
    while counter <= user_number:
        new_number += counter
        counter += 1

    # Submits the output from the algorithm and asks the player if they would like to play again.
    print("The sum of your number and the rest of the numbers below it is:", str(new_number))
    playing = input("Would you like to play the game again? (Y/N)").lower()


