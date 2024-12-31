from bs4 import BeautifulSoup

# content = open("website.html", "r")
# print(content.read())

with open("website.html") as file:
    content = file.read()

print(content)