# Name:         Tamarah Binek
# OSU Email:    binekt@oregonstate.edu
# Course:       CS361 - Software Engineering I
# Assignment:   9 - Microservice for Book App
# Due Date:     31 July 2023
# Description:  A program that, given a descriptive string ("Sort by Title", "Sort by Author", "Sort by Order_a", "Sort by Order_d"), returns
#               the set of books sorted (Sort Service)
# Description:  A user interface (UI) that either has a button or
#               can receive a user command. When the button is pushed or the command is entered.
#                   (a) UI calls the  Service
#                   (b) UI calls the Sort Service using the

import time
import os
data = str([[1, 'Little Women', 'Louisa May Alcott'], [2, 'Pride and Prejudice', 'Jane Austen'], [5, "The Handmaid’s Tale", 'Margaret Atwood'], [3, 'The Hunger Games', 'Suzanne Collins'], [4, 'Where the Crawdads Sing', 'Delia Owens']])
while True:
    user_input = input("Please enter the type of sort you want ('Sort by Title', 'Sort by Author', 'Sort by Order_a' or 'Sort by Order_d'): ")

    if user_input == 'Sort by Title' or user_input == 'Sort by Author' or user_input == 'Sort by Order_a' or user_input == 'Sort by Order_d':
        with open("sort.txt", 'w') as sort_file:
            sort_file.write(user_input + "\n")
            sort_file.write(data)
        time.sleep(5)

    else:
        print("Unknown Option")
