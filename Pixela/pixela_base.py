import os
from dotenv import load_dotenv
import requests as rq

class PixelaBase:
    load_dotenv("../.venv/.env")
    instance = None
    def __init__(self):
        self.__USERNAME = "sefaertnc"
        self.__USER_TOKEN = os.getenv("PIXELA")
        self.__RUNNING_ID = "g1"
        self.END_POINT = "https://pixe.la/v1/users"
        self.USER_ENDPOINT = f"{self.END_POINT}/{self.__USERNAME}"
        self.GRAPH_ENDPOINT = f"{self.USER_ENDPOINT}/graphs/{self.__RUNNING_ID}"
        self.__header = {
            "X-USER-TOKEN": self.__USER_TOKEN,
        }

        adding_data = {
            "date": "20241224",
            "quantity": "4.62"
        }
        updated_data = {
            "quantity": "7.84"
        }

    def get_stats(self):
        stats = rq.get(f"{self.GRAPH_ENDPOINT}/stats")
        return stats.json()


    @staticmethod
    def get_instance():
        if not PixelaBase.instance:
            PixelaBase.instance = PixelaBase()
            print("Creating new instance")
        else:
            print("Instance already created")
        return PixelaBase.instance
