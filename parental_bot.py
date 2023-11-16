# Parental Bot
# Miles Ty
# Date: Nov 16th, 2023

# Create a Parental bot that asks 4 questions

# If the user responds with yes then the points will increase, and these points 
# influence the overall response later at the end of the code

# Ask the 4 questions
parental_points = 0
parental_question_1 = input("Did you eat? (Respond with yes/no)").lower()
parental_question_2 = input("Did you study? (Respond with yes/no)").lower()
parental_question_3 = input("Did you do your laundry? (Respond with yes/no)").lower()
parental_question_4 = input("Did you call your grandma? (Respond with yes/no)").lower()

if parental_question_1 == ("yes"):
    parental_points += 1
if parental_question_2 == ("yes"):
    parental_points += 1
if parental_question_3 == ("yes"):
    parental_points += 1
if parental_question_4 == ("yes"):
    parental_points += 1

if parental_points <1:
    print("I'm coming over")
elif parental_points <=2:
    print("Ok, not bad")
else:
    print("good job!")
