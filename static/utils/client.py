import socket, threading
import time
from static.utils.log_io import *

LOG_PATH = 'static/data/server_log.json'
CHAT_PATH = 'static/data/chat.json'

class Client:
    def __init__(self):
        self.c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = self.c_sock.getsockname()
        self.ip = self.addr[0]
        self.port = self.addr[1]
        self.username = ''
        self.count = 0
        self.firstSend = False


    def recv(self, mtu=1024):
        while True:
            msg = self.c_sock.recv(mtu).decode('utf-8')
            if len(msg) == 0:
                continue
            self.count += 1
            # write('chat', self.username, msg)
            print('recv{}: {}'.format(self.count, msg))


    def send(self, msg):
        if not self.firstSend:
            self.c_sock.send(msg.encode('utf-8'))
            self.username = msg
            self.firstSend = True

        else:
            time.sleep(1)
            if msg != self.username:
                self.c_sock.send(msg.encode('utf-8'))
                self.count += 1
                print('send{}: {}'.format(self.count, msg))



    def close(self):
        self.c_sock.send('exit'.encode('utf-8'))
        return