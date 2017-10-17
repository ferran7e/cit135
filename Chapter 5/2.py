#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Week Five Lab Practice Problems - Program 2
#Date Assigned: 9/27 @ 9AM
#Due Date and Time: 10/4 @ 9AM
#Description: Outputs the day of the week corresponding to the numbers 1-7 that the user selects.
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

import sys

# Asks the user for the number of the day of the week they would like to be outputted.
day_number = int(input("Please input the number of the week you would like (Ex: 1 = Sunday, 2 = Monday, etc.): "))

# Checks to see if the user input is valid. Program exits if the input is invalid.
if day_number < 1 or day_number > 7:
    print("You have entered a number out of range. Input must be between 1 and 7.")
    sys.exit("User input was not correct.")

# Outputs the day of the week to the user depending on the number that was input.
if day_number == 1:
    print("The day of the week that you input was Sunday.")
elif day_number == 2:
    print("The day of the week that you input was Monday.")
elif day_number == 3:
    print("The day of the week that you input was Tuesday.")
elif day_number == 4:
    print("The day of the week that you input was Wednesday.")
elif day_number == 5:
    print("The day of the week that you input was Thursday.")
elif day_number == 6:
    print("The day of the week that you input was Friday.")
elif day_number == 7:
    print("The day of the week that you input was Saturday.")




