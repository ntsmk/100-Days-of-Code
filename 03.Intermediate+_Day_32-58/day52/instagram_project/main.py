from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()
uid = os.getenv("uid")
password = os.getenv("password")
similar_account = "nintendoamerica"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        # aria-label="Phone number, username, or email"
        username_input = self.driver.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']")
        username_input.send_keys(uid)
        # aria-label="Password"

        # todo need to figure out how to fix
        password_input = self.driver.find_element((By.XPATH, "//input[@aria-label='Password']"))
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        pass

    def follow(self):
        pass

insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()