# Robot Puppy
# Miles Ty
# 12 Jan 2024

from PIL import Image
import colour_helper

# import the image
red_ball_img = Image.open("./Images/Red Ball.jpeg")

RED_PIXEL = (244, 59, 65)
red_pixels = []

# use colour helper to assist in finding the red ball
# Find the location of red pixels in the image.
for y in range(red_pixels):
    for x in range(red_pixels):
        # Get the pixel information
        current_pixel = red_ball_img.getpixel((x, y))

        # Detect the current pixel's colour
        if colour_helper.pixel_to_name(current_pixel) == "red":
            red_pixels.append((x, y))
mid_point = RED_PIXEL
orig_image_width = red_pixels.width
orig_image_height = red_pixels.height

red_pixel_midpoint = Image.new("RGB", (orig_image_width, orig_image_height))
ball_coordinates = mid_point in red_pixels
print(ball_coordinates)
# calculate the x and y axis for the mid-point of the red ball
most_left_red_pixel = red_pixels
most_right_red_pixel = red_pixels
diameter = most_left_red_pixel and most_right_red_pixel / 2 
# distance from the left to 
# right divided by 2 to get the middle point
# issue is - Don't know a solution to figuring out the most left and most right side of the red ball.
