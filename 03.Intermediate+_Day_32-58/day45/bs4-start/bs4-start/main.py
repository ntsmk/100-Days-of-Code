from bs4 import BeautifulSoup
# import lxml

# content = open("website.html", "r")
# print(content.read())

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title)