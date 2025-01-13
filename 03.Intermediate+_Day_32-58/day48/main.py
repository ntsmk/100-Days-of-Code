from selenium import webdriver

# keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

# driver.close() -> just one tab
# driver.quit() -> all tabs
