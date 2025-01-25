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
        password_input = self.driver.find_element(By.XPATH, "//input[@aria-label='Password']")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

        time.sleep(7)
        not_now1 = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div")
        not_now1.click()
        time.sleep(3)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{similar_account}/")
        time.sleep(5)

        # follower_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/nintendoamerica/followers/']")
        follower_link = self.driver.find_element(By.XPATH, "//a[contains(@href, '/followers/')]")
        follower_link.click()
        time.sleep(5)

        # Scroll the followers popup
        popup = self.driver.find_element(By.XPATH, "//div[@role='dialog']") # no error but something wrong
        print("successfully load popup")
        for _ in range(10):  # Adjust the range to scroll more or less
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup) # not working, no error
            time.sleep(2)  # Pause to allow content to load


    def follow(self):
        pass

insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()