from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv("email")
password = os.getenv("password")

promised_down=  100
promised_up = 10

URL = "https://www.speedtest.net/"

driver = webdriver.Firefox()
driver.get(URL)