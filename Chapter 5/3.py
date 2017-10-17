#Author: Adam Ferrante
#Class: CIT-135-01
#Assignment: Week Five Lab Practice Problems - Program 3
#Date Assigned: 9/27 @ 9AM
#Due Date and Time: 10/4 @ 9AM
#Description: This randomly selects blackjack numbers for the user and computer and plays them against each other.
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
playing = input("Would you like to play some Baby Blackjack? (Y/N): ").lower()

while playing == "y":
    # Pick two random cards for each player, the player and the dealer.
    user_card_one = random.randint(1, 11)
    user_card_two = random.randint(1, 11)
    dealer_card_one = random.randint(1, 11)
    dealer_card_two = random.randint(1, 11)

    # Calculate the totals for each player and store them in a variable.
    user_total = user_card_one + user_card_two
    dealer_total = dealer_card_one + dealer_card_two

    if user_total > dealer_total:
        print("YOU WIN! You had a total of " + str(user_total) + ". The dealer had a total of " + str(dealer_total))
    else:
        print("THE DEALER WON! The dealer had a total of " + str(dealer_total) + ". You had a total of " + str(user_total))

    playing = input("Would you like to play again? (Y/N): ").lower()