import random
import os 
from art import logo


def clear():
    os.system('cls')

def restart():
    restart_game = input("Do you want to restart the game? Put 'y' or 'n' ").lower()
    return restart_game

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

while True:
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append((deal_card()))
        computer_cards.append((deal_card()))

    def calculate_score(cards):
        """Take a list  of cards and return the score calculated from the cards"""
        if sum(cards) == 21 and len(cards) == 2:
            return 0    
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    while not game_over:
        user_score = calculate_score(cards=user_cards)
        computer_score = calculate_score(cards= computer_cards)
        print(f"Computer's first card: {computer_cards[0]}")
        print(f"User cards: {user_cards}")
        print(f"Current user score: {user_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Do you want to draw another card? - 'Y' or 'N'").lower()
            if another_card == "y":
                user_cards.append((deal_card()))   
            else:
                game_over = True
        
    while computer_score != 0 and computer_score < 17:
        computer_cards.append((deal_card())) 
        calculate_score(cards=computer_cards)
        computer_score = calculate_score(cards=computer_cards) 
        print(f"Computer cards: {computer_cards}")
        print(f"Current computer score: {computer_score}")  

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "It's a draw"
        elif computer_score == 0:
            return "You lose"
        elif user_score == 0:
            return "You win"
        elif user_score > 21:
            return "You lose"
        elif computer_score:
            return "You win"
        elif computer_score > user_score:
            return "You loser"
        else:
            return "You win"
        
    print(compare(user_score, computer_score))

    if restart() == "n":
        break
    else:
        clear()
