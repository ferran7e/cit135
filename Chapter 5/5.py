#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Week Five Lab Practice Problems - Program 5
#Date Assigned: 9/27 @ 9AM
#Due Date and Time: 10/4 @ 9AM
#Description: Creates a random list, and allows the user to input a number. Checks to see if the given number is in the list.
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

# Import libraries and creates the list to be generated.
import random
random_list = []

# Generates the random list.
count = 0
while count < 10:
    random_list.append(random.randint(1, 51))
    count += 1

# Prints the list to the user to reference.
print("The list that was generated was:\n" + str(random_list))

user_input = int(input("Please enter a number: "))

# Notifies the user if the number was or wasn't found in the list.
if random_list.count(user_input) > 0:
    print("Your number was in the list " + str(random_list.count(user_input)) + " time(s).")
else:
    print("Your number was not in the list.")