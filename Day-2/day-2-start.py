"""
# Data Type's

# String
print("Hello"[0])

# Integer
print(123 + 345)

# Float
print(3.14159)

# Boolean
a = True
b = False

# Type Convert

# Converting from str to int
num_char = len(input("What is your name?\n> "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# Converting from int to str
print(str(36) + str(23))

# Mathematical Operations

#  2 + 1  ------> Addition
#  22 - 5 ------> Subtraction
#  3 * 2  ------> Multiplication
#  6 / 3  ------> Division
#  2 ** 2 ------> Exponents

# Number Manipulation
print(round(8 / 3, 2))
"""
# F Strings
score = 20.2
enemy = 2
isWinning = "Diamond"
print(f"Your score is {score}, your number of enemies killed {enemy}, your new rank {isWinning}.\n> Congratulations!")
