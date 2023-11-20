# Parental Bot
# Author: Ricco
# Date: 16 November 2023

# Greet the user
print("Hey!")

list_of_questions = ["Did you eat? (yes or no): ", "Did you study? (yes or no): ", "Did you do your laundry? (yes or no): ", "Did you call grandma? (yes or no): "]

score = 0

for answer1 in list_of_questions:
    # Get answer from the user
    answer = input(answer1).lower()

    if answer == "yes":
        score += 1

# Make the total
if score >= 3:
    print("Good!")
elif score >= 1 < 3:
    print("Ok")
else:
    print("I'm coming over.")