# Turtle Example
# Author: Miles Ty
# 21 November 2023

import turtle

# ----- CONSTANTS
TURTLE_MAGNITUDE = 20

# Create a turtle
michaelangelo = turtle.Turtle()


# Get some instructions from the user
print("""To give commands, type:
F - to go forward
L - to turn left
R - to turn right
B - to go backwards""")

# Repeat the below code
done = False

while not done:
    command = input("Where should i go?").strip(",.?! ").lower()



        # Based on thoser instructions move the turtle
        # on the screen
        # If the user says stop quit the loop
    if command in ["f", "forward"]:
            michaelangelo.forward(TURTLE_MAGNITUDE)
    elif command in ["l", "left"]:
                michaelangelo.left(90)  
    elif command in ["r", "right"]:
                michaelangelo.right(90)
    elif command in ["b", "backwards"]:
                michaelangelo.backward(TURTLE_MAGNITUDE)
    elif command == "stop":
            done = True