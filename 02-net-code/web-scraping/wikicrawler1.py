from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLink(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    return soup.find('div', {'id': 'bodyContent'}).find_all('a', {'href': re.compile('^(/wiki/)((?!:).)*$')}) # найти все ссылки на другие статьи в wiki

links = getLink('https://en.wikipedia.org/wiki/Kevin_Bacon') # отправная точка

while len(links) > 0:
    urlpage = 'https://en.wikipedia.org' + links[random.randint(0, len(links)-1)].attrs['href']
    print(urlpage)
    links = getLink(urlpage)
