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
child = 5
young = 7
adult = 12
prize = 0
photo_prize = 3
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("\nPlease enter your age to find out the price.\n> "))
    if age < 12:
        prize += child
    elif age <= 18:
        prize += young
    else:
        prize += adult
else:
    print("Sorry, you have to grow taller before you can ride.")

photo = (input("Do you want to photograph? Y or N\n> "))

if photo == "Y" or "y":
    prize += photo_prize
    print(f"The fee you have to pay : {prize}")
elif photo == "N" or "n":
    print(f"The fee you have to pay : {prize}")
else:
    print(f"You keyed wrong. Your fee: {prize}")
