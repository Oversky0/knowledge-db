from ftplib import FTP

adress = 'ftp://192.168.0.1/' # много музыки в формате mp3
userdata = () # анонимный доступ
dirname = '.' # каталог, откуда загружаются файлы
filename = 'music.mp3'

connection = FTP(adress)
connection.login(userdata)
connection.cwd(dirname)

localfile = open(filename, 'wb') 
connection.retrbinary('RETR ' + filename, localfile.write, 1024) # RETR + filename - стандартный запрос загрузки файлов по FTP
connection.quit()
localfile.close()