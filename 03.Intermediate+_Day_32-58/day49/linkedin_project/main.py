from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time
from selenium.common.exceptions import StaleElementReferenceException

URL = ("https://www.linkedin.com/jobs/search/"
       "?currentJobId=4117936833"
       "&f_AL=true"
       "&keywords=python%20developer"
       "&origin=JOB_SEARCH_PAGE_JOB_FILTER"
       "&refresh=true")
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

# # click save and follow
# time.sleep(5)
# # save = driver.find_element(By.CSS_SELECTOR, 'button.jobs-save-button:nth-child(3)')
# # save = driver.find_element(By.CSS_SELECTOR, 'button.jobs-save-button:nth-child(3)')
# # save.click() # it works after relocating again
# company = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__company-name > a:nth-child(1)")
# company = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__company-name > a:nth-child(1)")
# company = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__company-name > a:nth-child(1)")
# company.click()
# time.sleep(2)
#
# follow = driver.find_element(By.CSS_SELECTOR, "button.follow:nth-child(1)")
# follow.click()
# # not_now = driver.find_element(By.CSS_SELECTOR, "#ember518")
# # not_now = driver.find_element(By.CSS_SELECTOR, "#ember518")
# # not_now.click()
# turn_on = driver.find_element(By.CSS_SELECTOR, "#ember522")
# # turn_on.click()
# driver.execute_script("arguments[0].click();", turn_on)

time.sleep(20) # because of security check
jobs = driver.find_elements(By.CSS_SELECTOR, "div[class^='artdeco-entity-lockup__subtitle']")
for i in range(7):
    jobs[i].click()
    try:
       save = driver.find_element(By.CSS_SELECTOR, 'button.jobs-save-button:nth-child(3)')
       save.click()
    except StaleElementReferenceException:
       save = driver.find_element(By.CSS_SELECTOR, 'button.jobs-save-button:nth-child(3)')
       save.click()
# todo need to get all job info