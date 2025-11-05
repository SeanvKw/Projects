import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.KEY = "GFyI23jafHfhhfWWN56D2vQ0uyDpLuNI"
        self.SECRET = "u76LSKlGEhTkLt34"
        self.params = {
            "client_id": self.KEY,
            "client_secret": self.SECRET
        }
        self.data = requests.post(url="", json=self.params)
        self.data.json()
        print(self.data)
