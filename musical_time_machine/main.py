import requests
from bs4 import BeautifulSoup

era = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

url = f'https://www.billboard.com/charts/hot-100/{era}'

soup = BeautifulSoup(url, 'html.parser')

songs_tag = soup.find_all(name='h3')

song_list = [song.get_text() for song in songs_tag]

print(song_list)