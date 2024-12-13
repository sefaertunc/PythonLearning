import datetime as dt
import pandas as pd
import smtplib
import random as rd

MY_EMAIL = "sefaertnc@gmail.com"
PASSWORD = "jpgz hqks zfjq vcbz"
NOW = dt.datetime.now()
PLACEHOLDER = "[NAME]"
letter_list = []

try:
	birthday_data = pd.read_csv('birthdays.csv')
	birthday_dic = birthday_data.to_dict()
	print(birthday_dic)
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
	for num in range(len(birthday_dic["month"])):
		print(num)
		if NOW.month == birthday_dic["month"][num]:
			for num2 in range(len(birthday_dic["day"])):
				print(num2)
				if NOW.day == birthday_dic["day"][num2]:
					name = birthday_dic["name"][num2]
					mail = birthday_dic["email"][num2]
					print(f"{name} {mail}")


def prepare_mail(name):
	num = rd.randint(1, 3)
	letter = f"letter_{num}.txt"
	try:
		with open(f"letter_templates/{letter}", "r") as letter:
			letter_content = letter.read()
			new_letter = letter_content.replace(PLACEHOLDER, name)
	except FileNotFoundError as e3:
		print(f"An error occurred: {e3}")
	finally:
		return new_letter


check_the_date()
