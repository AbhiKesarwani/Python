#with open("weather_data.csv") as file:
#    data = file.readlines()
#    print(data)

#import csv
#with open("weather_data.csv") as file:
#    data = csv.reader(file)
#    temp = []
#    for row in data:
#        print(row)
#        if row[1] != 'temp':
#            temp.append(int(row[1]))
#    print(temp)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])