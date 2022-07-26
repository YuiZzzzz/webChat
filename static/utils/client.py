import socket, threading
import time


class Client:
    def __init__(self):
        self.c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.addr = self.c_sock.getsockname()
        self.ip = self.addr[0]
        self.port = self.addr[1]
        self.username = ''
        self.count = 0

    def recv(self, mtu=1024):
        while True:
            msg = self.c_sock.recv(mtu).decode('utf-8')
            if len(msg) == 0:
                continue
            print(msg)
            if msg == '请输入昵称:':
                msg = input()
                self.c_sock.send(msg.encode('utf-8'))
                self.username = msg
            print(self.username)
            self.count += 1
            print('recv:{}'.format(self.count))


    def send(self):

        while True:

            time.sleep(1)
            msg = input()
            if len(msg) == 0:
                continue
            print(msg)
            self.c_sock.send(msg.encode('utf-8'))
            self.count += 1
            print('send:{}'.format(self.count))



