import datetime as dt
import html
import os
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

yesterday = dt.datetime.today().date() - dt.timedelta(days=1)
two_days = dt.datetime.today().date() - dt.timedelta(days=2)

try:
    params = {
        'apiKey': os.getenv('NEWS_API_KEY'),
        'q': f'{STOCK}, {COMPANY_NAME}',
        'searchIn': 'title',
        'from': two_days,
        'to': yesterday,
        'language': 'en',
        'sortBy': 'popularity',
        'pageSize': 4
    }

    response = requests.get(url=NEWS_ENDPOINT, params=params)
except requests.RequestException:
    print(f'There was an error: {response.status_code}')

    # Create JSON file holding 12 hours of data
try:
    data = response.json()['articles']
except (KeyError, TypeError, ValueError):
    print("There was an error. Please rerun.")

texts = [html.unescape(f"\nHeadline: {story['title']}. \nBrief: {story['description']}") for story in data]
