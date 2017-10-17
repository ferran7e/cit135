#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python Week Six In class Lab - Problem 4
#Date Assigned: Oct 4 at 9am
#Due Date and Time: Oct 11 by 9am
#Description: Generates a list and prints numbers to the screen. Counts the number of times an element is in the list from the user input using a sequential search.
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

# Creates a random list.
my_list = []

# Generates and prints a list of 10 numbers.
for x in range(10):
    my_list.append(random.randint(1, 51))
print(my_list)

# Prompts user for input.
user_input = int(input("Please input a number to compare: "))

# Searches through the list using a sequential search.
for n in my_list:
    if n == user_input:
        print("Your number is in the list!")