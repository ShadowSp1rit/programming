# AOC Day 1
# Author: Miles Ty
# 30 November 2023

# There is one elf carrying the max calories
# How many calories does that elf

# Create a list that holds all the calories of the
# Elves

elves = []

# Open the file "f" is the name that we give the file
with open("aoc2022day1.txt") as f:
    # Calories of the current elf
    current_cals = 0

    for line in f:
        # IF there is something in the line
        if line.strip():
            current_cals += int(line.strip())
        else:
            # dump current_cals into elves list
            elves.append(current_cals)


            # reset current_cals for the next elf
            current_cals = 0

print(elves)
print(max(elves))
print(sorted(elves))

# get the top three elves
sorted_elves = sorted(elves)
top_three = sorted_elves[-3:]
top_three_total = sum(top_three)
print(sum(sorted(elves)[-3:]))









