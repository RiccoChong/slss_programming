# Olymic_judging
# Ricco Chong
# nov 3 2023

import time

# greet the user
print("Hello. We will be judging you to determine your olympic scores")
time.sleep(1)
print("Each score is out of 10 points.")
time.sleep(1)
print("Half points are allowed!")
time.sleep(1)

# Create a list of questions to ask
decisions = [
    "Judge 1 = ",
    "Judge 2 = ",
    "Judge 3 = ",
    "Judge 4 = ",
    "Judge 5 = "
]

total_score = []

# For every answer from the list
for answer in decisions:
    print(answer)

    # get the users rating
    indiv_judge_score = float(input().strip(",.?! "))
    total_score.append(indiv_judge_score)

# find the average of all 5 judges
average = sum(total_score) / 5

# output the answer
print(f"The average score is {average}!!")