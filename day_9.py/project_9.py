import os
from art import logo

def clear():
    os.system('cls')

print(logo)
bidders = {}

while True:
    name = input("What is your name?")
    bid = int(input("What's your bid?"))
    bidders.update({(name, bid)})
    choose = input("Are there any other bidders Type 'yes' or 'no' ")
    if choose == "no":
        break
    else:
        clear()
        
max_key = max(bidders, key=bidders.get)
max_bid = bidders[max_key]

print(f"The winner is {max_key} with a bid of ${max_bid}.")

