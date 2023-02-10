"""
Загружает произвольный файл по FTP. Используется анонимный доступ к FTP, 
если не указан кортеж user=(имя, пароль).
"""

from ftplib import FTP
from os.path import exists

def ftp_get_file(file, address, dirname, user=()):
    if exists(file): 
        print(file, 'exists')
    else:
        localfile = open(file, 'wb')
        try:
            connection = FTP(address)
            connection.login(*user)
            connection.cwd(dirname)
            connection.retrbinary('RETR ' + file, localfile.write, 1024) # RETR + filename - стандартный запрос загрузки файлов по FTP
            connection.quit()
        finally:
            localfile.close()

if __name__ == '__main__':

    address = '185.54.136.70'
    dirname = '/users/yura' # каталог, откуда загружаются файлы
    filename = 'readme!.txt' # загружаемый файл

    ftp_get_file(filename, address, dirname)