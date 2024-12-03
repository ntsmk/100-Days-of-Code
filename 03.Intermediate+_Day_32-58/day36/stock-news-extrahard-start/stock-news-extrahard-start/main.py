import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# today = str(date.today())
# yesterday = str(date.today() - timedelta(1))
# day_before_yesterday = str(date.today() - timedelta(3))

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STOCK_API_KEY = ""
STOCK_END_POINT = "https://www.alphavantage.co/query"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

response_1 = requests.get(url=STOCK_END_POINT, params=stock_parameters)
response_1.raise_for_status()
data_1 = response_1.json()["Time Series (Daily)"]
print(response_1.status_code)
print(data_1)

data_list = [value for (key, value) in data_1.items()]
yesterday_close = float(data_list[1]['4. close'])
day_before_yesterday_close = float(data_list[2]['4. close'])
# today_open = float(data_1["Time Series (Daily)"][today]["1. open"])
# print(f"Today's open price: {today_open}")
# yesterday_open = float(data_1["Time Series (Daily)"][yesterday]["1. open"])
# print(f"Yesterday's open price: {yesterday_open}")
# day_before_yesterday_open = float(data_1["Time Series (Daily)"][day_before_yesterday]["1. open"])
# print(f"day before yesterday open price: {day_before_yesterday_open}")
# decimal = day_before_yesterday_open / yesterday_open
decimal = day_before_yesterday_close / yesterday_close
print(decimal)
percent = "{:.0%}".format(decimal)
print(percent)
print(type(percent))

if decimal >= 1.01 or decimal <= 0.99:
    print("Get News!")

# # day_before_yesterday_open = data["Time Series (Daily)"][day_before_yesterday]["1. open"]
# # print(f"Yesterday's open price: {day_before_yesterday_open}")
# # todo how to check day before yesterday if it is Friday or not?
# #  -> ignore for now? if today is wed, thu, fri, sat, it works
# #   NOTE: Nov 28 is Thursday but US stock is closed because Thanksgiving
# --> used list comprehension

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

NEWS_END_POINT = ""
NEWS_API_KEY = ""

news_parameters = {
    "q": COMPANY_NAME,
    "language": "en",
    "apikey": NEWS_API_KEY,
}

response_2 = requests.get(url=NEWS_END_POINT, params=news_parameters)
response_2.raise_for_status()
data_2 = response_2.json()
print(response_2.status_code)
print(data_2)
contents = ""
for i in range(3):
    headline = data_2["articles"][i]["title"]
    print(f"Headline {i+1}: {headline}")
    brief = data_2["articles"][i]["description"]
    print(f"Brief {i+1}: {brief}")

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
account_sid = ""
auth_token = ""

if decimal > 1:
    final_percent = ("🔺"+ percent[2:])
elif decimal < 1:
    final_percent = ("🔻"+ str(10-int(percent[1]))+"%")

if decimal >= 1.01 or decimal <= 0.99:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+19786432271",
        body=f"{STOCK}: {final_percent}\nHeadline: {data_2["articles"][0]["title"]}\nBrief: {data_2["articles"][0]["description"]}",
        to=""
    )

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
