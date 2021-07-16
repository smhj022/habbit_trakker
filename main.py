import requests
from datetime import datetime
import os 

USERNAME = "suyash"
TOKEN = os.environ["TOKEN"]
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

# create a user

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# create a graph

graph_api = f"{pixela_endpoint}/{USERNAME}/graphs"
header = {
    "X-USER-TOKEN": TOKEN
}

# graph_config = {
#     "id": f"{GRAPH_ID}",
#     "name": "Coding Graph",
#     "unit": "mins",
#     "type": "int",
#     "color": "ajisai"
#
# }
#
# response = requests.post(url=graph_api, json=graph_config, headers=header)
# print(response.text)

# create a pixel

post_graph_api = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2021, month=6, day=7)
date = today.strftime("%Y%m%d")
print(date)
graph_params = {
    "date": f"{date}",
    "quantity": "150"
}
#
# response = requests.post(url=post_graph_api, json=graph_params, headers=header)
# print(response.text)


# update a pixel

# update_graph_api = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
#
# update_graph_config = {
#     "quantity": "120"
# }
#
# response =requests.put(url=update_graph_api, json=update_graph_config, headers=header)
# print(response.text)

delete_graph_api = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

response =requests.delete(url=delete_graph_api, headers=header)
print(response.text)