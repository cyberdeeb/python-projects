import requests


APP_ID = ''
API_KEY = ''
fitness_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY,
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
print(response.text)