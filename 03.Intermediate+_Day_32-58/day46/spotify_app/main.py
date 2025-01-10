import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = os.getenv("USER_ID")
redirect_uri = os.getenv("REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                               redirect_uri=redirect_uri, scope="playlist-modify-private"))

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
max_songs = 30

# 1. pulling the top 100 songs from the Billboard (Scraping part)
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(URL, headers=header)
billboard_page = response.text
soup = BeautifulSoup(billboard_page, "html.parser")
songs_name = soup.select(selector="li h3", class_="c-title a-no-trucate")
song_list = [song.getText().strip() for song in songs_name]
song_list_100 = song_list[0:max_songs]
print("searching for the songs...")

# 2. get URI for the song
uri_list = []
for i in range(len(song_list_100)):
    results = sp.search(song_list_100[i], type="track", limit=1)
    song_uri = results['tracks']['items'][0]['uri']
    uri_list.append(song_uri)
print("Songs found successfully!")

# 3. create the new playlist
playlist_creation = sp.user_playlist_create(user=user_id,
                                            name=f"{date} Billboard {max_songs}",
                                            public=False,
                                            description=f"This is Billboard chart {max_songs} on {date}")
playlist_id = playlist_creation["id"]

# # 4. add the songs to the playlist
sp.user_playlist_add_tracks(user_id, playlist_id, uri_list, position=None)
print("Playlist created successfully!")
