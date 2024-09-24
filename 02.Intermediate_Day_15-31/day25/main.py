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

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()
print(data_dict)
