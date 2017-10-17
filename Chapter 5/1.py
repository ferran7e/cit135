#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Week Five Lab Practice Problems - Program 1
#Date Assigned: 9/27 @ 9AM
#Due Date and Time: 10/4 @ 9AM
#Description: Inputs three variables from the user and outputs according to the number.
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

# Takes input from the user.
name = input("What is your name?: ")
age = int(input("What is your age?: "))
random_number = float(input("Input a number between 7 and 100 with two decimal places: "))

# Forces the user to input a number over 7 and under 100 if they haven't done so in the last input.
while random_number <= 7 or random_number >= 100:
    random_number = float(input("Input a number between 7 and 100 with two decimal places: "))

# Rounds in the input from the user to two decimal places.
random_number = round(random_number, 2)

# Outputs to the screen the information that has been processed.
print("Hey, " + name + " welcome to my program!")
print("From what you told me, you're " + str(age) + " years young!")
print("The number that you input was " + str(random_number))
