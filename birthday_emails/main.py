import datetime as dt
import os
import pandas as pd
import random as r
import smtplib


def main():

    # Login details to test email
    my_email = 'theboywholived409@gmail.com'
    password = 'gjxqryzdxjnuummd'

    # Open and chose random quote
    with open('quotes.txt') as quotes:
        quote = r.choice(quotes.readlines())

    # Open updated letter to send
    with open(f'sent_letters/{day_check()[0]}.txt') as file:
        doc = file.read()

    # Open connection and send email containting saved text and quote
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=day_check()[1],
            msg=f'Subject:Happy Birthday!\n\n{doc}\n\n{quote}'
        )


# Check if today matches a birthday in the birthdays.csv
def day_check():
    birthday_data = pd.read_csv('birthdays.csv')
    month = dt.datetime.now().month
    day = dt.datetime.now().day
    person = birthday_data[(birthday_data['month'] == month) & (birthday_data['day'] == day)]

    if person.empty:
        return False
    else:
        return person['name'].item(), person['email'].item()


# If there is a birthday, pick a random letter from letter templates
def document():
    if day_check():
        name = day_check()[0]
        letter = r.choice(os.listdir('letter_templates'))
        #  Replace the [NAME] with the person's actual name from birthdays.csv
        with open(f'letter_templates/{letter}', 'r') as file:
            with open(f'sent_letters/{name}.txt', 'w') as v2:
                v1 = file.read()
                v2.write(v1.replace('[NAME]', name))
    else:
        return False


document()
main()
