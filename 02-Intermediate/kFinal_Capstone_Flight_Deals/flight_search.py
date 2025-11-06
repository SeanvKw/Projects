import requests
import time
from datetime import datetime, timedelta


class FlightSearch:

    TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
    SEARCH_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
    FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    def __init__(self):
        # Amadeus credentials
        self.KEY = "GFyI23jafHfhhfWWN56D2vQ0uyDpLuNI"
        self.SECRET = "u76LSKlGEhTkLt34"

        # Token
        self.access_token = None
        self.token_expiry_time = 0

        self.get_access_token()

    def get_access_token(self):
        """Fetch a new access token from Amadeus."""
        print("Requesting new access token...")
        params = {
            "grant_type": "client_credentials",
            "client_id": self.KEY,
            "client_secret": self.SECRET
        }
        self.header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(
            url=self.TOKEN_URL, data=params, headers=self.header)

        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data["access_token"]
            # usually 1799 seconds (~30 min)
            expires_in = token_data["expires_in"]
            self.token_expiry_time = time.time() + expires_in - 60
            print("✅ Token retrieved successfully.")
        else:
            raise Exception(
                f"❌ Token request failed: {response.status_code} - {response.text}")

    def ensure_token_valid(self):
        """Refresh the token if it's expired or missing."""
        if not self.access_token or time.time() >= self.token_expiry_time:
            self.get_access_token()

    def get_iata_code(self, city_name):
        params = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        header = {
            "Authorization": f"Bearer {self.access_token}"
        }
        resp = requests.get(url=self.SEARCH_URL, params=params,
                            headers=header)
        try:
            code = resp.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        self.ensure_token_valid()
        headers = {"Authorization": f"Bearer {self.access_token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=self.FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
