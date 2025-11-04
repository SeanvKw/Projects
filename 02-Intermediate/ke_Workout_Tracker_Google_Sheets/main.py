import requests
from datetime import datetime


GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 189
AGE = 19


APP_ID = "YOURAPPID"
KEY = "YOURKEY"
SHEETY_KEY = "YOUR 64BASE ENCRYPTED SHEETY API KEY"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


get_sheety_endpoint = "https://api.sheety.co/1acdf326c0a5cc1e86c0c1bd17585861/kopiaMyWorkouts/workouts"
post_sheety_endpoint = "https://api.sheety.co/1acdf326c0a5cc1e86c0c1bd17585861/kopiaMyWorkouts/workouts"

get_sheety_req = requests.get(url=get_sheety_endpoint)
sheety_result = get_sheety_req.json()

now = datetime.now()
payload = {
    "workout": {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "exercise": "Run",
        "duration": 25,
        "calories": 105
    }
}
sheety_header = {
    "Authorization": f"Basic {SHEETY_KEY}"
}
post_sheety_req = requests.post(
    url=post_sheety_endpoint, json=payload, headers=sheety_header)
post_sheety_req.raise_for_status()
print(post_sheety_req.text)
