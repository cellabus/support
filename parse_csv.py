import csv
import os
import sys

CSV_FILE = 'knowledgebase.csv'
PATH = 'app/articles/'

articles = []
with open(CSV_FILE, 'r') as handle:
    reader = csv.DictReader(handle)
    for row in reader:
        if row['Published'] == 'true':
            articles.append(row)

print(len(articles))

if not os.path.isdir(PATH):
    os.mkdir(PATH)

for article in articles:
    file_path = PATH + article['Updated At'].replace(' ', '-')
    print(file_path)
    data = article['Question'] + "\n"
    data += article['Updated At'] + "\n"
    data += article['Section'] + "\n"
    data += article['Answer Html']

    with open(file_path, 'w') as handle:
        handle.write(data)
