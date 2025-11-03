import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "hiwbdaoiwebsnmaiejskake",
    "username": "seanvkw",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
data = requests.post(url=pixela_endpoint, json=user_params)
print(data.text)
