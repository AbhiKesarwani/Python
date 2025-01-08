print("Welcome to the Python Password Generator!")
import random

alphabets_input = int(input("How many letters would you like in your password? "))
numbers_input = int(input("How many numbers would you like in your password? "))
symbols_input = int(input("How many symbols would you like in your password? "))

password = []
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ["*","^",";",":","!","~","&","%","$","#","@","(",")","[","}","{","]"]

for i in range(0,alphabets_input):        #number of alphabets time loop will run
    letter = random.choice(alphabets)     #taking random alphabets
    password.append(letter)               #appending that alphabets to password list

for i in range(0,numbers_input):
    number = random.randint(0,9)
    password.append(number)

for i in range(0,symbols_input):
    symbol = random.choice(symbols)
    password.append(symbol)

easy_password = ""             #typecasting from list to string with the help of loops
for password_elements in password:
    easy_password += str(password_elements)
print("Easy password is ",easy_password)

random.shuffle(password)      #shuffling the original list
hard_password = ""
for password_elements in password:
    hard_password += str(password_elements)
print("Hard password is ",hard_password)



#organised password generator
''' Ma'am code
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
password = ""

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print("Your easy password is",password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your hard password is: {password}")
'''
