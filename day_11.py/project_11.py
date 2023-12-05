import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

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

user_score = calculate_score(cards= user_cards)
computer_score = calculate_score(cards= computer_cards)
print(f"Computer's first card: {computer_score}")
_
if user_score == 0 or computer_score == 0 or user_score > 21:
    game_over = True

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

