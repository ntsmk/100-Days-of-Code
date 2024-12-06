import requests
from datetime import datetime


USERNAME = "whereismycoffee"
TOKEN = ""
GRAPH_ID = "graph1"

# creating account
pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

# creating graphs
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "steps",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# posting value to graph
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2024, month=12, day=5)
print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9000",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# updating value to graph
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

update_pixel_config = {
    "quantity": "15000",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# deleting graph
# response = requests.delete(url=pixel_endpoint, headers=headers)
# print(response.text)