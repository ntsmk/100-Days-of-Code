# List comprehension 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num*num for num in numbers]
print(squared_numbers)

# List comprehension 2
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(i) for i in list_of_strings]
result = [even for even in numbers if even % 2 == 0]
print(result)

# Dictionary Comprehension 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# print(sentence.split())
# for item in sentence.split():
#     print(item)

result = {key: len(key) for key in sentence.split()}
print(result)

# Dictionary Comprehension 2
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {key: (value * 9/5) + 32 for key, value in weather_c.items()}

print(weather_f)
