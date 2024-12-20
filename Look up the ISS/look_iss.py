import time
import os
from dotenv import load_dotenv
import requests
import datetime as dt
import math
import smtplib

load_dotenv("../venv/.env")

MY_LAT = -51.200321
MY_LNG = 145.420788
MY_TIME = int(dt.datetime.now().hour)
MY_EMAIL = "sample.learning.24@gmail.com"
PASSWORD = os.getenv("APP_PASSWORD")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
    "date": 'today'
}


def send_mail():
    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)

        look_message = "Subject:ISS\n\nLook up to the sky to see the ISS."
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="sefaertnc@gmail.com", msg=look_message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

def check_time():
    print("Method is checked.")
    if math.fabs(MY_LAT - iss_lat) < 5 and math.fabs(MY_LNG - iss_lng) < 5:
        if MY_TIME >= sun_set or MY_TIME <= sun_rise:
            return True

iss_response = requests.get("http://api.open-notify.org/iss-now.json")
sun_set_rise_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
iss_data = iss_response.json()
sun_set_rise_data = sun_set_rise_response.json()

iss_lat = float(iss_data["iss_position"]["latitude"])
iss_lng = float(iss_data["iss_position"]["longitude"])

sun_set = int(sun_set_rise_data["results"]["sunset"].split("T")[1].split(":")[0])
sun_rise = int(sun_set_rise_data["results"]["sunrise"].split("T")[1].split(":")[0])

while True:
    time.sleep(5)
    if check_time():
        send_mail()
