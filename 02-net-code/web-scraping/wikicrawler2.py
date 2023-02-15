from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    for link in soup.find('div', {'id': 'bodyContent'}).find_all('a', {'href': re.compile('^(/wiki/)')}):
        if link['href'] not in pages:
            newurl = link['href']
            print(newurl)
            pages.add(newurl)
            getLinks('http://en.wikipedia.org{}'.format(newurl))

getLinks('http://en.wikipedia.org')