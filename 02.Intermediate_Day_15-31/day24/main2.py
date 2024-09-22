# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# with open("/Users/Natsumi/Desktop/new_file.txt") as file:
#     print(file.read())

# absolute path
# with open(r"\Users\Natsumi\Desktop\new_file.txt") as file:
#     print(file.read())

# relative path
with open(r"..\..\..\..\..\Desktop\new_file.txt") as file:
    print(file.read())

