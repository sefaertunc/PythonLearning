import smtplib
import random as rd
import datetime as dt

my_email = "sefaertnc@gmail.com"
my_password = "jpgz hqks zfjq vcbz"


def send_quote():
	with open("/quotes.txt", "r") as file:
		quotes = file.readlines()
	try:
		# Connect to Gmail's SMTP server
		connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
		connection.starttls()  # Start TLS encryption
		connection.login(user=my_email, password=my_password)

		# Prepare the email
		msg = f"Subject: MONDAY QUOTE\n\n{rd.choice(quotes)}"
		connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg)
		print("Email sent successfully!")

	except Exception as e:
		print(f"An error occurred: {e}")

	finally:
		connection.close()


if dt.datetime.now().weekday() == 0:
	send_quote()
