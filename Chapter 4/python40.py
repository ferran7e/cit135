#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python 4.0
#Date Assigned: Sept 20 at 11am
#Due Date and Time: Monday, Sept 25th @ 11:59pm
#Description: Calculates the user's BMI and outputs statements depending on the result. Statements correspond with this diagram: https://goo.gl/1DWeCU
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

# Prompts the user for input about their weight and height.
kg_weight = float(input("Please enter your weight in Kilograms: "))
meters_height = float(input("Please enter your height in meters: "))

# Converts meters to centimeters to easily compare to chart listed above.
centimeters_height = meters_height / 100

# Calculates the user's BMI
bmi = kg_weight / (math.pow(meters_height, 2))

# Evaluates and outputs the BMI and a suggestion to the user.
if bmi <= 19:
    print("Your BMI is", round(bmi, 1), "\nYou're underweight. You should consider eating some milkshakes and fast food!")
elif bmi <= 25:
    print("Your BMI is", round(bmi, 1), "\nYou're normal weight -- keep eating and doing physical activity!")
else:
    print("Your BMI is", round(bmi, 1), "\nYou should consider losing some weight. Try eating different foods, and working out more!")






