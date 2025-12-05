numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)

#By List Comprehension
new_list = [n+1 for n in numbers]
print(new_list)

#used for string also and add it to the list
name = "Abhinav"
new_list = [letter for letter in name]
print(new_list)

#doubling the old list
new_list =[number*2 for number in range(1,5)]
print(new_list)

#Conditional List Comprehension
names = ['Alex', 'Beth', 'Caroline', 'Freddie', 'Abhinav', 'Abhi']
new_name_list = [name for name in names if len(name) == 4]
print(new_name_list)
upper_name = [name.upper() for name in names if len(name) > 4]
print(upper_name)
