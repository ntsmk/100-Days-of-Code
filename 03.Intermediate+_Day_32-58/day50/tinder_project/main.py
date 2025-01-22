from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://tinder.com/"

load_dotenv()
email = os.getenv("email")
password = os.getenv("password")
minutes = 5
timeout = 60 * minutes  # [seconds]
timeout_start = time.time()

driver = webdriver.Firefox()
driver.get(URL)

# navigate to login
time.sleep(5)
login = driver.find_element(By.CSS_SELECTOR, "a.c1p6lbu0")
login.click()

time.sleep(2)
facebook_login = driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Log in with Facebook']")
facebook_login.click()

# change window and login with Facebook
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email_input = driver.find_element(By.CSS_SELECTOR, "#email")
email_input.send_keys(email)
password_input = driver.find_element(By.CSS_SELECTOR, "#pass")
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)
# need to do puzzle manually after this

driver.switch_to.window(base_window)
print(driver.title)

# dismiss all requests
time.sleep(30)
print("signed in to Tinder")

allow = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]")
allow.click()
print("clicked allow")

time.sleep(15)
miss_out = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[2]")
miss_out.click()
print("clicked miss out")

# swiping part. Arrow Left = Nope, Arrow Right = like
time.sleep(5) # wait for loading
while time.time() < timeout_start + timeout:
    ActionChains(driver).key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
    time.sleep(2) # wait for the next swipe

