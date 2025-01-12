from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib

# STATIC_URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.ca/Apple-iPhone-13-256-GB/dp/B0DPJG9KWM?ref_=Oct_d_onr_d_3379583011_4&pd_rd_w=GUIsY&content-id=amzn1.sym.7b441bd6-a65d-4d2f-9222-f35257c4b0dd&pf_rd_p=7b441bd6-a65d-4d2f-9222-f35257c4b0dd&pf_rd_r=FJSDGB540TE0884RMMF1&pd_rd_wg=7uppP&pd_rd_r=374f1ecc-f2a7-4eb6-bffa-6edaea9300df&pd_rd_i=B0DPJG9KWM"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
response = requests.get(LIVE_URL, headers=header)
amazon_page = response.text
soup = BeautifulSoup(amazon_page, "html.parser")
max_price = 700

# step 1
title = soup.find(id="productTitle").getText().split("\n")[0].split("        ")[1].strip()
price = soup.find(class_="a-offscreen").getText().split("$")[1]
print(f"item title: {title}")
print(f"item price: ${price}")

# step 2
load_dotenv()
smtp_address = os.getenv("SMTP_ADDRESS")
email_address = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

def sendEmail():
    with smtplib.SMTP(smtp_address) as connection:
        connection.starttls()
        connection.login(user=email_address, password=password)
        connection.sendmail(from_addr=email_address,
                            to_addrs=email_address,
                            msg=f"Subject:Amazon Price Alert\n\n{title} is now "f"${price}, "
                                f"go check it out!\n{LIVE_URL}")

if float(price) < max_price:
    sendEmail()
    print("Email sent")
