# Olympic Judging 
# Author: Miles
# Date: Nov 2nd, 2023
NUM_RESPONDENTS = 5
# Greet the user
print("Please answer the following question")
# Create a list of questions to ask
for _ in range(NUM_RESPONDENTS): questions = ["On a scale of 1 to 10 how were they?",
                                              "On a scale of 1 to 10 how were they?",
                                              "On a scale of 1 to 10 how were they?",
                                              "On a scale of 1 to 10 how were they?",
                                              "On a scale of 1 to 10 how were they?"]
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
print(f"The average score of this person is: {average_rating:.2f} / 10")