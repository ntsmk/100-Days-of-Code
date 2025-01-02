from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# requests.get("https://appbrewery.github.io/news.ycombinator.com/")

print(response.text)











# # import lxml
#
# # content = open("website.html", "r")
# # print(content.read())
#
# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# #print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags[0].getText())
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
# name = soup.select_one(selector="#name")
# print(name)
# heading_a = soup.select(".heading")
# print(heading_a)