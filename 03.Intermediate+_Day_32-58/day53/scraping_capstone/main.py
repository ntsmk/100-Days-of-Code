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

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

class DataEntry:
    def __init__(self):
        self.links = []
        self.prices = []
        self.addresses = []

    def scrape_data(self):
        response = requests.get(ZILLOW_URL, headers=header)
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

        # print(self.links) # len 89 -> why?? links[1::2] -> now it matches 44
        # print(self.prices) # len 44
        # print(self.addresses) # len 44

    def send_data(self):

        self.driver = webdriver.Firefox()
        self.driver.get(FORM_URL)
        time.sleep(5)

        # todo need to figure out send_keys, and then use for loop range(len(self.links))
        for i in range(len(self.links)):
            q1 = self.driver.find_element(By.XPATH, "//input[contains(@aria-describedby, 'i2')]")
            q1.send_keys(self.addresses[i])

            q2 = self.driver.find_element(By.XPATH, "//input[contains(@aria-describedby, 'i7')]")
            q2.send_keys(self.prices[i])

            q3 = self.driver.find_element(By.XPATH, "//input[contains(@aria-describedby, 'i12')]")
            q3.send_keys(self.links[i])

            submit_button = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
            submit_button.click()
            time.sleep(3)
            another_one = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            another_one.click()
            time.sleep(3)

if __name__ == '__main__':
    data_entry = DataEntry()
    data_entry.scrape_data()
    data_entry.send_data()



