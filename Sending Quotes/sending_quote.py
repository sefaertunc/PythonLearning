import smtplib
import random as rd
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv("../.venv/.env")

MY_EMAIL = "sample.learning.24@gmail.com"
PASSWORD = os.getenv("GMAIL_APP_PASS")


def send_quote():
	with open("quotes.txt", "r") as file:
		quotes = file.readlines()
	try:
		# Connect to Gmail's SMTP server
		connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
		connection.starttls()  # Start TLS encryption
		connection.login(user=MY_EMAIL, password=PASSWORD)

		# Prepare the email
		msg = f"Subject: MONDAY QUOTE\n\n{rd.choice(quotes)}"
		connection.sendmail(from_addr=MY_EMAIL, to_addrs="sefaertnc@gmail.com", msg=msg)
		connection.sendmail(from_addr=MY_EMAIL, to_addrs="yasemencelik91@gmail.com ", msg=msg)
		print("Email sent successfully!")

	except Exception as e:
		print(f"An error occurred: {e}")

	finally:
		connection.close()


if dt.datetime.now().isoweekday() == 1:
	send_quote()
