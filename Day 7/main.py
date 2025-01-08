#my_code
from hangman_art import logo, stages
from hangman_words import word_list
import random
print(logo)
word = random.choice(word_list)  #choosing the word
print(word)

letter_list = []
for _ in range(len(word)):
    letter_list.append("_")    #making list of blank length of the word

lifes = 6

game_is_on = True
while game_is_on:
    guessed_letter = input("Guess a letter: ")
    print(stages[lifes])
    if guessed_letter not in word:
        if lifes == 0:
            game_is_on = False
            print("Game Over.You are out of lives.")
        if lifes > 0:      #tracking lifes
            print(f"Wrong Guess.Lives remaining {lifes - 1}")
        lifes -= 1
    elif guessed_letter in word:
        if guessed_letter in letter_list:
            print("This letter you already guessed previously.")
        for index in range(len(letter_list)):
            letter = word[index]
            if letter == guessed_letter:
                letter_list[index] = guessed_letter        #putting guessed letter in list
        print(f"You Guessed right.\n{letter_list}")
        if "_" not in letter_list:
            print("Yon won the Game.")
            game_is_on = False
