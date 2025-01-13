from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("John")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Doe")

email = driver.find_element(By.NAME, value="email")
email.send_keys("abc@gmail.com")

submit = driver.find_element(By.CLASS_NAME, value="btn")
submit.send_keys(Keys.ENTER)
# driver.quit()
