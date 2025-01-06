from bs4 import BeautifulSoup
import datetime as dt
from dotenv import load_dotenv
import requests as rq
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

load_dotenv("../.venv/.env")

scope = "playlist-modify-private"
my_id = os.getenv("SPOTIFY_ID")
my_secret = os.getenv("SPOTIFY_SECRET")


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri="http://example.com",
        client_id=my_id,
        client_secret=my_secret,
        show_dialog=True,
        cache_path="../.venv/private/.token.txt",
    )
)


my_username = sp.current_user()["id"]
END_POINT = "https://www.billboard.com/charts/hot-100/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
now_date = dt.datetime.now().date().strftime("%Y%m%d")
min_date = 19580804
date = ""
songs_uris = []


def user_input():
    global date
    while True:
        try:
            date = input("Enter the date (YYYYMMDD): ")
            if not date.isdigit() or len(date) != 8:
                raise ValueError("Invalid format. Please enter the date in YYYYMMDD format.")

            if int(date) <= min_date or int(date) >= int(now_date):
                print("Invalid date. Please enter a date within the valid range.")
            else:
                break
        except ValueError as e:
            print(e)

def get_songs():
    list_end_point = f"{END_POINT}{date[:4]}-{date[4:6]}-{date[6:]}"
    response = rq.get(list_end_point, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    all_list_items = soup.find_all(name="ul",class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")
    songs = {item.find(name="span").text.strip():item.find(name="h3").text.strip() for item in all_list_items}
    return songs


def get_song_uris():
    for value in get_songs().values():
        result = sp.search(q=f"track:{value} year:{date[0:4]}", type="track", limit=1)
        try:
            the_uri = result["tracks"]["items"][0]["uri"]
            songs_uris.append(the_uri)
        except IndexError:
            print(f"{value} is not a valid track id.")

def add_songs_toList():
    playlists = { item["name"]:item["id"] for item in sp.user_playlists(my_username)["items"]}
    sample_list_uri = list(playlists.values())[0]
    for uri in songs_uris:
        sp.playlist_add_items(sample_list_uri, uri)


user_input()
get_songs()
get_song_uris()
add_songs_toList()
