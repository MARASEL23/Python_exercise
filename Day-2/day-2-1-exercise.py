"""
Instructions

Write a program that adds the digits in a 2 digit number.
e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on lines 1-3.
Your program should work for different inputs. e.g. any two-digit number.
"""

digit_number = input("Enter two digit number : ")
first_num = int(digit_number[0])
second_num = int(digit_number[1])
result = first_num + second_num
print("Result : " + str(first_num) + " + " + str(second_num) + " = " + str(result))
