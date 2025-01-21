from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

URL = "https://tinder.com/"

load_dotenv()
email = os.getenv("email")
password = os.getenv("password")

driver = webdriver.Firefox()
driver.get(URL)

time.sleep(5)
login = driver.find_element(By.CSS_SELECTOR, "a.c1p6lbu0")
login.click()

time.sleep(2)
facebook_login = driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Log in with Facebook']")
facebook_login.click()

email_input = driver.find_element(By.CSS_SELECTOR, "input[class^='email']") # need to modify
email_input.send_keys(email)

password_input = driver.find_element(By.CSS_SELECTOR, "input[id='pass']") # need to modify
password_input.send_keys(password)