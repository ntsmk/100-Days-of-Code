from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()
email = os.getenv("email")
password = os.getenv("password")

URL = "https://www.speedtest.net/"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.promised_down = 100
        self.promised_up = 10
        self.driver = webdriver.Firefox()

    def get_internet_speed(self):
        self.driver.get(URL)
        time.sleep(5)
        go = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test")
        go.click()

        time.sleep(40)

        down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
        up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
        print(f"down: {down.text}")
        print(f"up: {up.text}")

    def tweet_at_provider(self):
        pass


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
