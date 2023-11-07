# Worldd Traveller
# Name: Ricco Chong
# Date: Nov 6 2023

import time 

# grreet the user
name = input("Hello traveller, whats your name?")
time.sleep(1)
print(f"Hello {name}, nice to meet you!")
time.sleep(1)
print("Just so you know, please answer in yes or no!")

 # Ask the user questions
list_of_continents = [
    "North America | ",
    "South America | ",
    "Asia | ",
    "Africa | ",
    "Europe | ",
    "Australia | ",
    "Antartica | "
]

total_score = 0

answer = ["YES"]

# For every answer from the list
for continent in list_of_continents:
    time.sleep(1)
    answer = input(continent).lower()

    # get the users rating
    if answer == "yes".lower():
        total_score += 1

# output the answer
print(f"You have been to {total_score} / 7 continents")