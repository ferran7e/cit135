#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Jumbo
#Date Assigned: 9/27 @ 9am
#Due Date and Time: 9/27 @ 5PM
#Description: Jumbles user input.
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

from builtins import print

# Welcomes the user and sets up our words.
print("Welcome to the Jumbled word game!")
play = input("Do you want to play?").lower()
words = ("cow", "pig", "chicken", "donkey", "sheep", "harambe")

# Runs while the user is playing.
while play == "y":
    word = random.choice(words)
    correctword = word
    jumble = ""

    # Jumbles the words in the tuple.
    while word:
        letter = random.randrange(len(word))
        jumble = jumble + word[letter]
        word = word[0:letter] + word [letter+1:]
        print(word)

    print("The words are animals")
    print("The jumbled word is ", jumble)

    # Prompts the user for a guess, and compares it to the jumbled word.
    guess = input("What is your guess?")
    while guess != correctword and guess !="":
        print("WRONG")
        guess = input("Guess Again!")
    if guess == correctword:
        print("Well Done!")
    else:
        print("Sorry!")

    play = input("Would you like to play again??")

else:
    print("Goodbye!")
