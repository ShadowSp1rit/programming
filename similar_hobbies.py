# Similar Hobbies Machine
# Author: Miles Ty
# Date: Nov 14th, 2023

# Create an input that allows the user to input 3 hobbies, which is asked twice
similarity_score = 0
print("Please enter 3 hobbies, seperated by spaces")
person_1_fav_hobbies = input().lower()
person_2_fav_hobbies = input().lower()
# Based on the favourites in person 1 and 2 lists if they are similar increase the similarity score by 1

for hobby in person_1_fav_hobbies:
    if hobby in person_2_fav_hobbies:
        similarity_score += 1

print(f"you have {similarity_score} hobbies in common")
