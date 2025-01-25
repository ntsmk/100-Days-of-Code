from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()
email = os.getenv("email")
password = os.getenv("password")
uid = os.getenv("uid")
promised_down = 100
promised_up = 10

SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://x.com/"

class InternetSpeedTwitterBot:
    def __init__(self):

        self.driver = webdriver.Firefox()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        time.sleep(5)
        go = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test")
        go.click()
        time.sleep(60)

        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(5)
        signin = self.driver.find_element(By.CSS_SELECTOR, "a.css-175oi2r:nth-child(2)")
        signin.click()
        time.sleep(5)
        email_input = self.driver.find_element(By.CSS_SELECTOR, ".r-30o5oe")
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        uid_input = self.driver.find_element(By.CSS_SELECTOR, ".r-30o5oe")
        uid_input.send_keys(uid)
        uid_input.send_keys(Keys.ENTER)
        time.sleep(5)
        password_input = self.driver.find_element(By.CSS_SELECTOR, ".r-homxoj")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
        post = self.driver.find_element(By.CSS_SELECTOR, ".r-1fkl15p")
        post.click()
        time.sleep(5)

        tweet = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Post text')]")

        tweet.send_keys(f"Hey Internet Provider, why is my internet speed is down: {self.down} Mbps up: {self.up} Mbps?\n"
                        f"Even though I pay money for down: {promised_down} Mbps up:{promised_up} Mbps!")

        post = self.driver.find_element(By.XPATH, "//button[@data-testid='tweetButton']")
        post.click()
        print("post completed")

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
