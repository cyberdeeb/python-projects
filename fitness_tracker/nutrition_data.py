import os
from datetime import datetime as dt
import requests

fitness_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
header = {
    "x-app-id": os.getenv('APP_ID'),
    'x-app-key': os.getenv('API_KEY'),
    "x-remote-user-id": '0',
}

workout = input('Tell me which exercises you did: ')

params = {
    "query": workout,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

response = requests.post(url=fitness_url, json=params, headers=header)
data = response.json()

name = data['exercises'][0]['name'].title()
duration = data['exercises'][0]['duration_min']
calories = data['exercises'][0]['nf_calories']

today = dt.now()
date = dt.strftime(today, "%Y/%m/%d %H:%M:%S")
day, time = date.split(" ")