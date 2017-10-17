#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python 3.2
#Date Assigned: Sep 13 at 11am
#Due Date and Time: Monday 9/18 @ 12:30pm
#Description: This program takes 6 user inputs, figures out the min and max, and returns statements depending on the numbers.
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

# Define the variables for the operations to be carried out.
user_inputs = 0
highest_number = None
lowest_number = None

# Loops while the user is entering 6 numbers.
while user_inputs < 6:
    current_number = int(input("Enter a number to the list: "))

    # Set the variables on the first round so there are equal baseline to compare with.
    if user_inputs == 0:
        highest_number = current_number
        lowest_number = current_number

    # Increase the counter by 1, to end up with 6 inputs from the while statement.
    user_inputs += 1

    # Compare the user's number with the highest and lowest numbers to determine the output eventually.
    if current_number > highest_number:
        highest_number = current_number

    if current_number < lowest_number:
        lowest_number = current_number


# Print and display the output to the user, detecting if the numbers are over a certain value.
if highest_number > 50:
    print("The highest number is:", highest_number, "-- Whoa! That is a really big number!")
else:
    print("The highest number is:", highest_number)

if lowest_number < 5:
    print("The lowest number is:", lowest_number, "-- Oh my! That is a very small number!")
else:
    print("The lowest number is:", lowest_number)






