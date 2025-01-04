import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_page = response.text
soup = BeautifulSoup(movie_page, "html.parser")

# titles = soup.find_all(class_="title")
titles = soup.find_all("h3")
movie_list = []
for title in titles:
    movie_list.append(title.getText())

print(movie_list)

# todo Generate a text file called movies.txt that lists the movie titles in ascending order (starting from 1)
