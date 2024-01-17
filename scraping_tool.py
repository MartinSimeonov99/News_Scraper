import requests
from bs4 import BeautifulSoup
import re
from apscheduler.schedulers.background import BackgroundScheduler


def scrape_news():

    response = requests.get('https://www.artificialintelligence-news.com/')
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')

    new_articles = []
    existing_articles = []

    with open('ai.txt', 'r') as f:
        existing_articles = f.read().splitlines()

    for article in soup.find_all('article'):
        article_text = article.get_text()
        article_text = re.sub(r'\s+', ' ', article_text)

        if article_text not in existing_articles:
            new_articles.append(article_text)

    with open('ai.txt', 'w') as f:
        for article in new_articles:
            f.write(article)
            f.write('\n')


scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(scrape_news, 'cron', minute='*/5')

while True:
    pass
