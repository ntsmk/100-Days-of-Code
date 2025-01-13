from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Firefox()
driver.get("https://www.python.org/")

# price_dollor = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# print(f"The price is ${price_dollor}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# bug_link = driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
# print(bug_link.text)
# todo create a dictionary contains "Upcoming Events"
events_time = driver.find_elements(By.CSS_SELECTOR, value="medium-widget event-widget last")
print(events_time)

# driver.close() -> just one tab
# driver.quit() -> all tabs
