import requests as rq
import datetime as dt

from pixela_UI import PixelaUI
from pixela_base import PixelaBase

pixBase = PixelaBase().get_instance()
pixUI = PixelaUI()

# region Graph Creating Data
# user_params = {
# 	"token": USER_TOKEN,
# 	"username": USERNAME,
# 	"agreeTermsOfService": "yes",
# 	"notMinor": "yes",
# }

# graph_config = {
# 	"id": "g1",
# 	"name": "Running Graph",
# 	"unit": "Km",
# 	"type": "float",
# 	"color": "sora"
# }




# response = rq.post(url=END_POINT, json=user_params) # Creating Profile
# response = rq.post(url=graph_endpoint, headers=header, json=graph_config) # Creating Graph
# response = rq.post(url=GRAPH_ENDPOINT, headers=header, json=adding_data) # Adding Data on a Pixel
# response  = rq.get(url=f"{GRAPH_ENDPOINT}/stats", headers=header) # Getting Stats
# response  = rq.get(url=f"{GRAPH_ENDPOINT}/pixels", headers=header) # Getting Pixel List
# response = rq.get(url=f"{GRAPH_ENDPOINT}/20241222", headers=header) # Getting a Pixel
# response = rq.put(url=f"{GRAPH_ENDPOINT}/20241224", json=updated_data, headers=header) # Updating a Pixel
# response = rq.delete(url=f"{GRAPH_ENDPOINT}/20241222", headers=header) # Deleting a Pixel
# print(f"{GRAPH_ENDPOINT}") # View only graph
# print(f"{GRAPH_ENDPOINT}.html") # View detailed graph
# print(f"{GRAPH_ENDPOINT}/stats")
# print(response.text)
# print(response.status_code)
# print(response.json())

