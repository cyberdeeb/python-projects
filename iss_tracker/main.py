from datetime import datetime as dt
import requests
import smtplib

# Your latitude & longitude
MY_LAT = 34.052235
MY_LONG = -118.243683


def main():

    # Login details to test email
    my_email = 'theboywholived409@gmail.com'
    password = 'lmmcgjrvcaoadtzm'

    # If its dark and the ISS is close above then send email
    if sun_down() and is_above():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='abrahamdeeb@gmail.com',
                msg=f'Subject:Look Up!\n\n The ISS is right above you! Do you see it?'
            )


# Function to check location of ISS relative to current location
def is_above():
    # API pulls current ISS location
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_distance = iss_latitude - MY_LAT
    lng_distance = iss_longitude - MY_LONG

    if -5 < lat_distance < 5 and -5 < lng_distance < 5:
        return True


# Function to check if it is dark outside based on user location
def sun_down():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # API to pull sunset and sunrise times
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # API data is given in UTC, pull UTC hour for comparison
    hour_now = dt.utcnow().hour

    # Check to see if its dark
    if sunset <= hour_now <= sunrise:
        return True


main()
