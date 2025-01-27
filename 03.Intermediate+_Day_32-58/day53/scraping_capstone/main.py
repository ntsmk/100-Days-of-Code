# step 1
# use beautifulsoup and scrape data (links, prices, address) and create the lists for each and then store it
# https://appbrewery.github.io/Zillow-Clone/

import requests
from bs4 import BeautifulSoup
import pprint

URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(URL)
zillow_page = response.text
soup = BeautifulSoup(zillow_page, "html.parser")

# Links
link_elements = soup.select(selector="a", class_="StyledPropertyCardDataArea-anchor")
links = [link.get('href') for link in link_elements if "www.zillow.com" in link.get('href')]
print(links) # [0] is just www.zillow.com, Links is done.

# Prices
price_elements = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
prices = [price.text[:6] for price in price_elements]
print(prices) # it returns $2,895 format. Done

# Address
address_elements = soup.find_all("address", attrs={"data-test": "property-card-addr"})
addresses = [address.text.strip().replace("|", "") for address in address_elements]
print(addresses) # it returns cleaned up data

# step 1 is done


# step 2
# use selenium and send data (price/address/link) for the form
# https://docs.google.com/forms/d/e/1FAIpQLSfsjD62Gwntd50JDjRr-9_utIIG23_YwBGX2g_rc3V6CNTZOA/viewform
