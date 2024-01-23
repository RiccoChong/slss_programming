# Chip Rater
# Author: Ricco Chong
# 2 November 2023

# Interview people about their
# perception of the deliciousness
# of potato chips.
# We will ask them a set of
# questions. In the end,
# we'll give an aggregate score.

# Greet the user
print("Please answer the following questions on the chip you just ate.")

# Create a list of questions to ask
questions = [
    "How crispy is the chip on a scale from 1 to 5? 5 is very crispy, 1 is mushy.",
    "How would you rate the taste from 1 to 5? 5 is best chip ever. 1 is I'd rather eat dirt.",
    "From 1 to 5, how would you rate the packaging? 5 is I would buy this JUST for the packaging. 1 is Someone got paid to put this together?"
]

total_rating = 0

# For every question in that list
for question in questions:
    print(question)

    # Get the user's rating
    user_rating = int(input().strip(",.?! "))

    # Add the rating to some total-rating
    total_rating += user_rating

# Do some maths on the results
# Use the average score to represent the chip's rating
average_rating = total_rating / len(questions)

# Present the results
print(f"The average rating for this chip is: {average_rating:.2f} / 5")