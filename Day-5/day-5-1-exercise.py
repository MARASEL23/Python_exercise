"""
Instructions

You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 height's in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer.
You should try to replicate their functionality using what you have learnt about for loops.
"""
student_height = input("Input a list of student heights\n> ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

total_height = 0
for height in student_height:
    total_height += height
number_of_students = 0
for student in student_height:
    number_of_students += 1
# total_height = sum(student_height)
# number_of_students = len(student_height)
average_height = round(total_height / number_of_students)
print(f"The average size of the class is {average_height}!")
