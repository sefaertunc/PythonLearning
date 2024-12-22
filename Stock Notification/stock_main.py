from stock_brain import StockNotifier
import datetime as dt

notifier = StockNotifier(stock_name="TSLA", company_name="Tesla Inc")

if dt.datetime.now().hour == 7:
	notifier.send_sms()
