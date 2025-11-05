import requests
from datetime import datetime


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.today = datetime.now()
        self.SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.KEY = "GFyI23jafHfhhfWWN56D2vQ0uyDpLuNI"
        self.SECRET = "u76LSKlGEhTkLt34"
        self.params = {
            "grant_type": f"client_credentials&client_id={self.KEY}&client_secret={self.SECRET}",
            "client_id": self.KEY,
            "client_secret": self.SECRET,

        }
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.data = requests.post(
            url=self.SEARCH_ENDPOINT, json=self.params, headers=self.header)
        self.data.json()
        print(self.data.text)


FlightSearch()
