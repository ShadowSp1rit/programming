# Chatbot
# Author: Miles Ty
# Date: Sept 21, 2023

# Greet the user
print("Hello there! 🤖")
print("I'm a crude chatbot, here to talk to you")

# Get the user's name and store in a variable
user_name = input("So... what's your name?")

# Respond with the uer's name
print(f"It's nice to meet you, {user_name}!")

# Ask the user what their favourite food is 
fave_food = input(f"{user_name} what's your favourite food?")

# Respond with something that is NOT TOO repetetive

# Create a list of appropriate response
list_of_fave_food_responses = [
    "Mmmmmm, That sounds delicious.",
    f"Yes, {fave_food} is one of my favourites too.",
    "DAMNNN."
]
# Choose one response randomly from the list
import random
random_response = random.choice(list_of_fave_food_responses)
# Print out the chosen response
print(random_response)