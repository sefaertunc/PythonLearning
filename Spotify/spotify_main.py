from bs4 import BeautifulSoup
import datetime as dt
from dotenv import load_dotenv
import requests as rq
import spotipy
from numpy.f2py.crackfortran import myeval
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import os

load_dotenv("../.venv/.env")


scope = "playlist-modify-private"
my_id = os.getenv("SPOTIFY_ID")
my_secret = os.getenv("SPOTIFY_SECRET")
my_username = "sefaertunc3"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri="http://example.com",
        client_id=my_id,
        client_secret=my_secret,
        show_dialog=True,
        cache_path=".token.txt",
        username=my_username,
    )
)
user_id = sp.current_user()["id"]

END_POINT = "https://www.billboard.com/charts/hot-100/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
now_date = dt.datetime.now().date().strftime("%Y%m%d")
min_date = 19580804
date = "20250104"


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

#user_input()

LIST_END_POINT = f"{END_POINT}{date[:4]}-{date[4:6]}-{date[6:]}"
response = rq.get(LIST_END_POINT, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
all_list_items = soup.find_all(name="ul",class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")
songs_dic = {item.find(name="span").text.strip():item.find(name="h3").text.strip() for item in all_list_items}

# item = all_list_items[0].find(name="h3",id="title-of-a-story")
# top_100_list = {item.find(name="span",id="title-of-a-story"):item.find(name="h3",id="title-of-a-story") for item in all_list_items}