import smtplib
import datetime as dt
import pandas
import random

now = dt.datetime.now()
current_month = now.month
current_day = now.day

df = pandas.read_csv("birthdays.csv")
dict = df.to_dict(orient="records")

my_email = "whereismycoffee9@gmail.com"
password = "gwhvyxuczlqgkmaq"

replaced_text = ""

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=the_email,
                            msg=f"Subject:Happy Birthday\n\n{replaced_text}")
    print("mail sent")

for i in range(len(dict)):
    if dict[i]['month'] == current_month and dict[i]['day'] == current_day:
        the_name = dict[i]['name']
        the_email = dict[i]['email']
        random_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_number}.txt") as file:
            f = file.read()
            replaced_text = f.replace("[NAME]", the_name)
        send_email()
    else:
        print("this is not the birthday person")
