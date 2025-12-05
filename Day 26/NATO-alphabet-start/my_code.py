import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_on = True
while is_on:
    user_word = input("Enter the word: ").upper()
    try:
        output_list = [new_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters are allowed in input please.")
    else:
        print(output_list)
        is_on = False
