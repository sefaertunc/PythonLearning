import requests as rq
import datetime as dt

USERNAME = "sefaertnc"
USER_TOKEN = "SKm4Mct8S56aasdLOHAF"
END_POINT = "https://pixe.la/v1/users"
RUNNING_ID = "g1"

user_params = {
	"token": USER_TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

graph_endpoint = f"{END_POINT}/{USERNAME}/graphs"

graph_config = {
	"id": "g1",
	"name": "Running Graph",
	"unit": "Km",
	"type": "float",
	"color": "sora"
}

headers = {
	"X-USER-TOKEN": USER_TOKEN,
}

editPixel_endPoint = f"{END_POINT}/{USERNAME}/graphs/{RUNNING_ID}/20241222"
data = {
	"quantity": "5.34",
}

# today_date = dt.date.today()
# today_date = str(today_date)
# print()

# response = rq.delete(url=editPixel_endPoint, headers=headers)
# print(response.text)
#
