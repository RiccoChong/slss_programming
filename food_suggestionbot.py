# Food Suggestion Bot
# Author: Ricco Chong
# Date: 6 Oct 2023

# A bot that asks the user what their favourit food is.
# The bot identifies the type/cuisine of the food and offer a suggestion for a resaurant.

import random
import time

# Introduce the bot to the user
# Ask the user what their favourite food is.
print("Hello, I am here to suggest a restaurant to you.")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me what your favourite food is.")
time.sleep(1)

# If they answer with an Italian dish
# Offer a suggestion to a Italian restaurant
#list all thhe italian dishes
# Add one more cuisine/type/etc
# Test it to see if it works
italian_food = ["pizza", "pasta", "canneloni", "tiramisu"]
japanese_food = ["udon", "sushi", "nigiri", "ramen"]

if fave_food.lower().strip(" ,.?!") in italian_food:
    print("I think that you might like Italian food. ")
    time.sleep(1)
    print("I suggest Bella Roma Italian Ristorante Richmond. ")
    print("You can find the address below.")
    print("8368 Alexandra Rd, Richmond")
elif fave_food.lower().strip(",.?!") in japanese_food:
    print("Hmmm, thats japanese food!")
    time.sleep(1)
    print("How about a japanese resteraunt, i suggest Gami Sushi in Richmond!")
    print("You can find the address below.")
    print("10111 No. 3 Rd #126, Richmond, BC V7A 1W6")
else:
    print("Sorry. I don't reconize your favourite food.")
    print("My algorithm is still being worked on.")
    time.sleep(1)
    print("I cant help you, sorry! ")