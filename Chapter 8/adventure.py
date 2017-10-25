#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Python Quest Module Version One
#Date Assigned: Wednesday 10/18 @ 9:30am
#Due Date and Time: Wednesday 10/25 @ 11am
#Description: This is complete quest game using functions.
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

# Define the originals that will be used globally throughout the quests and functions.
inventory = []
money = {'gold': 0, 'silver': 0, 'bronze': 0}
health = 100
available_quests = {1: 'street', 2: 'jail', 3: 'outerspace'}

# Function that defines the quests and adds/removes money, inventory, and health. Returns to function caller.
def sj_quest(quest):
    if quest == "street":
        # List of items that are possible to be taken from the quest.
        possible_items = ['hammer', 'gun', 'knife', 'very big stick', 'a bag of nuts', 'some swag', 'a gold chain', 'some fresh items']

        # Alters the amount of money found randomly.
        money_found = {"gold": random.randint(0, 25), "silver": random.randint(0, 25), "bronze": random.randint(0, 25)}

        # Decides the amount of damage that should be taken from the player.
        damage_taken = random.randint(0, 50)

        items = []

        # Chooses the amount of items that should be taken.
        amount_of_items = random.randint(1, len(possible_items))

        # Picks the amount of items from the list, and adds them to a new list.
        while len(items) < amount_of_items:
            items.append(possible_items[random.randint(1, len(possible_items)-1)])

        return money_found, items, damage_taken

    if quest == "jail":
        possible_items = ['a guitar', 'a chair', 'some new clothes', 'a bag of chips', 'sunglasses', 'a broomstick']
        money_found = {"gold": random.randint(0, 10), "silver": random.randint(0, 10), "bronze": random.randint(0, 10)}
        damage_taken = random.randint(0, 25)

        items = []
        amount_of_items = random.randint(1, len(possible_items))
        while len(items) < amount_of_items:
            items.append(possible_items[random.randint(1, len(possible_items)-1)])

        return money_found, items, damage_taken

    if quest == "outerspace":
        possible_items = ['some cool space food', 'a piece of the moon', 'a very cool hat', 'shoes', 'a guitar', 'a star']
        money_found = {"gold": random.randint(0, 30), "silver": random.randint(0, 30), "bronze": random.randint(0, 30)}
        damage_taken = random.randint(0, 35)

        items = []
        amount_of_items = random.randint(1, len(possible_items))
        while len(items) < amount_of_items:
            items.append(possible_items[random.randint(1, len(possible_items)-1)])

        return money_found, items, damage_taken


# Prints the outro statements. Used for cleanliness.
def print_outro():
    print("\n##### THANKS FOR PLAYING! #####")
    print("The final items that " + character_name + " had were:")
    print("Current Inventory: " + str(inventory))
    print("Current Money: " + str(money['gold']) + " Gold, " + str(money['silver']) + " Silver, " + str(
        money['bronze']) + " Bronze")

# Prints the status of the character to the player. Includes health, inventory, and money.
def print_status():
    print("\nQuest Taken: " + available_quests[quest])
    print("Current Inventory: " + str(inventory))
    print("Current Money: " + str(money['gold']) + " Gold, " + str(money['silver']) + " Silver, " + str(
        money['bronze']) + " Bronze")
    print("Current Health: " + str(health) + '\n')

# Makes changes to the global variables after travelling through a quest. Deals with the return of information after sj_quest() is called.
def alter_attributes():
    for k, v in result[0].items():
        money[k] += v

    for item in result[1]:
        inventory.append(item)

# Introduction to the game. Tells the user what they've gotten into and asks if they want to play, and for a character name.
print("################################")
print("### Welcome to the SJ Quest! ###")
print("################################\n")
playing = input('Shall the SJ Quest begin? (Y/N): ').lower()
character_name = input("What would you like your character name to be?\n> ")
print("\n" + character_name + " is riding on a monster that has the ability to take him anywhere he desires.")
print("The monster may be evil, so we hope the monster will bring us somewhere good!")
print("In the hope to find loot and money, " + character_name + " could take a chance on the monster to travel.")

# Confirms the user actually wants to play during this risky-biz quest.
cont = input("\nWould " + character_name + " like to continue on his journey even while knowing the risks? (Y/N)\n> ").lower()
if cont == "y":
    while playing == "y":

        # Randomly selects a quest for the user to play.
        quest = random.randint(1, 3)
        result = sj_quest(available_quests[quest])

        # Alters health and determines if the player can continue if they haven't died.
        health -= result[2]
        if health > 0:
            alter_attributes()
            print_status()

            # Asks if the user would like to play the game again.
            playing = input("Would " + character_name + " like to venture on another quest to gain more items? (Y/N): ").lower()
        else:
            playing = "n"
            print("Oh no! You died!")

    print_outro()







