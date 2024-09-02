import requests
import bs4
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python']


def get_fake_headers():
    return Headers(browser='chrome', os='windows').generate()


response = requests.get('https://habr.com/ru/all/', headers=get_fake_headers())

soup = bs4.BeautifulSoup(response.text, features='lxml')
news_list = soup.findAll('article', class_='tm-articles-list__item')
for news in news_list:

    article_link = news.find('a', class_='tm-title__link')['href']
    response = requests.get(
        f'https://habr.com/{article_link}', headers=get_fake_headers())
    article = bs4.BeautifulSoup(response.text, features='lxml')
    title = article.find('h1').text
    headline = article.find('div', class_='tm-publication-hubs')
    headline = headline.find('span').text.rstrip('*')
    time = article.find('time')['title']
    post_preview_text= article.find('div', class_='article-formatted-body').text

    for search_word in KEYWORDS:
        if (search_word.lower() in headline.lower()):
            print(
                f'Дата: {time} - Заголовок: {title} - Ссылка: https://habr.com{article_link}-{headline}')
