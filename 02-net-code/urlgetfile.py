'''
Сценарий на языке Python для загрузки файла по строке адреса URL; 
urllib поддерживает протоколы FTP, HTTP, HTTPS на стороне клиента, 
локальные файлы, может работать с прокси­серверами, выполнять инструкции 
перенаправления, принимать cookies и многое другое; urllib также 
позволяет загружать страницы html, изображения, текст и так далее; 
смотрите также парсеры Python разметки html/xml веб­страниц, 
получаемых с помощью urllib
'''

from urllib.request import urlopen

address = 'https://www.ejin.ru/wp-content/uploads/2020/03/22-7.jpg'
filename = 'cat.jpg'

remotefile = urlopen(address)
localfile = open(filename, 'wb')
localfile.write(remotefile.read())
localfile.close()
remotefile.close()
