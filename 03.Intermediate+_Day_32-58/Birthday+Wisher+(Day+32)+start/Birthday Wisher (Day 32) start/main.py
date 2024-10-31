import smtplib
import random
import datetime as dt
import schedule

with open("quotes.txt") as file:
    random_quote = random.choice(file.readlines())

my_email = "whereismycoffee9@gmail.com"
password = ""

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Here is inspirational quote for you\n\n{random_quote}")

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(day_of_week) Thursday = 3
# print(year, month)
date_of_birth = dt.datetime(year=1996, month=3, day=8)
# print(date_of_birth)

if day_of_week == 2:
    send_email()
else:
    print("today is not that day")
