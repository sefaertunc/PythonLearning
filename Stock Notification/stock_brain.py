import os
import requests
from dotenv import load_dotenv
import math
from twilio.rest import Client

load_dotenv("../.venv/.env")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = os.getenv("ALPHAVANTAGE")

twilio_account_sid = os.getenv("TWILIO_ACC_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_NUMBER")
my_number = os.getenv("MY_NUMBER")

client = Client(twilio_account_sid, twilio_auth_token)

stock_value_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": API_KEY,
}

stock_news_params = {
    "function": "NEWS_SENTIMENT",
    "tickers": STOCK_NAME,
    "time_from": "20240101T0130",
    "apikey": API_KEY,
    "sort": "RELEVANCE",
    "limit": 50
}


def check_stock_value():
    """Return a tuple (Value Information, Relevant Two News)"""
    data = values_response.json()["Time Series (Daily)"]
    dates = list(data.keys())
    close1 = float(data[dates[0]]["4. close"])
    close2 = float(data[dates[1]]["4. close"])
    difference_nor = close1 - close2
    difference_abs = math.fabs(close1 - close2)
    percentage_dif = 100 * (close1 / close2 - 1)
    news_data = news_response.json()["feed"]
    news_dic = {
        "news": [
            {
                "title": news_data[0]["title"],
                "summary": news_data[0]["summary"],
                "url": news_data[0]["url"],
            },
            {
                "title": news_data[1]["title"],
                "summary": news_data[1]["summary"],
                "url": news_data[1]["url"],
            }
        ]
    }
    if difference_nor > 0:
        return_tuple = (f"{STOCK_NAME} up over 🔼${difference_abs:.2f} - 🔺{percentage_dif:.2f}%", news_dic)
        return return_tuple
    else:
        return_tuple = (f"{STOCK_NAME} down over 🔽${difference_abs:.2f} - 🔻{percentage_dif:.2f}%", news_dic)
        return return_tuple


def send_SMS():
    data = check_stock_value()
    msg_part1= f"{data[0]}\nNews1:{data[1]['news'][0]['title']}\nSummary:{data[1]['news'][0]['summary']}\n{data[1]['news'][0]['url']}\n"
    msg_part2 = f"{data[0]}\nNews1:{data[1]['news'][1]['title']}\nSummary:{data[1]['news'][1]['summary']}\n{data[1]['news'][1]['url']}\n"
    message = client.messages.create(
        body=msg_part1+msg_part2,
        from_=twilio_phone,
        to=my_number,
    )


news_response = requests.get(API_ENDPOINT, params=stock_news_params)
print(news_response.url)
values_response = requests.get(API_ENDPOINT, params=stock_value_params)
print(values_response.url)

send_SMS()
