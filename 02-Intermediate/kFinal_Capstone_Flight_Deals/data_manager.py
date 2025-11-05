import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/1acdf326c0a5cc1e86c0c1bd17585861/kopiaFlightDeals/prices"
        self.data = requests.get(url=self.SHEETY_ENDPOINT)
