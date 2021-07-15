"""
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip : There are 2 ways to round a number. You might have to do some Googling to solve this.💪
"""
print("Welcome to tip calculator.")
bill = float(input("What was the total bill?\n> $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?\n> %"))
split = str(input("How many people to split the bill?\n> "))
money_percentage = (bill * percentage) / 100
pay = round((bill + money_percentage) / float(split),2)
print(f"Each person should pay: ${pay}")
print("Thanks for choosing us!")