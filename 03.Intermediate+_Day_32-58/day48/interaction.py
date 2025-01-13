from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_num = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")[1]
# article_num.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# find the search <input>
search = driver.find_element(By.NAME, value="search")

# sending keyboad input to the search bar
search.send_keys("Python", Keys.ENTER)
