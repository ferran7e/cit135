#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Week Eight Practice Problems - Question 2
#Date Assigned: Oct 16 @ 11am
#Due Date and Time: Oct 23 @ 11am
#Description: Allows a shape to be calculated from user input.
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

import math

# Defines the functions for all four shapes.
def calc_square():
    side_length = float(input("Please enter the side length for the square: "))
    area = (side_length * side_length)
    area = round(area, 2)
    return area

def calc_rectangle():
    side_length = float(input("Please enter the length of the rectangle: "))
    side_height = float(input("Please enter the height of the rectangle: "))
    area = side_length * side_height
    area = round(area, 2)
    return area

def calc_triangle():
    side_base = float(input("Please enter the base of the triangle: "))
    side_height = float(input("Please enter the height of the triangle: "))
    area = .5 * (side_base * side_height)
    area = round(area, 2)
    return area

def calc_circle():
    radius = float(input("Please enter the radius of the circle: "))
    area = math.pi * (radius * radius)
    area = round(area, 2)
    return area

# Asks the user what shape they would like to input.
shape = int(input("Please input the number a shape below:\n\t1)Square\n\t2)Rectangle\n\t3)Triangle\n\t4)Circle\n> "))

# Determines what shape to use, calls the function, and outputs to the user.
if shape == 1:
    print("The area of a square is", calc_square())
elif shape == 2:
    print("The area of a rectangle is", calc_rectangle())
elif shape == 3:
    print("The area of a triangle is", calc_triangle())
elif shape == 4:
    print("The area of a circle is", calc_circle())
