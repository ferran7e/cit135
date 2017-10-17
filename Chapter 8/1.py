#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Week Eight Practice Problems - Question 1
#Date Assigned: Oct 16 @ 11am
#Due Date and Time: Oct 23 @ 11am
#Description: This program takes user input in number form and returns the month with the use of a function.
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

# Asks the user for some input.
number = int(input("Please input a number: "))

# Function that determines what month the number belongs to.
def find_month(number):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[number-1]

# Prints the month that was processed.
print("The month you've input was: " + find_month(number))