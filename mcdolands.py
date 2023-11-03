# mcdolands question 3
# author: miles
# date: nov 3, 2023

food_cost = 0 

# Ask the user what their order is and if they say yes add money if no dont add money to the total

print("Would you like a burger for $5? (Yes/No)")
burger_food = input().strip(",.?! ").lower()
if burger_food == "yes":
    food_cost += 5

print("Would you like a fries for $3? (Yes/No)")
fries_food = input().strip(",.?! ").lower()
if fries_food == "yes":
    food_cost += 3

tax_cost = food_cost *0.14

print(f"that would be {food_cost + tax_cost:.2f}$")