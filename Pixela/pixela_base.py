import tkinter

from dotenv import load_dotenv
import os
from pixela_UI import PixelaUI
import requests as rq
import tkinter as tk
from tkinter import messagebox
import webbrowser


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
        self.__show_statistics()
        print(rq.get(f"{self.GRAPH_ENDPOINT}/20241226", headers=self.__header).url)

    def __check_stat(self, date):
        code = 0
        while not code==200:
            stat = rq.get(f"{self.GRAPH_ENDPOINT}/{date}", headers=self.__header)
            if stat.status_code == 200:
                code = stat.status_code
        return code

    def __update_stat(self, date, quantity):
        """
        Update or add pixel data for the specified date and quantity.
        """
        status = self.__check_stat(date)

        if status == 404:
            data = {"date": date, "quantity": quantity}
            response = self.__send_request("POST", self.GRAPH_ENDPOINT, data=data)
            self.__handle_response(response, "ADDE")
        elif status == 200:
            pixel_url = f"{self.GRAPH_ENDPOINT}/{date}"  # Correct pixel URL
            data = {"quantity": quantity}
            response = self.__send_request("PUT", pixel_url, data=data)
            self.__handle_response(response, "UPDATE")
        else:
            messagebox.showinfo(title="Pixela", message="Please click the button again.")
            return
        self.__show_statistics()

    def __delete_stat(self, date):
        status = self.__check_stat(date)
        if status == 200:
            response = self.__send_request("DELETE", f"{self.GRAPH_ENDPOINT}/{date}")
            self.__handle_response(response, "DELETE")
        elif status == 404:
            tkinter.messagebox.showerror(title=str(status), message="There is no data for this date.")
        else:
            messagebox.showinfo(title="Pixela", message="Please click the button again.")
            return
        self.__show_statistics()

    def __show_graph_image(self):
        webbrowser.open(self.GRAPH_ENDPOINT)

    def __show_detailed_graph(self):
        webbrowser.open(f"{self.GRAPH_ENDPOINT}.html")

    def __show_statistics(self):
        canvas = self.__pixUI.stats_canvas
        stats = rq.get(f"{self.GRAPH_ENDPOINT}/stats").json()
        canvas.itemconfig(self.__pixUI.stats_values,text=f"{stats['todaysQuantity']}  min\n\n"
                                                         f"{stats['avgQuantity']}  min\n\n"
                                                         f"{stats['maxQuantity']}  min\n\n"
                                                         f"{stats['minQuantity']}  min\n\n"
                                                         f"{stats['totalQuantity']}  min\n\n")

    def __send_request(self, method, url, data=None):
        """
        Sends an HTTP request with the specified method, URL, and optional data.

        :param method: HTTP method (e.g., "POST", "PUT", "GET", "DELETE").
        :param url: The endpoint URL.
        :param data: (Optional) JSON payload for POST or PUT requests.
        :return: Response object from the request.
        """
        method = method.upper()  # Ensure method is in uppercase for consistency

        if method == "POST":
            return rq.post(url=url, headers=self.__header, json=data)
        elif method == "PUT":
            return rq.put(url=url, headers=self.__header, json=data)
        elif method == "GET":
            return rq.get(url=url, headers=self.__header)
        elif method == "DELETE":
            return rq.delete(url=url, headers=self.__header)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

    def __handle_response(self, response, action):
        if response.status_code != 200:
            messagebox.showerror(
                title="Data Error",
                message=f"Error {response.status_code}: {response.json().get('message', 'Unknown error')}\n")
        else:
            messagebox.showinfo(title=f"{response.status_code}", message=f"The data is successfully {action.lower()}d.")
            self.__clean_entries()

    def __clean_entries(self):
        self.__pixUI.date_entry.delete(0, tk.END)
        self.__pixUI.duration_entry.delete(0, tk.END)
        self.__pixUI.date_entry.insert(0, "Date:YYYYMMDD")
        self.__pixUI.duration_entry.insert(0, "Duration:00.0 min")
        self.__pixUI.date_entry.focus_set()

    def __initial_settings(self):
        self.__pixUI.upgrade_button.config(command=lambda: self.__update_stat(date=str(self.__pixUI.date_entry.get()),
                                                                              quantity=str(
                                                                                  self.__pixUI.duration_entry.get())))
        self.__pixUI.delete_button.config(command=lambda: self.__delete_stat(date=str(self.__pixUI.date_entry.get())))
        self.__pixUI.graph_button.config(command=lambda: self.__show_graph_image())
        self.__pixUI.detailed_graph_button.config(command=lambda: self.__show_detailed_graph())

    def get_mainloop(self):
        self.__pixUI.window.mainloop()

    @staticmethod
    def get_instance():
        if not PixelaBase.instance:
            PixelaBase.instance = PixelaBase()
            print("Creating new instance")
        else:
            print("Instance already created")
        return PixelaBase.instance
