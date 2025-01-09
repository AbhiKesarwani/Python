import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print("Welcome to the secret auction program.")

bid = {}    #creating empty dictionary
def auction():      #putting all the auction in a dictionary
    name = input("Enter your name? ")
    bid_amount = int(input("What's your bid?: $"))
    bid[name] = bid_amount

def bid_winner():  #comparing bids and declaring highest bidder
    highest_bid = 0
    for names in bid:
        if bid[names] > highest_bid:
            highest_bid = bid[names]
            highest_bidder_name = names
    print(f"The bid winner is {highest_bidder_name} with a bid of ${highest_bid}.")



is_game_on = True  #program
while is_game_on:
    print(logo)
    auction()
    move_further = input("Are there any other biddders? Type 'yes' or 'no': ")
    if move_further.lower() == "yes":
        is_game_on = True
        os.system('cls')
        print("Welcome to the secret auction program.")
        print(logo)
    elif move_further.lower() == "no":
        is_game_on = False
        os.system('cls')
        print(logo)
        bid_winner()
    else:
        print("Invalid Input")
        is_game_on = False

#TODO: Clear the previous bid in pycharm 