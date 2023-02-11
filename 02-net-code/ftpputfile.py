'''
Выгружает произвольный файл по FTP в двоичном режиме. 
Использует анонимный доступ к ftp, если функции не был передан 
кортеж user=(имя, пароль) аргументов.
'''

from ftplib import FTP

def ftp_put_file(file, address, dirname, user=()):
    localfile = open(file, 'rb')
    try:
        connection = FTP(address)
        connection.login(*user)
        connection.cwd(dirname)
        connection.storbinary("STOR " + file, localfile, 1024)
        connection.quit()
    finally:
        localfile.close()

if __name__ == '__main__':
      
    address = '185.54.136.70'
    dirname = '/users/evgen'
    filename = 'readme.txt'
    userinfo = ('evgen', 'qwerty')

    ftp_put_file(filename, address, dirname)