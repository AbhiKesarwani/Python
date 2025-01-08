print("Welcome to the Stone,Paper and Scissor Game!")

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
import random

choices = [rock,paper,scissors]
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
if user_choice < 0 or user_choice > 2:
    print("Invalid Input")
else:
    print(choices[user_choice])              #printing graphic of user choice
    computer_choice = random.randint(0,2)    #computer choosing its choice
    print("Computer chose: ")
    print(choices[computer_choice])           #printing graphic of user choice

    #defining rules to loose,win and draw game.
    if user_choice == computer_choice:
        print("Game is Draw.")
    elif user_choice == 0 and computer_choice == 1:
        print("Computer won the game.")
    elif user_choice == 1 and computer_choice == 2:
        print("Computer won the game.")
    elif user_choice == 2 and computer_choice == 0:
        print("Computer won the game.")
    else:
        print("You won the game.")





