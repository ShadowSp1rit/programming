# Functions and Turtle
# Author: Miles Ty
# 28 November 2023

import turtle

alfred_river_wilson = turtle.Turtle()
alfred_river_wilson.color("lightblue")
alfred_river_wilson.shape("turtle")
alfred_river_wilson.shapesize(35)

def squared(num: float) -> float:
    """Returns the given number squared"""
    return num**2


def draw_square(side_length: float) -> None:
    for _ in range(4):
        alfred_river_wilson.forward(side_length)
        alfred_river_wilson.left(90)


alfred_river_wilson.speed(0)

# Create squares that get bigger and bigger
# Draws from 1 until 19
for i in range(40):
    draw_square(squared(i))

turtle.done()

