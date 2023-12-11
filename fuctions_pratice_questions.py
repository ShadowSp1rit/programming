# Functions Questions #1-4
# Author: Miles Ty
# Date: Nov 27th, 2023


# Question 1

# Write a function called stars()

# Make the function take an int as a parameter.

# It then returns a string of stars with the same length as the argument


def stars(num_stars: int) -> str:
    """Returns a number of stars

    Params:

    num_stars - the number of stars to return
    """

    return "*" * num_stars

print(stars(5))


# Question 2

# Write a function that TAKES THREE NUMBERS

# it should RETURN THE BIGGEST of the three numbers

# Call it "biggest_of_three"

def biggest_of_three(num_one: float, num_two: float, num_three: float) -> float:
    """Calculates the highest number out of three inputs.
    Result is the highest number.
    
    Params:
    num_one - the first number
    num_two - the second number
    num_three - the third number
    
    Returns:
    the biggest of the three numbers
    """

    if num_one > num_two > num_three:
        return num_one
    elif num_two > num_three:
        return num_two
    else:
        return num_three

print(biggest_of_three(1000, 100, 10))
print(biggest_of_three(100, 1000, 10))
print(biggest_of_three(10, 100, 1000))

# Question 3
# Question 4
# Create functions called pyramid() and pyramid_mirror()
# Takes one number as a parameter
# Give a pyramid either regular way or mirrored

def pyramid(num_layers: int) -> None:
    """Prints out a pyramid of given number of layers.

    Params:
    num_layers - number of layers in the pyramid
    """

    for current_layer in range(1, num_layers + 1):
        print(stars(current_layer))


pyramid(2)
pyramid(3)
pyramid(20)


def pyramid_mirror(num_layers: int) -> None:
    """Prints out a mirrored pyramid.

    Params:
    num_layers - number of layers of pyramid
    """

    for current_layer in range(1, num_layers + 1):
        # Print the spaces then print the stars
        # num_layers == 2
        # " " * 1  +  stars(1)
        # " " * 0   + stars(2)
        # num_layers == 3
        # " " * 2  + stars(1)
        # " " * 1  + stars(2)
        # " " * 0  + stars(3)
        print(" " * (num_layers - current_layer) + stars(current_layer))


pyramid_mirror(4)
pyramid_mirror(20)