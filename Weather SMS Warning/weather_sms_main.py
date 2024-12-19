import requests as rq
import os
from dotenv import load_dotenv

load_dotenv("../.venv/.env")

main_domain = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
	"lat": 48.208176,
	"lon": 16.373819,
	"appid": os.getenv("WEATHER_API_KEY"),
	"units": "metric",
	"cnt": 4
}
weather = rq.get(main_domain, params=weather_params)
weather.raise_for_status()
weather_json = weather.json()

for days in weather_json["list"]:
	print(days["weather"][0]["main"])
