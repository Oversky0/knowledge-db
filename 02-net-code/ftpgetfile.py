from ftplib import FTP

adress = '185.54.136.70'
userdata = () # анонимный доступ
dirname = '/users/yura' # каталог, откуда загружаются файлы
filename = 'readme!.txt'

connection = FTP(adress)
connection.login(userdata)
connection.cwd(dirname)

localfile = open(filename, 'wb') 
connection.retrbinary('RETR ' + filename, localfile.write, 1024) # RETR + filename - стандартный запрос загрузки файлов по FTP
connection.quit()
localfile.close()