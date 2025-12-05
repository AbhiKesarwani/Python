   #Reading File

file = open("my_file.txt")     #opening file synatx
contents = file.read()
print(contents)
file.close()     #closing file syntax

with open("my_new_file.txt") as file:    #with this syntax no need to close the file
    contents = file.read()
    print(contents)

    #Writing on File
with open("my_new2_file.txt",mode = 'w') as file:    #if file exist it will delete all previous texts  and if file not exist it will create a new file.
     file.write("Writing on non-existing file")

     # Appending File
with open("my_file.txt",mode='a') as file:  #it will append the text with previous texts
   file.write("\nAppending Text")

  # Reading file which is in different folder by using absolute path
with open('\Programming\Python\File for day 24.txt') as file:       #with this syntax no need to close the file
    contents = file.read()
    print(contents)


  # Reading file which is in different folder by using relative path and we are going back
with open('../../File for day 24.txt') as file:    #with this syntax no need to close the file
    contents = file.read()
    print(contents)

