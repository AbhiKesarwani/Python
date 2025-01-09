
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
    , 'w', 'x', 'y', 'z']

def caesar(): #function for encryption
    if encryption.lower() == "encode":   
        sign = 1
    elif encryption.lower() == "decode":  
        sign = -1
    new_encrypted = ""
    for letter in message:   #encrypting message
        new_letter_index = alphabet.index(letter) + shift*sign
        new_encrypted += alphabet[new_letter_index]
    print(f"Here's the encrypted result: {new_encrypted}")

print('''          
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')

game_is_on = True
while game_is_on:
    encryption = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    if encryption.lower() == "encode" or encryption.lower() == "decode":
        message = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        while shift > 25:
            shift -= 25
        caesar()
        further_go_on = input("Type 'yes' if you want to go again.Otherwise Type 'no': ")
        if further_go_on.lower() == "yes":
            game_is_on = True
        elif further_go_on.lower() == "no":
            game_is_on = False
            print("Goodbye")
        else:
            print("Invalid Input")
            game_is_on = False
    else:
        print("Invalid Input")
        game_is_on = False