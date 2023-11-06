line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

position_list = [char for char in position]

valor_one = position_list[0].upper()
valor_two = position_list[1].upper()

list_horizontal = ["A", "B", "C"]
list_vertical =["1", "2", "3"]

index_horizonal = 0
index_vertical = 0


for indice, valor_h in enumerate(list_horizontal):
    if valor_h == valor_one:
        index_horizonal = list_horizontal.index(valor_h)
        
for indice, valor_v in enumerate(list_vertical):
    if valor_v == valor_two:
        index_vertical = list_vertical.index(valor_v)

map[index_vertical][index_horizonal] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

