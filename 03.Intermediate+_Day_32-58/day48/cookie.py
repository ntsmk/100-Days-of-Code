from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

timeout = 300   # [seconds]
timeout_start = time.time()

items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")[:8]
# item_cost = int(item.text.split("-")[1].replace(",", ""))

while True:
    cookie.click()
    # money = int(driver.find_element(By.ID, value="money").text)
    # item_cost = int(items[0].text.split("-")[1].replace(",", ""))
    # if money > item_cost:
    #     items[0].click()



# cookie_second = driver.find_element(By.ID, value="cps").text