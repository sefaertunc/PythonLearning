import os
import math
import datetime as dt
from dotenv import load_dotenv
from twilio.rest import Client
import requests


class StockNotifier:
    def __init__(self, stock_name, company_name):
        load_dotenv("../.venv/.env")

        self.__stock_name = stock_name
        self.__company_name = company_name

        self.__api_endpoint = "https://www.alphavantage.co/query"
        self.__api_key = os.getenv("ALPHAVANTAGE")

        self.__twilio_account_sid = os.getenv("TWILIO_ACC_SID")
        self.__twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.__twilio_phone = os.getenv("TWILIO_NUMBER")
        self.__my_number = os.getenv("MY_NUMBER")

        self.__client = Client(self.__twilio_account_sid, self.__twilio_auth_token)

    def __fetch_stock_data(self):
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.__stock_name,
            "outputsize": "compact",
            "datatype": "json",
            "apikey": self.__api_key,
        }
        response = requests.get(self.__api_endpoint, params=params)
        response.raise_for_status()
        return response.json()["Time Series (Daily)"]

    def __fetch_news_data(self):
        params = {
            "function": "NEWS_SENTIMENT",
            "tickers": self.__stock_name,
            "time_from": "20240101T0130",
            "apikey": self.__api_key,
            "sort": "RELEVANCE",
            "limit": 50,
        }
        response = requests.get(self.__api_endpoint, params=params)
        response.raise_for_status()
        return response.json()["feed"]

    def __analyze_stock(self):
        data = self.__fetch_stock_data()
        dates = list(data.keys())
        close1 = float(data[dates[0]]['4. close'])
        close2 = float(data[dates[1]]['4. close'])

        difference_nor = close1 - close2
        difference_abs = math.fabs(difference_nor)
        percentage_dif = 100 * (close1 / close2 - 1)

        trend = "up" if difference_nor > 0 else "down"
        symbol = "🔼" if trend == "up" else "🔽"

        return f"{self.__stock_name} {trend} over {symbol}${difference_abs:.2f} - {symbol}{percentage_dif:.2f}%"

    def __prepare_news(self):
        news_data = self.__fetch_news_data()
        return [
            {
                "title": news["title"],
                "summary": news["summary"],
                "url": news["url"]
            }
            for news in news_data[:2]
        ]

    def __compose_message(self):
        stock_analysis = self.__analyze_stock()
        news = self.__prepare_news()

        messages = []
        for i, article in enumerate(news):
            message = (
                f"{stock_analysis}\n"
                f"News {i + 1}: {article['title']}\n"
                f"Summary: {article['summary']}\n"
                f"{article['url']}\n"
            )
            messages.append(message)
        return "\n".join(messages)

    def send_sms(self):
        message_body = self.__compose_message()
        message = self.__client.messages.create(
            body=message_body,
            from_=self.__twilio_phone,
            to=self.__my_number,
        )
        print(f"Message sent with SID: {message.sid}")


if __name__ == "__main__":
    print("This code is being run directly.")
