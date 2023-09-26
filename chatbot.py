# Chatbot
# Author: Miles Ty
# Date: Sept 21, 2023

import random
import time

# Greet the user
# Pause in between lines of dialogue 
print("Hello there! 🤖")
time.sleep(2)
print("I'm a crude chatbot, here to talk to you")
time.sleep(1.5)

# Get the user's name and store in a variable
user_name = input("So... what's your name?")
time.sleep(2)

# Respond with the uer's name
print(f"It's nice to meet you, {user_name}!")
time.sleep(2)

# Ask the user what their favourite food is 
fave_food = input(f"{user_name} what's your favourite food?")
time.sleep(2)
# Respond with something that is NOT TOO repetetive

# Create a list of appropriate response
list_of_fave_food_responses = [
    "Mmmmmm, That sounds delicious.",
    f"Yes, {fave_food} is one of my favourites too.",
    "DAMNNN.",
    "WOW",
]
# Choose one response randomly from the list
random_response = random.choice(list_of_fave_food_responses)
# Print out the chosen response
print(random_response)