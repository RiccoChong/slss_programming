# Loop Practice
# Author: Ricco Chong
# Date: 10 October 2023

import time

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Do something for each thing in the list
# print it out in a pretty way
for item in groceries:
    print(f"* {item}")
    print("  ---")

# Create a pyramid like this using a for loop.

#*
#**
#***
#****
#*****

stars =["*", "**", "***", "****", "*****"]

for item in stars:
    print(f" {item}")


# Problem:
# Create a new years eve countdown
# Requirements:
# * Starts off at 10
# * Countdown every second and print the second that it's at
# * Instead of reaching zero it sayss "Happy New Year"
# Example output:
#       10
#       9
#       8
#       ...
#       1
#       Happy new year!!

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Year!!"]

for item in countdown:
    print(f"        {item}")
    time.sleep(1)
    