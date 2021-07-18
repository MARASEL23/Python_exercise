import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_img = [rock, paper, scissors]
print("Welcome to Rock-Paper-Scissors Game!")
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n> "))
print(game_img[user_choose])
computer_choose = random.randint(0, 2)
print(f"Computer chose {computer_choose}")
print(game_img[computer_choose])
if user_choose >= 3 or user_choose < 0:
    print("You typed an invalid number, you lose!")
elif user_choose == 0 and computer_choose == 2:
    print("You Win!")
elif computer_choose == 0 and user_choose == 2:
    print("You Lose!")
elif computer_choose > user_choose:
    print("You Lose!")
elif user_choose == computer_choose:
    print("It's a draw!")
elif user_choose > computer_choose:
    print("You Win!")
