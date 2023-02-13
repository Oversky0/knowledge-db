""" 
===================================================================================
Запрашивает файл y сервера через сокет 
===================================================================================
"""

import os 
import time
from socket import *

serverhost = 'localhost'
serverport = 50001

def now():
    return time.asctime()

class Client():
    def __init__(self, host, port):
        self.serverhost = host
        self.serverport = port
        self.serversock = socket(AF_INET, SOCK_STREAM)
    
    def connect(self):
        self.serversock.connect((self.serverhost, self.serverport))

    def get_file(self, filename):
        self.serversock.send((filename + '\n').encode())
        dropdir = os.path.split(filename)[1]
        file = open(dropdir, 'wb')
        while True:
            data = self.serversock.recv(1024)
            if not data: break
            file.write(data)
        self.serversock.close()
        file.close()
        print('Client got', filename, 'at', now())


if __name__ == '__main__':
    client = Client(serverhost, serverport)
    client.connect()
    client.get_file("data\\textfile.txt")

