import random
# 1 Make the welcome text
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if difficulty == 'easy':
    count = 10
else:
    count = 5

# 2 Make a randonic number
number = random.randrange(1, 101)
print(number)
# Make the condition about the difficulty
winner = False

while not winner:
    guess = int(input("Make a guess:"))
    if difficulty == 'easy':
        print(f"You have {count} attempts remaining to guess the number.")
        count -= 1
        if count == 10:
            print("You lost")
            break
    else:
        print(f"You have {count} attempts remaining to guess the number.")
        count -= 1
        if count == 5:
            print("You lost")
            break
        if guess < number:
            print("To low.\nGuess again.")
        elif guess > number:
            print("To high.\nGuess again.")
        else:
            print("You're right!")
            break
        
