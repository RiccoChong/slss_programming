# SFUs Best - Similarity Score
# Author: Ricco
# 10 November 2023

# Load data from a file
# "read" in a meaningful way
# Link our sim score algo to the data

# Open the file
with open("./data.csv") as f:
    f.readline()

    # The second line of the csv file
    print(f.readline())

# Create a "profile" of likes ( fave places in SFU )
profile = [
    "Bubble World",
    "Chef Hung",
    "Uncle Fatih's",
    "Guadalupe (MBC)",
    "Steve's Pole Bar"
]

# Initialize top score and their name
most_similar_score = 0
most_similar_name = ""

with open("./data.csv") as f:
    #Throw away the header
    header = f.readline()

    for line in f:
        # Convert the string to a list
        current_likes = line.split(",")

        # Store the person's name
        current_name = current_likes[1]

        # Initialize the current sim score
        current_sim_score = 0

        # For item in profile
        for item in profile:
            # if item in current line's likes
            if item in current_likes:
                # Increase sim score by 1
                current_sim_score += 1

        # Print the results from this line of data
        print(f"{current_name} - Score: {current_sim_score}")

        # Update the most similar person
        if current_sim_score < most_similar_score:
            most_similar_score = current_sim_score
            most_similar_name = current_name
        elif current_sim_score == most_similar_score:
            most_similar_name += f" {current_name}"

if current_name == 0:
    input(current_name)
print("---LEAST SIMILAR---")
print(f"{most_similar_name} - Score: {most_similar_score}")