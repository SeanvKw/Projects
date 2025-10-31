import requests
import os
from twilio.rest import Client
parameters = {
    "lat": 51.164471,
    "lon": 16.872593,
    "appid": "",
    "cnt": 4,
}
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

five_hours = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast", params=parameters, timeout=5)
five_hours_data = five_hours.raise_for_status()
five_hours_data = five_hours.json()

mynumber = os.getenv("mynumber")

print(mynumber)
will_rain = False

for hour_data in five_hours_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if not will_rain:
    message = client.messages.create(
        messaging_service_sid='MG8ec5aa470f5784d4332cc522a36ac9e9',
        body='Bring an umbrella!',
        from_='+12297017683',
        to=str(mynumber)
    )
