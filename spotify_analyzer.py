# Spotify Data Analyzer
# Author: Ricco Chong
# 16 janurary 2023 

# Version 0.1
#   - from the data set, get all the songs performed by Drake

import csv

def find_all_songs(artist: str) -> list:
    """Returns a list of all songs from a given artist
"""

    # Open up the file
    with open ("./spotify.csv") as f:
        # --- Look for all songs performed by Drake using linear search---
        # create a csv reader object
        csv_reader = csv.DictReader(f)

        # Create a list to store all Drake's songs
        drake_song = []

        # Create a counter for the current line number
        line_num = 0

        # for every song in the .csv file
        for line in csv_reader:
            # If this song is sung by Drake
            if "drake" in line["artist"].lower():
                # Add it to the song list
                song.append(line["artist"], line["song_title"], line["danceability"])
    
    return song


for song in drake_song:
    if float(song[-1]) >= 0.6:
        print(song)