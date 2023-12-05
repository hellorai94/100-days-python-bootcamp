# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

dic_operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
      '/': divide}

# function = dic_operations["+"]
# function(2,3)
from art import logo

def calculator():
    print(logo)
    num_one = float(input("What's the first number? "))
    for symbol in dic_operations:
        print(symbol)
    operation = input("What operation do you want to make? ")
    num_two = float(input("What's the second number? "))
    function = dic_operations[operation]
    answer = function(num_one, num_two)

    print(f"{num_one} {operation} {num_two} = {answer}")

    while True:
        another = input("Do you want make more operations? If yes, type'Y'. If you want new calculation type 'N' ")
        if another == 'Y' or another == 'y':
            for symbol in dic_operations:
                print(symbol)
            operation = input("What operation do you want to make? ")
            num_three = float(input("What's the next number? "))
            function = dic_operations[operation]
            last_answer = answer
            answer = function(answer, num_three)
            print(f"{last_answer } {operation} {num_three} = {answer}")
        elif another == 'N' or another == 'n':
            calculator()

calculator()

