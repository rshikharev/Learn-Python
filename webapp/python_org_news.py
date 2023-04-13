import requests
from bs4 import BeautifulSoup
from datetime import datetime

from webapp.db import db
from webapp.news.models import News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Connection error')
        return False

def get_python_news():
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                repl = {
                    'Jan. ': '01-',
                    'Feb. ': '02-',
                    'Mar. ': '03',
                    'Apr. ': '04-',
                    'May ': '05-',
                    'Jun. ': '06-',
                    'Jul. ': '07-',
                    'Aug. ': '08-',
                    'Sep. ': '09-',
                    'Oct. ': '10-',
                    'Nov. ': '11-',
                    'Dec. ': '12-',
                    ', ': '-',
                }
                for i, j in repl.iteritems():
                    published = published.replace(i, j)
                published = datetime.strftime(published, format="%m-%-d-%Y")
            except:
                published = datetime.now()
            save_news(title, url, published)
    
def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()