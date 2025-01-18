from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4128218882&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
load_dotenv()
email = os.getenv("email")
password = os.getenv("password")

driver = webdriver.Firefox()
driver.get(URL)

time.sleep(2)
sign_in = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/section/div/div/div/div[2]/button")
time.sleep(2)
sign_in.click()

email_or_phone = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
email_or_phone.send_keys(email)

password_for_linkedin = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
password_for_linkedin.send_keys(password)
password_for_linkedin.send_keys(Keys.ENTER)
