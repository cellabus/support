from bs4 import BeautifulSoup
import csv
import os
import re
import requests
import shutil
import sys

CSV_FILE = 'knowledgebase.csv'
ARTICLES_PATH = 'app/articles/'
IMG_PATH = 'app/static/articles/'
PUBLIC_IMG_PATH = '/static/articles/'


def get_articles():
    articles = []
    with open(CSV_FILE, 'r') as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row['Published'] == 'true':
                articles.append(row)
    print(len(articles))
    return articles


def create_directory(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir(path)


def slugify(string):
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.replace(' ', '-')
    string = string.lower()
    return string


def save_articles(articles):
    for article in articles:
        file_path = ARTICLES_PATH + article['Updated At'].replace(' ', '-')
        print(file_path)
        data = article['Question'] + "\n"
        data += slugify(article['Question']) + "\n"
        data += article['Updated At'] + "\n"
        data += article['Section'] + "\n"
        answer = parse_html(article['Answer Html'])
        data += answer

        with open(file_path, 'w') as handle:
            handle.write(data)
        print("")


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.findAll('img'):
        src = img.get('src')
        newsrc = download_src(src)
        html = html.replace(src, newsrc)
        print(newsrc)
    return html

def download_src(src):
    remote_path = src
    if remote_path[0] == '/':
        remote_path = 'http://support.cellabus.com' + remote_path
    img = requests.get(remote_path)
    if img.status_code != 200:
        return src
    src_name = img.url.split('/')[-1]
    src_name = src_name.split('?')[0]
    if src_name[-4] != '.':
        src_name = src_name + '.png'
    local_path = IMG_PATH + src_name
    with open(local_path, 'wb') as handle:
        handle.write(img.content)
    local_public_path = PUBLIC_IMG_PATH + src_name
    return local_public_path


if __name__ == "__main__":
    articles = get_articles()
    create_directory(ARTICLES_PATH)
    create_directory(IMG_PATH)
    save_articles(articles)
