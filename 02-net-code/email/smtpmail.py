'''
Использует модуль Python почтового интерфейса SMTP для отправки сообщений;
'''

import sys
import smtplib
import email.utils

smtpserver = 'smtp.yandex.ru'
From = 'evgen.in.it@yandex.ru'
To = 'evgen.in.it@yandex.ru'
Tos = ';'
Subj = 'A B C D E F G'
Date = email.utils.formatdate()

text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To, Tos, Subj))
text += 'Hello world!'

print('Connecting...')
connection = smtplib.SMTP_SSL(smtpserver)
connection.connect(smtpserver, 465)
connection.login('evgen.in.it', '')

failed = connection.send_message(text)
connection.quit()
if failed:
    print('Error', failed)
else:
    print('No errors')
print('-' * 80)