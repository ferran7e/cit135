#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python 4.1 // Part 1
#Date Assigned: Sep 20 at 12am
#Due Date and Time: Monday 9/25 at 11:59pm
#Description: This program outputs the range between 1 and 100, replacing multiples of 3 and 5 with silly phrases.
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

# Prompts the user if they would like to play the game.
playing = input("Would you like to play a game? (Y/N): ").lower()

# This while loop is continuously active while the user is playing the game.
while playing == "y":
    print("Welcome to the number print game!")

    # Defines the starting and ending range.
    range_start = 1
    range_end = 100

    # Sets the static words that will be used to output to the user in the upcoming 'for' loop.
    multiple_three_word = "Fizz"
    multiple_five_word = "Buzz"

    # Processes for each number in our range, defined by variables above, what words should be printed a divisibility of 3 or 5.
    for x in range (range_start, range_end + 1):
        if x % 3 == 0 and x % 5 == 0:
            print(multiple_three_word + multiple_five_word)
        elif x % 3 == 0:
            print(multiple_three_word)
        elif x % 5 == 0:
            print(multiple_five_word)
        else:
            print(x)

    # Asks the user if they would like to play the game again, if yes, goes back to the top of the while loop.
    playing = input("Would you like to play another game? (Y/N): ").lower()




