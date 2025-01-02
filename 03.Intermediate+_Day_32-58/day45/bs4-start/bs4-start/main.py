from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page,"html.parser")

title = soup.find(class_="titleline")
link = title.select_one("a").get("href")
subtitle = soup.find(class_="subline")
article_upvotes = subtitle.find(class_="score").getText()

article_texts = []
article_links = []
titles = soup.find_all(class_="titleline")
for title in titles:
    article_texts.append(title.getText())
    link = title.select_one("a").get("href")
    article_links.append(link)
# print(article_texts) -> it works
# print(article_links) -> it works but sometimes it contains 'item?id=42575535'



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