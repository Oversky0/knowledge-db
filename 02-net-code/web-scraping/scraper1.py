from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    page = urlopen('https://pythonscraping.com/pages/warandpeace.html')

    soup = BeautifulSoup(page, 'html.parser')
    name_list = soup.find_all('span', {'class': 'green'}) # name_list - список тегов span с атрибутом class=green
    # name_list = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) # получить все указанные теги из списка
    # name_list = soup.find_all('span', {'class': {'green', 'red'}}) # получить все теги span с атрибутом class=green или red
    # name_lost = soup.find_all(id = 'title', class_='text') # получить все теги с атрибутами id=title и class=text
    for name in name_list:
        print(name.get_text()) #get_text - получить содержимое тега

except HTTPError as e:
    print('HTTP error: ', e)
except URLError as e:
    print('URL error: ', e)