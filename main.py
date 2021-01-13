import requests
from datetime import datetime

USERNAME = "*****"
TOKEN = "**********************"
GRAPH_ID = "******"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "BJJ graph",
    "unit": "hours",
    "type": "int",
    "color": "sora"

}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

response = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
print(response.text)
