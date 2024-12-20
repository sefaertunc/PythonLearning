import datetime as dt
import pandas as pd
import smtplib
import random as rd
import os
from dotenv import load_dotenv

load_dotenv("../venv/.env")

MY_EMAIL = "sample.learning.24@gmail.com"
PASSWORD = os.getenv("APP_PASSWORD")
today_month = dt.datetime.now().month
today_day = dt.datetime.now().day
PLACEHOLDER = "[NAME]"

try:
	birthday_data = pd.read_csv('birthdays.csv')
	birthday_dic = birthday_data.set_index("name").T.to_dict(orient="list")
except FileNotFoundError as e1:
	print(f"An error occurred: {e1}")


def sent_birthday_mail(name, mail):
	try:
		connection = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
		connection.starttls()
		connection.login(user=MY_EMAIL, password=PASSWORD)

		birthday_msg = f"Subject:HAPPY BIRTHDAY\n\n{prepare_mail(name)}"
		connection.sendmail(from_addr=MY_EMAIL, to_addrs=mail, msg=birthday_msg)
		print("Email sent successfully!")

	except Exception as e2:
		print(f"An error occurred: {e2}")
	finally:
		connection.close()


def check_the_date():
	for ind in birthday_dic:
		if birthday_dic[ind][2] == today_month and birthday_dic[ind][3] == today_day:
			sent_birthday_mail(ind, birthday_dic[ind][0])


def prepare_mail(name):
	num = rd.randint(1, 3)
	letter = f"letter_{num}.txt"
	try:
		with open(f"letter_templates/{letter}", "r") as letter:
			letter_content = letter.read()
			new_letter = letter_content.replace(PLACEHOLDER, name)
	except FileNotFoundError as e3:
		print(f"An error occurred: {e3}")
	else:
		return new_letter


check_the_date()
