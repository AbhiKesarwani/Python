import pandas
data = pandas.read_csv("weather_data.csv")
#print(data)
#print(type(data))
#print(type(data["temp"]))

#data_dict = data.to_dict()
#print(data_dict)

#Series
#temp_list = data["temp"].to_list()
#print(temp_list)
#
#print(data["temp"].mean())
#print(data["temp"].max())
#
#print(data["condition"])
#print(data.condition)

#Get data of row
#print(data[data.day == "Monday"])
#print(data[data["temp"] == data["temp"].max()])

#monday = data[data.day == "Monday"]
#print(monday)
#print(monday["condition"])    #monday.condition

monday = data[data.day == "Monday"]
monday_temp = monday["temp"]    #monday.temp
monday_temp_in_F = (9/5)*monday_temp + 32
print(monday_temp_in_F)