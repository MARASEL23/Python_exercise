"""
Instructions

I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days,
weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly,
even the positions of the commas and full stops.
"""

print("Welcome to Your Life in Weeks")
estimated_age = 90
age = int(input("Enter your age : "))
remaining_life = estimated_age - age
days = remaining_life * 365
week = remaining_life * 52
month = remaining_life * 12
print(f"Your estimated lifespan {days} days, {week} weeks, {month} months left.")
