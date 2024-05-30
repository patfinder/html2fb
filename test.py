import codecs
from bs4 import BeautifulSoup

with codecs.open('./data/giao-tiep.html', mode='r', encoding="utf-8") as file1:
    html_doc = file1.read()

soup = BeautifulSoup(html_doc, 'html.parser')

print(f'P Node: {soup.div}')
