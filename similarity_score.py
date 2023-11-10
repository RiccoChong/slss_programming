# Calculating similarity score
# Author: Ricco Chong
# Date: 09 November 2023

# Calculate similarity scores between two people.

# Create two lists that represent the movies that they like
ubials_fave_movies = [
    "the matrix", 
    "avengers: infinity war", 
    "internal affairs", 
    "rogue one", 
    "the empires strikes back"
]
bens_fave_movies = [
    "thomas and friends, big world big adventure", 
    "paddington 2",
    "avengers:infinity war",
    "minions",
    "rogue one"
]

similarity_score = 0

# For every movie in the first list 
    # if that movie is in the second list
        # Increase the similarity score by 1
for movie in ubials_fave_movies:
    if movie in bens_fave_movies:
        similarity_score += 1

# Display the results
print("The similarity score between the users is:")