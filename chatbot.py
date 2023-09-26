 # Chatbot
 # Auther : Ricco Chong
 # Date : Sep 21 2023

import time
import random

# Greet the user
#pause in between lines of  dialogue
print("Hello there! ")
time.sleep(1)
print("i'm a crude chatbot, heres to talk to you. ")
time.sleep(1.5)

# Get the user's neame and store in a variable
user_name = input ("So... what's your name? ")
time.sleep(1)

# Respond with the user's name
print (f"it's nice to meet you, {user_name}! ")
time.sleep(2)
# Ask the user what their favourite food is
fave_food = input ("whats your favorite food? ")

# Respond with something appropriate(Respond with something that is not TOO repetitive)
# Create a list of appropriate responses
time.sleep(1)
list_of_fave_food_responses = [
    "Mmmmm. That sounds delicious.",
    f"Yes, {fave_food} is one of my favorites too!",
    "cool.",
    "intresting, i've never tried that before!"
]

# Choose one response randomly from the list 
randome_response = random.choice (list_of_fave_food_responses)

# Print out the chosen response
print(randome_response)
