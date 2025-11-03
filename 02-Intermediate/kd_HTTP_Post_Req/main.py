import requests
from datetime import datetime as dt
USERNAME = "seanvkw"
TOKEN = "hiwbdaoiwebsnmaiejskake"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
pixela_endpoint = "https://pixe.la/v1/users"
# data = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graphicalpro5"
graph_params = {
    "id": GRAPH_ID,
    "name": "Riding graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# post_request = requests.post(
#     url=graph_endpoint, json=graph_params, headers=headers)
TODAY = dt.now()
YESTERDAY = dt(year=2025, month=11, day=2)
graph_body = {
    "date": TODAY.strftime("%Y%m%d"),
    "quantity": str(input("How many kilometers did you cycle today? "))
}
graph_value_post = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

graph_request = requests.post(
    url=graph_value_post, headers=headers, json=graph_body)
graph_update_params = {
    "quantity": "5"
}
graph_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{YESTERDAY.strftime('%Y%m%d')}"
update_graph = requests.put(
    url=graph_update, headers=headers, json=graph_update_params)
print(update_graph.text)


delete_pixel = requests.delete(url=graph_update, headers=headers)
print(delete_pixel.text)
