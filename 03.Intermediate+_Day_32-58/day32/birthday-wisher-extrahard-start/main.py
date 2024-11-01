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
        the_name = dict[i]['name']
        the_email = dict[i]['email']
        print(the_name)
        print(the_email)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# todo need to work on this

# 4. Send the letter generated in step 3 to that person's email address.
my_email = "whereismycoffee9@gmail.com"
password = ""
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=the_email,
                            msg=f"Subject:Happy Birthday\n\n{random_letter}")



