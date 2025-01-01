from bs4 import BeautifulSoup
# import lxml

# content = open("website.html", "r")
# print(content.read())

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)

#print(soup.prettify())
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
