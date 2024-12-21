import os
import requests
from dotenv import load_dotenv

load_dotenv("../.venv/.env")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = os.getenv("ALPHAVANTAGE")

stock_value_params = {
	"function": "TIME_SERIES_DAILY",
	"symbol": STOCK_NAME,
	"outputsize": "compact",
	"datatype": "json",
	"apikey": "53BDTPIIE2M60PWN",
}

stock_news_params = {
	"function": "NEWS_SENTIMENT",
	"tickers": STOCK_NAME,
	"time_from": "20240101T0130",
	"apikey": "53BDTPIIE2M60PWN",
	"sort": "RELEVANCE",
	"limit": 50
}

news_response = requests.get(API_ENDPOINT, params=stock_news_params)
print(news_response.url)
values_response = requests.get(API_ENDPOINT, params=stock_value_params)
print(values_response.url)