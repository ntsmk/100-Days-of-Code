from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()
username = os.getenv("username")
password = os.getenv("password")
similar_account = "chefsteps"
