import os
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import requests as rq
from pixela_UI import PixelaUI


class PixelaBase:
    load_dotenv("../.venv/.env")
    instance = None

    def __init__(self):
        self.__pixUI = PixelaUI()
        self.__USERNAME = "sefaertnc"
        self.__USER_TOKEN = os.getenv("PIXELA")
        self.__RUNNING_ID = "g1"
        self.END_POINT = "https://pixe.la/v1/users"
        self.USER_ENDPOINT = f"{self.END_POINT}/{self.__USERNAME}"
        self.GRAPH_ENDPOINT = f"{self.USER_ENDPOINT}/graphs/{self.__RUNNING_ID}"
        self.__header = {
            "X-USER-TOKEN": self.__USER_TOKEN,
        }
        self.__initial_settings()

    def __check_stat(self, date):
        stat = rq.get(f"{self.GRAPH_ENDPOINT}/{date}", headers=self.__header)
        return stat.status_code

    def __update_stat(self, date, quantity):
        """
        Update or add pixel data for the specified date and quantity.
        """
        status = self.__check_stat(date)

        if status == 404:
            data = {"date": date, "quantity": quantity}
            response = self.__send_request("POST", self.GRAPH_ENDPOINT, data)
        elif status == 200:
            pixel_url = f"{self.GRAPH_ENDPOINT}/{date}"  # Correct pixel URL
            data = {"quantity": quantity}
            response = self.__send_request("PUT", pixel_url, data)
        else:
            messagebox.showinfo(title="Pixela", message="Please click the button again.")
            return

        self.__handle_response(response)

    def __send_request(self, method, url, data):
        if method == "POST":
            return rq.post(url=url, headers=self.__header, json=data)
        elif method == "PUT":
            return rq.put(url=url, headers=self.__header, json=data)

    def __handle_response(self, response):
        if response.status_code != 200:
            messagebox.showerror(
                title="Data Error",
                message=f"Error {response.status_code}: {response.json().get('message', 'Unknown error')}\n"
                        f"Example-> Date: 19231029 | Duration: 81"
            )
        else:
            messagebox.showinfo(title=f"{response.status_code}", message="The data is successfully updated.")
            self.__clean_entries()

    def get_mainloop(self):
        self.__pixUI.window.mainloop()

    def __clean_entries(self):
        self.__pixUI.date_entry.delete(0, tk.END)
        self.__pixUI.duration_entry.delete(0, tk.END)

    def __initial_settings(self):
        self.__pixUI.upgrade_button.config(command=lambda: self.__update_stat(date=str(self.__pixUI.date_entry.get()),
                                                                              quantity=str(
                                                                                self.__pixUI.duration_entry.get())))

    @staticmethod
    def get_instance():
        if not PixelaBase.instance:
            PixelaBase.instance = PixelaBase()
            print("Creating new instance")
        else:
            print("Instance already created")
        return PixelaBase.instance
