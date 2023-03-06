import datetime as dt
import os
import requests

url = 'https://pixe.la/v1/users'
TOKEN = os.getenv('TOKEN')
USERNAME = 'dweeber'
graph_id = 1
graph_endpoint = f'{url}/{USERNAME}/graphs/graph{graph_id}'

today = dt.datetime.now()

pixel_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '50'
}

headers ={
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url=graph_endpoint, json=pixel_config, headers=headers)
print(response.text)

