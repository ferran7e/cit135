#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Functions Lab
#Date Assigned:  Oct 16 at 12:30pm
#Due Date and Time: Oct 18 at 5pm
#Description: Creates a bunch of functions and feeds them into each other.
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

def square(number):
    squared_number = number * number
    return squared_number

def cube(number):
    cubed_number = number * number * number
    return cubed_number

def timeinsecs(hours, minutes):
    hours_to_minutes = hours / 60
    total_minutes = hours_to_minutes + minutes
    total_seconds = total_minutes * 60
    return total_seconds

def snowfall(timeinsecs(),flakespersec):
    #



# Ask the user to select a program
choice = input("Please input a program to use:\n\t1) Square a number\n\t2) Cube a number\n\t3) Seconds calculator\n\t4) Snowfall calculator\n> ")

# Use the correct function based on the input
if choice == "1" :
    number = int(input("Enter a number to square: "))

    print(str(number), "squared is", str(square(number)))

elif choice == "2" :
    number = int(input("Enter a number to cube: "))

    print(str(number), "cubed is", str(cube(number)))

elif choice == "3" :
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))

    print(str(hours), "hours and", str(minutes), "minutes is", str(seconds(hours, minutes)), "seconds.")

elif choice == "4" :
    hours = int(input("Please input the amount of hours: "))
    minutes = int(input("Please input the amount of minutes: "))
    flakes_per_second = int(input("Enter flakes per second: "))

    # dis
    snowfall(timeinsecs(hours, minutes), flakes_per_second)

    print(str(snowfall(seconds, flakes_per_second)), "inches is the depth of the snowfall.")

else:
    print(choice, "is not a valid choice!")