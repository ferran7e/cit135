#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python Week Six In class Lab - Problem 5
#Date Assigned: Oct 4 at 9am
#Due Date and Time: Oct 11 by 9am
#Description: Creates a dictionary and compares user input for the value of the key.
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

# Define the animals in a dict.
animals = {"cow": "bessie", "dog": "max", "cat": "meowcat", "wolf": "wolfie", "rabbit": "carroteater", "mouse": "mousie", "lizard": "charizard", "ogre": "shrek", "whale": "shamu", "sloth":"adam"}

# Show the user the available animals they can receive back.
animals_possible = ""
for k, v in animals.items():
    animals_possible = k + " " + animals_possible
print("You can choose from the following to get a name back:\n" + animals_possible)

# Takes input from the user and returns the animal name.
user_input = input("\nPlease input an animal to get the corresponding name: ").lower()
print("The name of the " + user_input + " is " + animals[user_input])



