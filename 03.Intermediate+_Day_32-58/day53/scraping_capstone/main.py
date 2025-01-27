import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

# step 1
# use beautifulsoup and scrape data (links, prices, address) and create the lists for each and then store it
# https://appbrewery.github.io/Zillow-Clone/
# step 2
# use selenium and send data (price/address/link) for the form
# https://docs.google.com/forms/d/e/1FAIpQLSfsjD62Gwntd50JDjRr-9_utIIG23_YwBGX2g_rc3V6CNTZOA/viewform

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfsjD62Gwntd50JDjRr-9_utIIG23_YwBGX2g_rc3V6CNTZOA/viewform"
EMAIL = os.getenv("email")
PASSWORD = os.getenv("password")

class DataEntry:
    def __init__(self):
        self.links = []
        self.prices = []
        self.addresses = []

    def scrape_data(self):
        response = requests.get(ZILLOW_URL)
        zillow_page = response.text
        soup = BeautifulSoup(zillow_page, "html.parser")

        # Links
        link_elements = soup.select(selector="a", class_="StyledPropertyCardDataArea-anchor")
        links = [link.get('href') for link in link_elements if "www.zillow.com" in link.get('href')]
        self.links = links[1::2]

        # Prices
        price_elements = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
        self.prices = [price.text[:6] for price in price_elements]

        # Address
        address_elements = soup.find_all("address", attrs={"data-test": "property-card-addr"})
        self.addresses = [address.text.strip().replace("|", "") for address in address_elements]

        # print(len(self.links[1::2])) # len 89 -> why?? links[1::2] -> now it matches 44
        # print(len(self.prices)) # len 44
        # print(len(self.addresses)) # len 44

    def send_data(self):
        self.driver = webdriver.Firefox()
        self.driver.get(FORM_URL)

        # todo need to figure out XPATH
        q1 = self.driver.find_element(By.XPATH, "")
        q1.send_keys(self.addresses[0])

        q2 = self.driver.find_element(By.XPATH, "")
        q2.send_keys(self.prices[0])

        q3 = self.driver.find_element(By.XPATH, "")
        q3.send_keys(self.links[0])

        # done following
        submit_button = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
        submit_button.click()
        time.sleep(3)
        another_one = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        another_one.click()
        time.sleep(3)


if __name__ == '__main__':
    data_entry = DataEntry()
    # data_entry.scrape_data()
    data_entry.send_data()





