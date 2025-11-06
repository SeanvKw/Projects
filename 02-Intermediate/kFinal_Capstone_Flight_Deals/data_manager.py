import requests
from pprint import pprint


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.header = {
            "Authorization": f"Basic Zmdham5lYWF3ZTpkemlhbGExMjMwNTE5MjEyMw=="
        }
        self.SHEETY_ENDPOINT = "https://api.sheety.co/1acdf326c0a5cc1e86c0c1bd17585861/kopiaFlightDeals/prices"
        destination_data = {}

    def get_data(self):
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.header
            )
            print(response.text)
