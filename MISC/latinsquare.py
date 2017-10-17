#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: In Class Python Lab Week 5
#Date Assigned: 9/27 @ 9am
#Due Date and Time: 9/27 @ 5PM
#Description: Inputs from a user and creates a latin square.
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

#Ask the user for size and start.
print("Welcome to the Latin Square Generator")
size = int(input("What size do you want to make the square? (1-10)"))
start = int(input("What is your starting number? (1-10)"))

for n in range(1, size + 1, 1):
    row = " "

    for i in range(start, start + size, 1):
        if i > size:
            i -= size
        item = str(i)
        row = row + " " + item


    start += 1
    if start > size:
        start -= size
    print(row)



