import smtplib
import datetime as dt
import pandas

now = dt.datetime.now()
current_month = now.month
current_day = now.day

df = pandas.read_csv("birthdays.csv")
dict = df.to_dict(orient="records")
for i in range(len(dict)):
    if dict[i]['month'] == current_month and dict[i]['day'] == current_day:
        print(dict[i]['name'])


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




