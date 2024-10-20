# # with open("a_file.txt") as file:
# #     file.read()
#
# try:
#     file = open("a_file.txt")
#     a_dic = {"key": "value"}
#     print(a_dic["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file was closed")
#     raise TypeError("This is an error that I made up")

#
# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)
#
#
# fruits = ["Apple", "Pear", "Orange"]
#
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")
#
# try:
#     make_pie(4)
# except:
#     print("Fruit pie")

fruits = ["Apple", "Pear", "Orange"]


# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)

# looks it is normal to put try and except in the actual method