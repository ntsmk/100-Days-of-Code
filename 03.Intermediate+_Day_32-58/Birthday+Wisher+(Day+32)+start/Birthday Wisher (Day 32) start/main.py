# import smtplib
#
# my_email = "whereismycoffee9@gmail.com"
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=my_email,
#                         msg="Subject:We wish you Merry Christmas\n\nThis is body of my email")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
print(year, month)

date_of_birth = dt.datetime(year=1996, month=3, day=8)

print(date_of_birth)