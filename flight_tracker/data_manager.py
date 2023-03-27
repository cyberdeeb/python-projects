import requests

SHEETY_URL = 'https://api.sheety.co/6ae4bde23162cc8bf92e1e8b6e96124c/flightDeals/prices'

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHEETY_URL)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def get_codes(self):

        for city in self.destination_data:

            tequila_url = 'https://api.tequila.kiwi.com/locations/query'

            header = {
                'apikey': 'ozli_ecSPUgQOM1EPpLMHHYecV4ibJp-',
            }

            params = {
                'term': city['city'],
            }

            response = requests.get(url=tequila_url, params=params, headers=header)
            data = response.json()

            city['iataCode'] = data['locations'][0]['code']

    def update_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_URL}/{city['id']}",
                json=new_data
            )
            print(response.text)