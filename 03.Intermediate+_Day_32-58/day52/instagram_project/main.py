from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()
username = os.getenv("username")
password = os.getenv("password")
similar_account = "nintendoamerica"

instagram_url = "https://www.instagram.com/"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass

insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()