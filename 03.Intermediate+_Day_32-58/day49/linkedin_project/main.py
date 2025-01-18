from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4128218882&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
load_dotenv()
email= os.getenv("email")
password= os.getenv("password")

driver = webdriver.Firefox()
driver.get(URL)

# todo need to figure out how to capture sign in button. Goal is Automatically Login to LinkedIn

sign_in = driver.find_element(By.CSS_SELECTOR, "#sign-in-modal button")
time.sleep(2)
# print(sign_in)
sign_in.click()
