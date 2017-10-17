#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python 2.1 ( First Program )
#Date Assigned: September 6, 2017
#Due Date and Time: September 11, 2017
#Description: This program inputs dimensions of a room, and calculates how much paint is needed for the walls and ceiling with 2 coats each.
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

#Prompt the user for the dimensions of the room.
length = int(input("What is the length, in feet, of the room?: "))
width = int(input("What is the width, in feet, of the room?: "))
height = int(input("What is the height, in feet, of the room?: "))

#Finds the area of the walls in the room.
wall_area = (length * height) * 2
wall_area_2 = (width * height) * 2

#Calculates the total square-footage of paint needed to paint the room with 2 coats of paint.
walls_total = (wall_area + wall_area_2) * 2

#Calculates how many gallons of paint are needed for this project.
wall_cans_needed = math.ceil(walls_total / 250)

print("You will need {} can(s) of paint to complete the walls of this room.".format(wall_cans_needed))

# Calculates the surface area of the ceiling.
ceiling_surface_area = length * width

# Calculates the amount of paint cans needed for the ceiling.
ceiling_paint_needed = ceiling_surface_area * 2
ceiling_cans_needed = math.ceil(ceiling_paint_needed / 200)

print("You will need {} can(s) of paint to complete the walls of this room.".format(ceiling_cans_needed))








