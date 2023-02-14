'''
Загружает HTML страницу по указанному URL адресу.
'''
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup

try:
    page = urlopen('https://pythonscraping.com/pages/page1.html') # page - экземпляр класса HTTPResponse, поддерживает интерфейс файла
    # print(page.read())
    
    soup = BeautifulSoup(page, 'html.parser') # html.parser - встроенный анализатор
    print(soup.h1) # ищет первое вхождение тега h1
    # print(soup.html.body.h1)
    # print(soup.body.h1)
    # print(soup.html.h1)

except HTTPError as e: # HTTPError возникает если сервер не может найти указанную страницу
    print('HTTP Error!')

except URLError as e:  # URLError возникает если не найден весь сервер
    print('URL Error!')