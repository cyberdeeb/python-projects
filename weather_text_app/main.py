import os
import requests
from twilio.rest import Client


def main():

    # Create Twilio client
    account_sid = os.getenv('SID')
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    # If it is going to rain then send sms
    if will_rain():
        message = client.messages \
            .create(
            body="It looks like it's going to rain today! Don't forget your jacket and ☔️",
            from_='+18446781985',
            to='+17026838052'
            )

    print(message.status)


def will_rain():

    # Try to use OWM api
    try:
        owm_api_key = os.getenv('OWM_API_KEY')
        exclude = 'current,minutely,daily'
        lat = 34.052235
        lon = -118.243683

        response = requests.get(f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}'
                                f'&appid={owm_api_key}')
    except requests.RequestException:
        print(f'There was an error: {response.status_code}')

    # Create JSON file holding 12 hours of data
    try:
        data = response.json()
    except (KeyError, TypeError, ValueError):
        print("There was an error. Please rerun.")

    data_slice = data['hourly'][:12]
    hourly_data = {}
    hour = 0

    # Fill hourly_data with only hours that will rain
    for _ in data_slice:
        weather_id = data_slice[hour]['weather'][0]['id']
        if weather_id < 700:
            hourly_data[hour] = weather_id
        hour += 1

    # If hourly_data contains rain data then return True
    if hourly_data:
        return True


main()
