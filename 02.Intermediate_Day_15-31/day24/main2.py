# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


with open("new_file.txt", mode="a") as file:
    file.write("\nNEW TEXT, this is second one")