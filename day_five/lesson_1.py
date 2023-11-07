# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height = sum(student_heights)
number_students = len(student_heights)

average = 0

# Write your code below this row 👇
for height in student_heights:
    average += height

average_final = round(average / number_students)

print(f"total height = {total_height}")
print(f"number of students = {number_students}")
print(f"average height = {average_final}")


