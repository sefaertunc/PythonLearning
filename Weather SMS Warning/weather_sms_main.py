import requests as rq
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("../.venv/.env")
app_id = os.getenv("WEATHER_API_KEY")
twilio_account_sid = os.getenv("TWILIO_ACC_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_NUMBER")
my_number = os.getenv("MY_NUMBER")

client = Client(twilio_account_sid, twilio_auth_token)

main_domain = "https://api.openweathermap.org/data/2.5/weather"
weather_params = {
	"lat": -19.258965,
	"lon": 146.816956,
	"appid": app_id,
	"units": "metric",
}


def send_SMS(status):
	message = client.messages.create(
		body=f"Today is {status}",
		from_=twilio_phone,
		to=my_number,
	)
	print(message.status)


weather = rq.get(main_domain, params=weather_params)
weather.raise_for_status()
weather_json = weather.json()


state = weather_json["weather"][0]["main"]
send_SMS(state)

