# with open("a_file.txt") as file:
#     file.read()

try:
    file = open("a_file.txt")
    a_dic = {"key": "value"}
    print(a_dic["abc"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")