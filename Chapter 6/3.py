#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python Week Six In class Lab - Problem 3
#Date Assigned: Oct 4 at 9am
#Due Date and Time: Oct 11 by 9am
#Description: Generates a list and prints numbers to the screen. Counts the number of times an element is in the list from the user input.
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

# Creates the empty list.
my_list = []

# Generates 10 random numbers in a list and prints them.
for x in range(10):
    my_list.append(random.randint(1, 51))
print(my_list)

# Asks the user for a number.
user_input = int(input("Please input a number to count it in our list: "))

# Prints and determines amount of times number is in the list.
print("Your number was in the list " + str(my_list.count(user_input)) + " time(s).")

