#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python Week Six In class Lab - Problem 2
#Date Assigned: Oct 4 at 9am
#Due Date and Time: Oct 11 by 9am
#Description: Stores 1000 numbers in a list and prints them out.
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

# Create empty list.
my_list = []

# Places a number from 10 to 1000 into a list, 1000 times.
for x in range(1000):
    my_list.append(random.randint(10, 100))

# Prints all numbers in the list.
for n in my_list:
    print(n)