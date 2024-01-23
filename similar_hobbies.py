# Similarity score
# Author: Ricco 
# Date: Nov 14 2023

common_similarities = 0

# Input all hobbies of the user
print("please enter hobbies, seperate by spaces")
p_1 = input("Person 1: ").lower().split()
p_2 = input("Person 2: ").lower().split()

# make an if statement and compare the users answer 
if p_1[0] in p_2:
    common_similarities += 1
if p_1[1] in p_2:
    common_similarities += 1
if p_1[2] in p_2:
    common_similarities += 1

#print the answers
print(f":You have {common_similarities} in common!")