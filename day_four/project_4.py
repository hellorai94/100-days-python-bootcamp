import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choose >= len(game_images):
    print("You typed an invalid number, you lose.")
else:
    print(game_images[choose])

    print("Computer chose:")
    choose_computer = random.randint(0,2)
    print(game_images[choose_computer])

    if choose_computer == 0 and choose == 1:
        print("You won")
    elif choose_computer == 0 and choose == 2:
        print("You lose")
    elif choose_computer == 1 and choose == 0:
        print("You lose")
    elif choose_computer == 1 and choose == 2:
        print("You won")
    elif choose_computer == 2 and choose == 0:
        print("You won")
    elif choose_computer == 2 and choose == 1:
        print("You lose")
    else: 
        print("It's a draw!")
        






