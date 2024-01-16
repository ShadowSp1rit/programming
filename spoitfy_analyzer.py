# Sportify Analyzer
# Miles Ty
# Jan 16 2024

# Version 0.1
# - From the data set, get all the songs
# - performed by Drake

import csv


# Open up the file
with open("spotify.csv") as f:
    # ----- Look for all songs performed by Drake
    #       using linear search
    # Create a csv reader object
    csv_reader = csv.DictReader(f)

    # Create a list to store all Drake's songs
    drake_songs = []
    # Create a counter for the current line number


    # for every song in the .csv file
    for line in csv_reader:
        print(line)

        # if this song  is sung by Drake
        if "drake" in line["artist"].lower():    
            # add it to the Drake list
            drake_songs.append(
                (line["artist"], line["song_title"], line["danceability"])
            )

for song in drake_songs:
    print(song)

# Print out all songs that have
    # a danceability of >+ 0.6


for song in drake_songs:
    if float(song[-1]) >= 0.6:
        print(song)
