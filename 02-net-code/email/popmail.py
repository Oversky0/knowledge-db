import poplib
import mailconfig

popserver = 'pop.yandex.ru'
popuser = 'evgen.in.it'
passwd = ''

print('Connection...')
server = poplib.POP3_SSL(popserver)
server.user(popuser)
server.pass_(passwd)

try:
    print(server.getwelcome())
    msgCount, msgBytes = server.stat()
    print('There are', msgCount, 'mail messages in', msgBytes, 'bytes')
    print(server.list())
    print('-' * 80)
    input('[Press enter key]')

    for i in range(msgCount):
        hdr, message, octets = server.retr(i+1)
        for line in message:
            print(line.decode())
        print('-' * 80)
        if i < msgCount - 1:
            input('[Press Enter key]')
finally:
    server.quit()