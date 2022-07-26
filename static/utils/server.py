import socket, threading, time

TIMEFORMAT = '%Y-%m-%d, %H:%M:%S'

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
        self.flag = False


    def broadcast(self,username, msg):
        print(self.clients)
        msg = '{}: {} - {}'.format(username, msg, time.strftime(TIMEFORMAT))
        print(msg)

        for _, client in self.clients.items():
            c_sock = client[0]
            c_sock.send(msg.encode('utf-8'))


    def listen(self, c_sock, addr):
        c_sock.send('请输入昵称:'.encode('utf-8'))
        username = c_sock.recv(1024).decode('utf-8')

        self.clients[username] = [c_sock, addr]
        self.broadcast(username, '已加入.')
        c_sock.send('Connected.'.encode('utf-8'))
        while True:
            try:
                conn = self.clients[username][0]
                message = conn.recv(1024).decode('utf-8')
                if len(message) == 0:
                    break
                self.broadcast(username, message)
            except:
                self.clients[username][0].close()
                self.clients.pop(username)
                self.broadcast(username, '已离开.')

    def handle_conn(self):
        while True:
            c_sock, addr = self.s_sock.accept()
            print("Connected with {}".format(addr))

            t = threading.Thread(target=self.listen, args=(c_sock, addr, ))
            t.start()

