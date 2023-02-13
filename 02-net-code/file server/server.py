""" 
===================================================================================
Реализует логику передачи произвольного файла клиенту через сокет 
===================================================================================
"""

import sys
import time
import _thread as thread
from socket import *

def now():
    return time.asctime()

def command_line():
    if len(sys.argv) == 3:
        defaultHost = sys.argv[1]
        defaultPort = sys.argv[2]

class HandlerClient():
    def handler_client(self, clientsock):
        filesock = clientsock.makefile('r')
        filename = filesock.readline()[:-1]
        
        try:
            file = open(filename, 'rb')
            while True:
                bytes = file.read(1024)
                if not bytes: break
                sent = clientsock.send(bytes)
                assert sent == len(bytes)
        except:
            print("Error download file on server: ", filename)
        
        clientsock.close()

class ThreadServer(HandlerClient):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket(AF_INET, SOCK_STREAM)
    
    def setup(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
    
    def start(self):
        while True:
            clientsock, clientaddr = self.sock.accept()
            print('Server connected by ', clientaddr, 'at', now())
            thread.start_new_thread(self.handler_client, (clientsock, ))
    
    def stop(self):
        self.sock.close()

if __name__ == '__main__':
    
    defaultHost = ''
    defaultPort = 50001
    
    command_line()
    
    server = ThreadServer(defaultHost, defaultPort)
    server.setup()
    server.start()
