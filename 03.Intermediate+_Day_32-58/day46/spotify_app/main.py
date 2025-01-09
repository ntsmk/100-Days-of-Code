import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

# pulling the top 20 songs of the artist
# results = sp.search(q='weezer', limit=20)
# song_list = [song["name"] for song in results["tracks"]["items"]]
# print(song_list)

# todo create a list of Spotify song URIs for the list of song names you found on Billboard
results = sp.xxx # needs to figure it out
print(results)


# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#
# URL = f"https://www.billboard.com/charts/hot-100/{date}/"
# # URL = "https://www.billboard.com/charts/hot-100/2021-10-23/"
#
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
# response = requests.get(URL, headers=header)
# billboard_page = response.text
# soup = BeautifulSoup(billboard_page, "html.parser")
#
# songs_name = soup.select(selector="li h3", class_="c-title a-no-trucate")
# song_list = [song.getText().strip() for song in songs_name]
# song_list2 = song_list[0:100]
# print(song_list2)