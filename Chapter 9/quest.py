#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python Quest Module v1
#Date Assigned: October 18, 2017
#Due Date and Time: October 23, 2017
#Description: This is a quest game! - Version 1
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

import random

########################QUESTS################################################
def printstuff(inventory, money, health):
    print('Our hero has the following items: ', inventory)
    print('He has the following financial resources:')
    for typemoney in list(money.keys()):
        print(typemoney, " : ", money[typemoney])













##############################MAIN####################################################

print("Welcome to the Hero Quest game, the best adventure game from CIT 135.")
play = input('Would you like to play the game? (Y/N)').lower()

hero = ''
inventory = []
money = {'gold': 0, 'silver': 0, 'bronze': 0}
health = 100
if hero == "":
    hero = input('Please input a name for your hero: ')

askit = input(hero + """ is riding a monster called 'Champ' in the middle of Lake Champlain\n
He is enjoying the sunshine with his eyes closed and suddenly a huge chest drops into the water.\n
Should our hero approach the chest and open it? (Y/N)""")

if askit == 'y':
    print("""The chest contains:
    \t - A healing potion
    \t - Poisonous gas in a cylinder
    \t - 10 Bronze Coins
    \t - Hilt
    \t - Baseball Bat""")

money['bronze'] += 3
print('Our hero now has the following items:', inventory)
printstuff(inventory, money, health)