import requests
from bs4 import BeautifulSoup

def get_html():
    html_page = requests.get('https://ria.ru/').text
    return html_page

soup = BeautifulSoup(get_html(), 'lxml')

def get_important():
    important_to_voice = {}
    important = soup.find('div', attrs={'data-block-position':'3'}).find_all('a')
    for news in important:
        news_html_page = requests.get(news['href']).text
        important_soup = BeautifulSoup(news_html_page, 'lxml')
        header = important_soup.find('div', class_='article__title').text
        text = ' '.join([p.text for p in list(important_soup.find_all('div', class_='article__text', limit=4))]).split('. ', 1)[-1]
        important_to_voice[header] = text
    return important_to_voice

def get_popular():
    popular_to_voice = {}
    popular = soup.find('div', attrs={'data-block-position':'4'}).find_all('a')
    for news in popular:
        news_html_page = requests.get(news['href']).text
        important_soup = BeautifulSoup(news_html_page, 'lxml')
        header = important_soup.find('div', class_='article__title').text
        text = ' '.join([p.text for p in list(important_soup.find_all('div', class_='article__text', limit=4))]).split('. ', 1)[-1]
        popular_to_voice[header] = text
    return popular_to_voice