from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/instant_pot/"
response = requests.get(URL)
amazon_page = response.text
soup = BeautifulSoup(amazon_page, "html.parser")
whole_price = soup.find(class_="a-price-whole").getText()
decimal = soup.find(class_="a-price-fraction").getText()
print(f"{whole_price}{decimal}")

# step 1 is done