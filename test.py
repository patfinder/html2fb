import codecs
from bs4 import BeautifulSoup


class Formetter():
    def __init__(self) -> None:
        # b, i, bi: bold, itatic, bold and itatic
        # o, u: ordered, unordered list
        self.type = None


def main():
    with codecs.open('./data/giao-tiep.html', mode='r', encoding="utf-8") as file1:
        html_doc = file1.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    print(f'P Node: {soup.div}')


# run main
main()