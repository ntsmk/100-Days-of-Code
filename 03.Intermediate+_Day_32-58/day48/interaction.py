from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")[1].text
print(num)