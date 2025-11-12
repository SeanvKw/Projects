import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
SPOTIFY_API = "https://top100billboardstimer.org/callback"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIFY_API,
        client_id=str(os.getenv("SPOTIFY_CLIENT_ID")),
        client_secret=str(os.getenv("SPOTIPY_CLIENT_SECRET")),
        show_dialog=True,
        cache_path="token.txt",
        username="Adrian Rączka",
    )
)
user_id = sp.current_user()["id"]  # type: ignore
date = str(input(
    # ONLY TYPE THE CURRENT DATE BECAUSE THE SITE REQUIRES A PAID SUBSCRIPTION :<
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "))

spotify_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard100",
    public=False,
    description="Top 100 songs from Billboard from your chosen date"
)
playlist_id = spotify_playlist["id"]  # type: ignore
print(playlist_id)
BILLBOARD_TOP_100_URL = f"https://www.billboard.com/charts/hot-100/{date}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 OPR/122.0.0.0"
}
response = requests.get(BILLBOARD_TOP_100_URL, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

song_titles = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in song_titles]
year = date.split("-")[0]
song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]  # type: ignore
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
