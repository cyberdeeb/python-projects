import datetime as dt
import os
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

yesterday = dt.datetime.today().date() - dt.timedelta(days=1)
two_days = dt.datetime.today().date() - dt.timedelta(days=2)

try:
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': STOCK,
        'apikey': os.getenv('STOCK_API_KEY')
    }

    response = requests.get(url=STOCK_ENDPOINT, params=params)
except requests.RequestException:
    print(f'There was an error: {response.status_code}')

    # Create JSON file holding 12 hours of data
try:
    data = response.json()
except (KeyError, TypeError, ValueError):
    print("There was an error. Please rerun.")

yesterday_price = float(data['Time Series (Daily)'][f'{yesterday}']['4. close'])
two_days_price = float(data['Time Series (Daily)'][f'{two_days}']['4. close'])

delta = round((((yesterday_price - two_days_price) / two_days_price) * 100), 2)
price_change = round((yesterday_price * (delta / 100)) + yesterday_price, 2)