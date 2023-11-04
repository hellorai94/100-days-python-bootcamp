print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

t = name1_lower.count("t") 
r = name1_lower.count("r") 
u = name1_lower.count("u") 
e = name1_lower.count("e") 

l = name1_lower.count("l") 
o = name1_lower.count("o")
v = name1_lower.count("v")
e_2 = name1_lower.count("e")

t_1 = name2_lower.count("t")
r_1 = name2_lower.count("r")
u_1 = name2_lower.count("u")
e_1 = name2_lower.count("e")

l_1 = name2_lower.count("l")
o_1 = name2_lower.count("o")
v_1 = name2_lower.count("v")
e_3 = name2_lower.count("e")


total_name1 = t + r + u + e + t_1 + r_1 + u_1 + e_1            
total_name2 = l_1 + o_1 + v_1 + e_3 + l + o + v + e_2
total = (str(total_name1) + str(total_name2))
end = int(total)

if end < 10 or end > 90:
    print(f"Your score is {end}, you go together like coke and mentos.")
elif end >= 40 and end <= 50:
    print(f"Your score is {end}, you are alright together.")
else:
    print(f"Your score is {end}.")
    





