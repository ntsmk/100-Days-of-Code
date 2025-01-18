from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4128218882&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
load_dotenv()
email= os.getenv("email")
password= os.getenv("password")

driver = webdriver.Firefox()
driver.get(URL)

