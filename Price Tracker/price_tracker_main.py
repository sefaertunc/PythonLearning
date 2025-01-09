import requests as rq
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv("../.venv/.env")
SENDING_EMAIL = "sample.learning.24@gmail.com"
RECEIVING_EMAIL = "sefaertnc@gmail.com"
GMAIL_PASSWORD = os.getenv("GMAIL_APP_PASS")
PRICE_LIMIT = 70

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}


response = rq.get("https://www.amazon.de/-/tr/dp/B08GSTF5NJ/ref=sr_1_3?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2O41FVJASXSIE&dib=eyJ2IjoiMSJ9.2x4CoZTOdM-LGNonNlWcFiLa-mRo1eJMdS6COueOmeeXvZyqdCCQVV-z9OT_tZJKMSsByI-QXOLfoZ72T9Pmn8Dhrd7sSM7dmwfrb51-yM0UWPcJ1ks87cRYb3t8l3kfA6NLAUXFUa4xjUET8uakgcPpuwZjAsW9WpuCC7V3yfEnuM_v7S04YeS0TcM8yFgITQQWhncuNQ6p7g2GFeQsSb7oyCUxFkwYslJFDURhOZg.qoYgmz13wlcmI9iNXFodVVk0fLycuHh3Nubo_mdRbqE&dib_tag=se&keywords=ddr4%2Bram%2B32gb%2B3200mhz%2Bsodimm&nsdOptOutParam=true&qid=1736446169&sprefix=ddr4%2Bram%2B32gb%2B3200mhz%2Bsodimm%2Caps%2C96&sr=8-3&th=1&language=en_GB", headers=header)
soup = BeautifulSoup(response.text, "html.parser")

#region Long Method to Get Price
# price_tag = soup.find_all("span", attrs={"class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"})
# base_price = price_tag[1].find("span",attrs={"class":"a-price-whole"})
# base_price = float((base_price.text).split(",")[0])
# coin_price = price_tag[1].find("span",attrs={"class":"a-price-fraction"})
# coin_price = float(coin_price.text)/100
# price = base_price + coin_price
#endregion

price_str = soup.find("span", attrs={"class":"a-offscreen"}).get_text()
price = float(price_str.split("€")[1].replace(",", "."))

title_str = soup.find("div", attrs={"class":"a-section a-spacing-none", "id":"titleSection"}).get_text().lstrip(" ").rstrip(" ")

if price < PRICE_LIMIT:
    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=SENDING_EMAIL, password=GMAIL_PASSWORD)

        msg = f"{title_str} is now ${price}\nThe link: {response.url}"
        connection.sendmail(SENDING_EMAIL, RECEIVING_EMAIL, msg)
        print("Email sent.")
    except Exception as e:
        print("Email failed.")
        print(e)