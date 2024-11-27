import requests
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
today = str(date.today())
yesterday = str(date.today() - timedelta(1))
day_before_yesterday = str(date.today() - timedelta(2))


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

API_KEY = ""
STOCK_END_POINT = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY,
}

response = requests.get(url=STOCK_END_POINT, params=parameters)
response.raise_for_status()
data = response.json()
print(response.status_code)
print(data)
today_open = data["Time Series (Daily)"][today]["1. open"]
print(f"Today's open price: {today_open}")
yesterday_open = data["Time Series (Daily)"][yesterday]["1. open"]
print(f"Yesterday's open price: {yesterday_open}")
# day_before_yesterday_open = data["Time Series (Daily)"][day_before_yesterday]["1. open"]
# print(f"Yesterday's open price: {day_before_yesterday_open}")
# todo how to check day before yesterday if it is Friday or not?

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

