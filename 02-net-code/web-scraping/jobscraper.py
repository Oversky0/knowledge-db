from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

# keyword = re.compile(r"\b(бот)|\b(bot)|(скрипт)|(script)")
# telegram = re.compile(r"(телег)|(teleg)")
# webword = re.compile(r"(парс)|(pars)|(скрап)|(scrap)")
# pythonword = re.compile(r"\b(питон)|\b(python)")

class WorkParser:
    
    def __init__(self, pages):
        self.pages = pages
        self.url = 'https://www.fl.ru/projects/?page={}&kind=5'
        self.keyword = re.compile(r"(?i)\b(бот)|\b(bot)|(скрипт)|(script)|(телег)|(teleg)|(парс)|(pars)|(скрап)|(scrap)|\b(питон)|\b(python)")
    
    def parse(self):
        for i in range(1, self.pages + 1):
            try:
                page = urlopen(self.url.format(i))
            except HTTPError as err:
                print('HTTP error: ', err)
            except URLError as err:
                print('URL error:', err)

            soup = BeautifulSoup(page, 'html.parser')
            
            for head in soup.find('div', {'id': 'projects-list'}).find_all('h2'):
                if head.find(string=self.keyword):
                    print(head.get_text(), end='')
                    print('https://www.fl.ru' + head.a['href'])
                    print('=' * 80)

if __name__ == '__main__':
    work = WorkParser(5)
    work.parse()