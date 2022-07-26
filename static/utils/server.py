import socket, threading, time
from static.utils.log_io import *

TIMEFORMAT = '%Y-%m-%d, %H:%M:%S'
LOG_PATH = 'static/data/server_log.json'

class Server:
    def __init__(self, host = '127.0.0.1', port = 9999):
        self.host = host
        self.port = port
        self.addr = (host, port)
        s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_sock.bind(self.addr)
        s_sock.listen()
        self.s_sock = s_sock
        self.clients = {}       # {username: [c_sock, addr]}


    def broadcast(self, username, msg):
        msg = '{}: {} - {}'.format(username, msg, time.strftime(TIMEFORMAT))
        print(msg)
        write('log', username, msg)

        for _, client in self.clients.items():
            c_sock = client[0]
            c_sock.send(msg.encode('utf-8'))


    def listen(self, c_sock, addr):

        username = c_sock.recv(1024).decode('utf-8')

        self.clients[username] = [c_sock, addr]
        self.broadcast(username, '已加入.')

        # c_sock.send('Connected.'.encode('utf-8'))
        while True:
            try:
                conn = self.clients[username][0]
                message = conn.recv(1024).decode('utf-8')
                if len(message) == 0:
                    break
                if message == 'exit':
                    self.destroy(username)
                self.broadcast(username, message)
            except:
                self.destroy(username)

    def handle_conn(self):
        while True:
            c_sock, addr = self.s_sock.accept()
            print("Connected with {}".format(addr))

            t = threading.Thread(target=self.listen, args=(c_sock, addr, ))
            t.start()

    def destroy(self,username):
        self.clients[username][0].close()
        self.clients.pop(username)
        self.broadcast(username, '已离开.')