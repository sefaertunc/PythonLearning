import requests as rq

weather_api_key = 'd956d45ce2d24af85cc6c30ce86f35c8'
main_domain = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
	"lat": 48.208176,
	"lon": 16.373819,
	"appid": weather_api_key,
	"units": "metric",
	"cnt": 4
}
weather = rq.get(main_domain, params=weather_params)
weather.raise_for_status()
weather_json = weather.json()
# print(weather_json["list"][1]["weather"][0]["main"])
for days in weather_json["list"]:
	print(days["weather"][0]["main"])
