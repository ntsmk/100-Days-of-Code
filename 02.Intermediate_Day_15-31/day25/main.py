# with open("weather_data.csv") as f:
#     data = f.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#
#     for row in data:
#         temperatures.append(row[1])
#     temperatures.remove("temp")
#     for i in range(len(temperatures)):
#         temperatures[i] = int(temperatures[i])
#
# print(temperatures)

import pandas
from statistics import mean

# data = pandas.read_csv("weather_data.csv")

# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# # average = mean(temp_list)
# # print(round(average,0))
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# print(data.temp)

# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == 'Monday']
# celsius = monday.temp
# fahrenheit = (celsius * 1.8) + 32
# print(f"celsius: {celsius}")
# print(f"fahrenheit: {fahrenheit}")

data_dic ={
    "student": ["Amy", "james", "angela"],
    "scores": [78, 57,29]
}
data = pandas.DataFrame(data_dic)
print(data)
data.to_csv("newdata.csv")