# Stars wars bot
# Auther: Ricco Chong
# Date: 10/16/08

import time
import random

# Introduce the bot and what it will do
print("Hello! ")
time.sleep(1)
print("I'm a star wars bot and my job is to determind what side you should join!")
time.sleep(2.5)
print("Alright, lets get started! " )
time.sleep(1)

# start asking information
fav_colour = input ("Is your favourite colour red? ").lower().strip("!?,.")
time.sleep(1)
like_cape = input("How about capes, do you like them? ").lower().strip("!?,.")

# recomend what side you should be on (light or dark)
if fav_colour == "yes" and like_cape == "yes":
    print("Great...")
    time.sleep(1)
    print("welcome to the dark side ")
elif fav_colour == "yes" and like_cape == "no":
    print("Yes...")
    time.sleep(1)
    print("Welcome to the dark side")
elif fav_colour == "no" and like_cape == "yes":
    print("Yes...")
    time.sleep(1)
    print("Welcome to the dark side")
else:
    print("Light side, I see...")