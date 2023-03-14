from nutrition_data import day, time, calories, duration, name
import os
import requests

sheety_url = 'https://api.sheety.co/6ae4bde23162cc8bf92e1e8b6e96124c/fitnessTracker/workouts'

# Bearer Token Authentication
bearer_headers = {
    "Authorization": os.getenv('AUTH')
}

row_data = {
    'workout': {
        'date': day,
        'time': time,
        'exercise': name,
        'duration': duration,
        'calories': calories
    }
}

response = requests.post(url=sheety_url, json=row_data, headers=bearer_headers)
print(response.status_code, response.text)
