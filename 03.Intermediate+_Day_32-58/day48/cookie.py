from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, value="cookie")

minutes = 5
timeout = 60 * minutes  # [seconds]
timeout_start = time.time()
purchase_frequency = 7

next_check = time.time() + purchase_frequency
while time.time() < timeout_start + timeout:
    cookie.click()
    money = int(driver.find_element(By.ID, value="money").text)
    items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")[7::-1]
    if time.time() >= next_check:
        for item in items:
            item_cost = int(item.text.split("-")[1].replace(",", ""))
            if money > item_cost:
                print(f"Clicking on {item.text.split("-")[0]} with cost: {item_cost}")
                item.click()
                break
            # else:
                # print(f"Not enough money: {money} for item cost: {item_cost}")
        next_check = time.time() + purchase_frequency

cookie_second = driver.find_element(By.ID, value="cps").text
driver.quit()
print(cookie_second)
