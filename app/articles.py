import os

root_path = os.path.dirname(os.path.realpath(__file__)) + '/../'


class Article():
    def __init__(self, article_file):
        self.article_file = article_file
        self.question = ''
        self.updated = ''
        self.section = ''
        self.answer = ''


def parse_articles():
    article_path = os.path.join(root_path, 'app', 'articles')
    article_files = os.listdir(article_path)
    articles = []
    for article_file in article_files:
        article = Article(article_file)
