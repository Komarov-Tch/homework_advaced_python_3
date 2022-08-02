import requests as req
from bs4 import BeautifulSoup as bs
from pprint import pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com/ru/all/'
resp = req.get(url, headers={'User-Agent': 'Chrome'})
soup = bs(resp.text, 'html.parser')
result_review = soup.find_all('article', {'data-test-id': "articles-list-item"})
result_head = soup.find_all('a', {'class': 'tm-article-snippet__title-link'})
result_date = soup.find_all('span', {'class': 'tm-article-snippet__datetime-published'})
for i in result_review:
    head = i.find('a', {'class': 'tm-article-snippet__title-link'})
    title = head.text
    link = 'https://habr.com' + head.get('href')
    text = i.find('div',
                  {'class': "article-formatted-body article-formatted-body article-formatted-body_version-2"}).text
    date = i.find('span', {'class': 'tm-article-snippet__datetime-published'}).find('time').get('datetime')[:10]

    print(text)
