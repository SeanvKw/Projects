import requests
from pprint import pprint


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.header = {
            "Authorization": f"Basic Zmdham5lYWF3ZTpkemlhbGExMjMwNTE5MjEyMw=="
        }
        self.SHEETY_ENDPOINT = "https://api.sheety.co/1acdf326c0a5cc1e86c0c1bd17585861/kopiaFlightDeals/prices"

    def get_data(self):
        self.data = requests.get(url=self.SHEETY_ENDPOINT)
        self.response = self.data.json()
        pprint(self.response)
