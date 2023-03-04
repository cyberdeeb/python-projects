from news_data import texts
from stock_data import delta
from twilio.rest import Client
import os


def main():

    # Create Twilio client
    account_sid = os.getenv('SID')
    auth_token = '75ba41646cb94d52152ac59c502f6d9f' #os.getenv('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    if abs(delta) > 2:
        for text in texts:
            message = client.messages.create(
                body=text,
                from_='+18446781985',
                to='+17026838052'
            )
            print(text)

        print(message.status)



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

main()
