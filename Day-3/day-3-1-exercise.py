"""
Instructions

Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

e.g. 86 is even because 86 ÷ 2 = 43

43 does not have any decimal places. Therefore the division is clean.

e.g. 59 is odd because 59 ÷ 2 = 29.5

29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

e.g.

6 ÷ 2 = 3 with no remainder.
"""

print("Welcome to Odd or Even calculator!")
num = int(input("Which number do you want to check?\n> "))
detector = num % 2

if detector == 0:
    print("Your number is an even number.")
else:
    print("Your number is an odd number.")
