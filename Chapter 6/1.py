#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python Week Six In class Lab - Problem 1
#Date Assigned: Oct 4 at 9am
#Due Date and Time: Oct 11 by 9am
#Description: Prints a random tuple with 5 numbers.
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

# Creates a new list for the random numbers to be generated into.
my_list = []

# Adds numbers to above list.
for x in range(5):
    my_list.append(random.randint(1,101))

# Converts then prints tuple.
print(tuple(my_list))


