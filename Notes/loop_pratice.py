# Loop Pratice
# Author: Miles Ty
# Date: Oct 10th, 2023

import random
import time

# Create a list of groceries 
groceries = ["hot wheels", "Lego", "Ice Cream","Video Games"]
# Do something for each thig from the list
# Print it out in a pretty way

for item in groceries:
    print(f"* {item}")
    print(" ---")

    # Create a pyramid like this using a for loop
    
    # *
    # **
    # ***
    # ****
    # *****

    stars = ["*", "**", "***", "****", "*****"]
    for row in stars:
        print(row)

    # Problem:
    # Create a new years eve countdown
    # Requirements:
    # * Countdown every second
    # * Instead of zero it says happy new year

    countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Year"]
    for timer in countdown:
        print(timer)
        time.sleep(1)

