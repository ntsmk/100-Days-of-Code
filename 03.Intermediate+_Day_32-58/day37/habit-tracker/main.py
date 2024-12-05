import requests

USERNAME = "whereismycoffee"
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Walking Graph",
    "unit": "steps",
    "type": "int",
    "color": "sora"

}

response = requests.post(url=graph_endpoint, json=graph_config)
print(response.text)
