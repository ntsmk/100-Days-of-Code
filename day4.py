import random

# create variables
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
com_choice = random.randint(0,2)

# ascii art
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
# user choice output
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("please enter 0 or 1 or 2")

# computer choice output
print("Computer chose:")
if com_choice == 0:
    print(rock)
elif com_choice == 1:
    print(paper)
elif com_choice == 2:
    print(scissors)

# scenario of user chose rock
if user_choice == 0 and com_choice == 0: # rock vs rock
    print("Draw")
if user_choice == 0 and com_choice == 1: # rock vs paper
    print("You lose")
if user_choice == 0 and com_choice == 2: # rock vs scissors
    print("You win")

# scenario of user chose paper
if user_choice == 1 and com_choice == 0: # paper vs rock
    print("You win")
if user_choice == 1 and com_choice == 1: # paper vs paper
    print("Draw")
if user_choice == 1 and com_choice == 2: # paper vs scissors
    print("You lose")

# scenario of user chose scissors
if user_choice == 2 and com_choice == 0: # scissors vs rock
    print("You lose")
if user_choice == 2 and com_choice == 1: # scissors vs paper
    print("You win")
if user_choice == 2 and com_choice == 2: # scissors vs scissors
    print("Draw")