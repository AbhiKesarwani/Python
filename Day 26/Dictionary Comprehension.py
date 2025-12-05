import random
names = ["Alex", "Beth", "Abhi", "Abhinav", "Freddie"]
students_scores = {name:random.randint(0,100) for name in names}
print(students_scores)

passed_students = {name:score for (name,score) in students_scores.items() if score>40}
print(passed_students)