#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


output_file_names = ["letter_for_Aang.txt","letter_for_Zuko.txt","letter_for_Appa.txt","letter_for_Katara.txt","letter_for_Sokka.txt","letter_for_Momo.txt","letter_for_Uncle Iroh.txt","letter_for_Toph.txt"]

for i in range(len(names)):
        file = open("./Input/Letters/starting_letter.txt", mode='r')
        content = file.read()
        strip_name = names[i].strip('\n')
        replace_content = content.replace("[name]", strip_name)

        address = "./Output/ReadyToSend/" + output_file_names[i]
        write_file = open(address, mode ='w')
        write_contents = write_file.write(replace_content)
        file.close()


'''Ma'am code
PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
'''