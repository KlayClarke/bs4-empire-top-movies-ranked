import requests
from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
empire_web_content = response.text

soup = BeautifulSoup(empire_web_content, 'html.parser')
