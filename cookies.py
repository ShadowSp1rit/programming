# Cookies
# Author:
# 21 November 2023

import turtle
import random

# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")


import random
import turtle

HEIGHT = turtle.window_height() // 2
WIDTH = turtle.window_width() // 2

# Make baker turtle
baker_turtle = turtle.Turtle()
baker_turtle.color("brown")
baker_turtle.fillcolor("brown")
baker_turtle.speed(0)


def make_cookie(x: int, y: int):
    """Draws a cookie on the screen at (x, y)

    Params:
    x - x-coordinate of the centre of cookie
    y - y-coordinate of the centre of cookie
    """
    # Set up the outline of the cookie
    baker_turtle.color("brown")
    baker_turtle.penup()
    baker_turtle.goto(-5 + x, -30 + y)
    baker_turtle.pendown()
    baker_turtle.begin_fill()
    baker_turtle.circle(30)
    baker_turtle.end_fill()
    baker_turtle.penup()

    # Add five chips
    baker_turtle.color("black")

    # Center
    baker_turtle.goto(0 + x, 0 + y)
    baker_turtle.stamp()

    # Top-right chip, bottom-right, bottom-left, top-left
    baker_turtle.goto(10 + x, 10 + y)
    baker_turtle.stamp()
    baker_turtle.goto(10 + x, -10 + y)
    baker_turtle.stamp()
    baker_turtle.goto(-10 + x, -10 + y)
    baker_turtle.stamp()
    baker_turtle.goto(-10 + x, 10 + y)
    baker_turtle.stamp()


make_cookie(100, 100)
make_cookie(0, 0)

for _ in range(1000):
    make_cookie(
        random.randint(-HEIGHT + 30, HEIGHT - 30),
        random.randint(-WIDTH + 30, WIDTH - 30),
    )

turtle.done()