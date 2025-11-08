import random
from logo import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def choosing_card():
    '''Return a random card'''
    return random.choice(cards)

def calculate_score(user_option,computer_option):
    '''Calculate Score and decide winner'''
    computer_score = sum(computer_option)
    while computer_score<17:    #make computer score equal to 17 or more through adding card
        computer_card = choosing_card()
        computer_option.append(computer_card)
        computer_score = sum(computer_option)
    print(f"Computer Cards: {computer_option}")
    print(f"Computer's total score: {sum(computer_option)} ")
    user_score = sum(user_option)
    if user_score == computer_score:
        print("Draw 🙃")
    elif user_score > 21 and computer_score > 21:
        print("You went over. You lose 😤")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score > computer_score:
        print("You win 😃")
    else:
        print("You lose 😤")

game_start = input("Do you want to play Blackjack game, Type 'yes' or 'no': ")
def play_game():
    '''Game Procedure'''
    user_option = []
    computer_option = []  
    game_play = True
    while game_play:
        print(logo)
        print()
        if game_start.lower() == "yes":
            for _ in range(2):  
                user_card = choosing_card()
                computer_card = choosing_card()
                user_option.append(user_card)
                computer_option.append(computer_card)
            print(f"Your cards: {user_option}, Your current score: {sum(user_option)}\nComputer's first card: {computer_option[0]} ")
            card_further = True
            while card_further:       #Checking Blackjack condition for game over
                if len(user_option) == 2 and sum(user_option) == 21:
                    user_score = 0
                    game_play = False
                    print("You won,you got a Blackjack,Game Over!")
                    break
                if len(computer_option) == 2 and sum(computer_option) == 21:
                    computer_score = 0
                    game_play = False
                    print("You Loose,Computer Got Blackjack,Game Over!")
                    break
                
                further_card = input("Type 'yes' to get another card, type 'no' to pass: ")   #addition of card
                if further_card.lower() == "yes":
                    user_card = choosing_card()
                    computer_card = choosing_card()
                    user_option.append(user_card)
                    computer_option.append(computer_card)
                    print(f"Your cards: {user_option}, Your current score: {sum(user_option)}\nComputer's first card: {computer_option[0]} ")
                elif further_card.lower() == "no":
                    if 11 in user_option and sum(user_option) > 21:   #changing ace value
                        user_option.remove(11)
                        user_option.append(1)
                    print(f"Your cards: {user_option}, Your total score: {sum(user_option)}")
                    calculate_score(user_option,computer_option)
                    card_further = False
                    game_play = False
                else:
                    print("Invalid Input,Game Over!")
                    card_further = False
                    game_play = False
        elif game_start.lower()=="no":
            print("Thank You")
            game_play = False
        else:
            print("Invalid Input,Try again")
            game_play = False


play_game()
is_game_again = True
while is_game_again: 
    game_again = input("\nDo you want to play game again, Type 'yes' or 'no': ")
    if game_again.lower() == "yes":
        play_game()
    else:
        print("Thank You for playing.")
        is_game_again = False



'''
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

'''

