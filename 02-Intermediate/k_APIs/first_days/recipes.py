import requests
import datetime as dt
MY_LAT = 51.164472
MY_LNG = 16.872592
# try:
#     resp = requests.get("http://api.open-notify.org/iss-now.json")
# except:
#     print("Error, Surely ISS Crashed!")
# else:
#     print(resp.json())

# resp = requests.get("http://api.open-notify.org/iss-now.json", timeout=5)
# resp.raise_for_status()

# data = resp.json()["iss_position"]  # Gather specific info from json API

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(data)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = dt.datetime.now()
print(time_now.hour)
