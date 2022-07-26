import threading
from client import Client

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9999
    c = Client()
    c.c_sock.connect((host, port))

    tr = threading.Thread(target=c.recv)
    tr.start()
    ts = threading.Thread(target=c.send)
    ts.start()
