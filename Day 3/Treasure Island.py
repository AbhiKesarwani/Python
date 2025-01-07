print('''              
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''') #multiple line string is written in triple quotes
print("Welcome to Treasure Island Game.")
print("Your mission is to find the treasure.") 
#flow of the Game
first_choice = input("You're at a cross road.Where do you want to go? Type 'left' or 'right' ")
if first_choice == "left":
    second_choice = input("You come to a river.There is an island in the middle of the river. Type 'wait' to wait for a ship to come or 'swim' to swim across. ")
    if second_choice == "wait":
        third_choice = input("You arrived at the island safely.There is a house with 3 doors.One red, one yellow and one blue. Which color do you chose? ")
        if third_choice == "red":
            print('Burned by fire.Game Over.')
        elif third_choice == "blue":
            print("Eaten by beasts.Game Over")
        elif third_choice == "yellow":
            print("You won!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fallen into a hole.Game Over.")