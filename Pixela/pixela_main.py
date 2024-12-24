import requests as rq
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv("../.venv/.env")

USERNAME = "sefaertnc"
USER_TOKEN = os.getenv("PIXELA")
END_POINT = "https://pixe.la/v1/users"
RUNNING_ID = "g1"

user_params = {
	"token": USER_TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

user_endpoint = f"{END_POINT}/{USERNAME}"
graph_endpoint = f"{END_POINT}/{USERNAME}/graphs"

graph_config = {
	"id": "g1",
	"name": "Running Graph",
	"unit": "Km",
	"type": "float",
	"color": "sora"
}

header = {
	"X-USER-TOKEN": USER_TOKEN,
}

editPixel_endPoint = f"{END_POINT}/{USERNAME}/graphs/{RUNNING_ID}"

data = {
	"date": "20241224",
	"quantity": "4.62"
}
updated_data = {
	"quantity": "7.84"
}

# response = rq.post(url=END_POINT, json=user_params) # Creating Profile
# response = rq.post(url=graph_endpoint, headers=header, json=graph_config) # Creating Graph
# response = rq.post(url=editPixel_endPoint, headers=header, json=data) # Adding Data on a Pixel
# response  = rq.get(url=f"{editPixel_endPoint}/stats", headers=header) # Getting Stats
# response  = rq.get(url=f"{editPixel_endPoint}/pixels", headers=header) # Getting Pixel List
# response = rq.get(url=f"{editPixel_endPoint}/20241222", headers=header) # Getting a Pixel
# response = rq.put(url=f"{editPixel_endPoint}/20241224", json=updated_data, headers=header) # Updating a Pixel
# response = rq.delete(url=f"{editPixel_endPoint}/20241224",headers=header) # Deleting a Pixel
# print(f"{editPixel_endPoint}") # View only graph
# print(f"{editPixel_endPoint}.html") # View detailed graph
# print(response.text)
# print(response.status_code)
# print(response.json())

