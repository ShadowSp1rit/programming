# Chip Rater
# Author: Miles
# 2 November 2023

# Interview people about their 
# perception of the deliciousness
# of potato chips
# we will ask them a set of questions
# we'll give an aggregate score

# Greet the user
print("Please answer the following questions")
# Create a list of questions to ask
questions = ["How crispy is the chip on a scale from 1 to 5? 5 being crispy and 1 being mushy", 
             "How would you rate the taste from 1 to 5? 5 is the best chip ever, and 1 being id rather eat dirt",
             "From 1 to 5, how would you rate the packaging? 5 is i would just buy this for the packaging, and 1 is someone got paid to put this together?"]
# For every question in that list, ask a question, get the user's rating, and add the rating for the total-rating

total_rating = 0

for question in questions:
    print(question)
    user_rating = int(input().strip(",.?! "))
    total_rating += user_rating

# Do some maths
# Use the average score to represent the chip's rating
average_rating = total_rating / len(questions)
# Present the results
print(f"The average score of this chip is: {average_rating:.2f} / 5")