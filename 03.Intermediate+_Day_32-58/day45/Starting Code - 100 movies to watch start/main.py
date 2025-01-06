import requests
from bs4 import BeautifulSoup
import re

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_page = response.text
soup = BeautifulSoup(movie_page, "html.parser")

# titles = soup.find_all(class_="title")
titles = soup.find_all("h3")
movie_list = [title.getText() for title in titles]
# for title in titles:
#     movie_list.append(title.getText())
# print(movie_list)

# movie_list.sort()
# print(sorted(movie_list))
# print(sorted(movie_list, key=lambda s: int(re.search(r'\d+', s).group())))
# movie_list1 = sorted(movie_list, key=lambda s: int(re.search(r'\d+', s).group()))
movie_list1 = movie_list[::-1]
# print(movie_list1)

with open('movie.txt', 'w', encoding="utf-8") as f:
    for i in range(len(movie_list1)):
        f.writelines(f"{movie_list1[i]}\n")
