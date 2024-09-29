sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# print(sentence.split())
# for item in sentence.split():
#     print(item)

result = {key:len(key) for key in sentence.split()}
print(result)
