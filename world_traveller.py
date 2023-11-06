# World Traveller Bot
# Author: Miles Ty
# Date: November 6th, 2023

continents_explored = 0

NUM_RESPONDENTS = 7

# Ask for the user's name and greets them

user_name = input("Hello, i'm a world traveller bot, what's your name?")
print (f"oh hello {user_name} I would like to ask you 7 questions and I will tell you how much of the world you've been to")

# Ask the user if they been to 7 of the continents in the world they respond with yes or no

for _ in range(NUM_RESPONDENTS): questions = ["Have you been to Europe? (Yes| No)", 
                                              "Have you been to North America? (Yes| No)",
                                              "Have you been to South America? (Yes| No)",
                                              "Have you been to Australia? (Yes| No)",
                                              "Have you been to Africa? (Yes| No)",
                                              "Have you been to Asia? (Yes| No)",
                                              "Have you been to Antarctica? (Yes| No)"]

for question in questions:
    print(question)
    response_question = (input().strip(",.?! "))
    if response_question.lower().strip(",.?! ") == ("yes"):
        continents_explored += 1
    
# Print how many contients they've been to afterward

print(f"You have been to {continents_explored}/7 continents")