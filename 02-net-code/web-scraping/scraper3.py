from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

page = urlopen('https://www.pythonscraping.com/pages/page3.html')

soup = BeautifulSoup(page, 'html.parser')

for image in soup.find_all('img', {'src': re.compile('..\/img/gifts\/img[0-9].jpg')}): # использование регулярных выражений 
    # print(image.attrs) # список атрибутов тега 
    print(image['src']) # обращение к значению атрибута по ключу

print('=' * 80)

print(soup.find_all(lambda tag: len(tag.attrs) == 2)) # найти все теги с двумя атрибутами
