# Star Wars Bot
# Name: Miles Ty
# Date: Oct 16th, 2023

import time

# Describe the purpose of the bot
print("I'm a star wars bot that will decide wether you should be on the dark of light side")
time.sleep(3)
print("These questions will determine which side you belong to")
time.sleep(2)
# Ask the user if you like capes and if they like the colour red
cape = input("do you like capes?")
time.sleep(1)
red_colour = input("do you like the colour red?")
if red_colour.lower().strip("!,.?") == "yes":
    print("hmmm, the dark side seems like a good fit for you")
if cape.lower().strip("!,.?") == "yes":
    print("hmmm, the dark side seems like a good fit for you")
elif cape and red_colour.lower().strip("!,.?") == "no":
    print("may you be in the path of the light")
else: print("light side it is")