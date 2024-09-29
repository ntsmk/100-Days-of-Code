# Dictionary Comprehension 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# print(sentence.split())
# for item in sentence.split():
#     print(item)

result = {key:len(key) for key in sentence.split()}
print(result)

# Dictionary Comprehension 2
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key:(value* 9/5) + 32 for key,value in weather_c.items()}

print(weather_f)