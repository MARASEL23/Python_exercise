"""
Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.

https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

Warning you should round the result to the nearest whole number.
The interpretation message needs to include the words in bold from the interpretations above.
e.g. underweight, normal weight, overweight, obese, clinically obese.
"""
print("Welcome to BMI 2.0 Calculator")
weight = float(input("Enter your weight(kg):\n> "))
height = float(input("Enter your height(cm):\n> "))
height_m = height / 100
bmi = round(weight / (height_m ** 2), 2)

if bmi <= 18.5:
    print(f"Your body mass index: {bmi}")
    print("Your index is below 18.5. You are too weak.")
elif 18.5 < bmi <= 25:
    print(f"Your body mass index: {bmi}")
    print("Your index is between 18.5 and 25. Your weight is normal.")
elif 25 < bmi <= 30:
    print(f"Your body mass index: {bmi}")
    print("Your index is between 25 and 30. You are slightly overweight.")
elif 30 < bmi <= 35:
    print(f"Your body mass index: {bmi}")
    print("Your index is between 30 and 35. You are obese.")
else:
    print(f"Your body mass index: {bmi}")
    print("Your index is above 35. Clinically obese.")
