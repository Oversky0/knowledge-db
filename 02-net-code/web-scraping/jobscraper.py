from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# keyword = re.compile(r"\b(бот)|\b(bot)|(скрипт)|(script)")
# telegram = re.compile(r"(телег)|(teleg)")
# webword = re.compile(r"(парс)|(pars)|(скрап)|(scrap)")
# pythonword = re.compile(r"\b(питон)|\b(python)")

regExp = re.compile(r"(?i)\b(бот)|\b(bot)|(скрипт)|(script)|(телег)|(teleg)|(парс)|(pars)|(скрап)|(scrap)|\b(питон)|\b(python)")

for i in range(1, 6):
    page = urlopen('https://www.fl.ru/projects/?page={}&kind=5'.format(i))
    soup = BeautifulSoup(page, 'html.parser')

    for head in soup.find('div', {'id': 'projects-list'}).find_all('h2'):
        if head.find(string=regExp):
            print(head.get_text(), end='')
            print('https://www.fl.ru' + head.a['href'])
            print('=' * 80)