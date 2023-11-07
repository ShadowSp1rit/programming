# Semester Evaluation Bot
# Author: Miles Ty
# Date: Nov 6th, 2023

# ask the user how many courses they are taking and based on response, is the number of questions asked
total_rating = 0
num_courses = int(input("How many courses are you taking this semester? "))

# Use a for loop to collect ratings for each course
# Code below makes the user's imput from a range from 1, # of courses and it goes up by 1 everytime
for course in range(1, num_courses + 1): 
    rating = float(input(f"Rate course {course} out of 5: "))
    total_rating += rating

# Calculate the average rating
average_rating = total_rating / num_courses

# Provide a comment based on the average rating
if average_rating <= 1:
    comment = f"{average_rating:.2f}? Ouch."
elif average_rating <= 3:
    comment = f"{average_rating:.2f}? Not a bad semester."
else:
    comment = f"{average_rating:.2f}? Glad to hear that."

# Print overall comment based on evalutaion of the rating
print(comment)

