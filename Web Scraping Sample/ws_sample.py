import requests as rq
from bs4 import BeautifulSoup
import os


response = rq.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

films = [item.find(name="h3", class_="title").text for item in soup.find_all(name="div", class_="article-title-description__text")]
films.reverse()


try:
    with open("movies.txt", "a",encoding="utf-8") as f:
        print("File exists! Proceeding...")
        for film in films:
            f.write(film + "\n")
except FileNotFoundError:
    with open("movies.txt", "w",encoding="utf-8") as f:
        print("File does not exist! Creating new one!")
        for film in films:
            f.write(film + "\n")
except Exception as e:
    print(e)

