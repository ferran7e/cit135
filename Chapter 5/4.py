#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Week Five Lab Practice Problems - Program 4
#Date Assigned: 9/27 @ 9AM
#Due Date and Time: 10/4 @ 9AM
#Description: Grabs an integer from the user, and counts from 0 to that number.
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

# Asks the user for the number they would like counted to.
user_number = int(input("Please input a number: "))

# Counts each number from 0 to the users number.
for n in range(0, user_number + 1):
    print(n)