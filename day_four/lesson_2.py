names_string = input()
names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random

num_items = len(names)
random_bill = random.randint(0, num_items - 1)
name = names[random_bill]

print(f"{name} is going to buy the meal today!")
