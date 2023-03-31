from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, 'html.parser')

movie_title_tag = soup.find_all(name='h3', class_='title')

title_list = list(reversed([movie.get_text() for movie in movie_title_tag]))

with open('top_100_movies.txt', 'w') as file:
    file.writelines([title + '\n' for title in title_list])



