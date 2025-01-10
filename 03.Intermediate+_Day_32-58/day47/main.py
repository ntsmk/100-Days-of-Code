from bs4 import BeautifulSoup
import requests


URL = "https://appbrewery.github.io/instant_pot/"
# URL = "https://www.amazon.ca/Google-Pixel-128GB-Canadian-Unlocked/dp/B0BL8HPF13/ref=sr_1_4?crid=15JYH9MH8W5M9&dib=eyJ2IjoiMSJ9.K_0WymDeRtI01PsTKd3J7hdtuhjzUkGO8gPJRPu02zOzfawGu04A7J9uItOTxPdcP4yIoN4ogr0x58_8L2ytkqQn3z_mUpirDgOrvrHY7AH7t56DNO8TYVRFvzGs0qGQqhKEgPH8yR2GUZ4tlaDXNLtVqzdsgB604BWqRrqtsC7J4gZZdrqRWe4Pr0ZxWfYiCKFWGxyvlKTAzrK6T5_19T4o3Zo0G_1XLQHbewPoprz7lMuC3kQ5LVz5bzTRKeeA8dzcBhpGyul4J_SP6wZrQ37kC__S1CSgpIJKfP7jwDzv1R7tQSvTRD7chVBUFX7inWCYAifXQpYj-ZmzdGnR338UFFKtdz4SZt4G7RLu81_MTRVEaRqAIpehQfUDYPkvMiuWLlrGFtgvDFrXbQEIUVZSiU-CLYvjC4ZnTMZNqK3qvyLBlCUGFQrbW_UUg0Qp.66DGeXI0Zzi3qo_9IT2XSDwt9BEoRr6lyl3YZ1XRrfE&dib_tag=se&keywords=google+pixel&qid=1736468397&sprefix=%2Caps%2C347&sr=8-4"
response = requests.get(URL)
amazon_page = response.text
soup = BeautifulSoup(amazon_page, "html.parser")
whole_price = soup.find(class_="a-price-whole").getText()
decimal = soup.find(class_="a-price-fraction").getText()
print(f"{whole_price}{decimal}")

# tried in the real one but it didn't work
# price = soup.select(selector="tr", class_="a-offscreen")
# print(price)

# step 1 is done