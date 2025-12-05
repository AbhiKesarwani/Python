import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_data = data["Primary Fur Color"]

Gray_color = 0
Cinnamon_color = 0
Black_color = 0
for color in color_data:
    if color == "Gray":
        Gray_color += 1
    elif color == "Cinnamon":
        Cinnamon_color += 1
    elif color == "Black":
        Black_color += 1

#gray_color = len(data[data["Primary Fur Color"] == "Gray"])
print(Gray_color)#2473
print(Cinnamon_color)#392
print(Black_color)#103

data_dict = {"Fur Color": ["Grey","Cinnamon","Black"], "Count":[2473,392,103]}
data_dataframe = pandas.DataFrame(data_dict)
print(data_dataframe)

data_dataframe.to_csv("squirrel_count.csv")
