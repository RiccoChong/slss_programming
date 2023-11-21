# Turtle examlple
# Author: Ricco
# 21 november 2023

import turtle

# --- CONSTANTS ---
TURTLE_MAGNITUDE = 20

# Create a tutle
michaelangelo = turtle.Turtle()

# Get some instructions from the user
print("""To give commands, type:
F - to go forward
L - to go left
R - to go right
B - to go backwards
Stop - to stop the program""")

# Repeat the below code INDEFINITELY
done = False

while not done:
    command = input("Where should i go? ").strip(",./? !@#$").lower()

    # Based on those instructions, move the tutle on the screen
    # if the user says stop, quit the loop
    if command in ["f", "forward"]:
        michaelangelo.forward(TURTLE_MAGNITUDE)
    elif command in ["l", "left"]:
        michaelangelo.left(90)
    elif command in ["r", "right"]:
        michaelangelo.right(90)
    elif command in ["b", "backward"]:
        michaelangelo.backward(TURTLE_MAGNITUDE)
    elif command == "stop":
        done = True
