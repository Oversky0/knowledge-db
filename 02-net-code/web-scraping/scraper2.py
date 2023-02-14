from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    page = urlopen('https://www.pythonscraping.com/pages/page3.html')

    soup = BeautifulSoup(page, 'html.parser')
    for child in soup.find('table', {'id': 'giftList'}).children: # найти первый тег table с атрибутом id:giftList и получить все его дочерние теги (не потомки!)
        print(child)
    
    # for child in soup.find('table', {'id': 'giftList'}).desndants: # найти первый тег table с атрибутом id:giftList и получить всех его потомков
    #    print(child)
    
    print('=' * 80)

    for sibling in soup.find('table', {'id': 'giftList'}).tr.next_siblings: # получить список тегов, расположенных на одном уровне, вложенных в тег table
        print(sibling)
    
    print('=' * 80)

    score = soup.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
    print(score)


except HTTPError as e:
    print('HTTP error: ', e)

except URLError as e:
    print('URL error: ', e)