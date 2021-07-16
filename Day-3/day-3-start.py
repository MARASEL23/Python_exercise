""""
print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm?\n> "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

***********************************************************************************

print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm?\n> "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("\nPlease enter your age to find out the price.\n> "))
    if age > 18:
        print("The fee you will pay is $12.")
    else:
        print("The fee you will pay is $7.")
else:
    print("Sorry, you have to grow taller before you can ride.")
********************************************************************************
"""
print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm?\n> "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("\nPlease enter your age to find out the price.\n> "))
    if age < 12:
        print("The fee you will pay is $5.")
    elif age <= 18:
        print("The fee you will pay is $7.")
    else:
        print("The fee you will pay is $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
