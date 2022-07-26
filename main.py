import csv
import json
import threading
import time

from flask import Flask, render_template, request, redirect, url_for, session
from static.utils.log_io import *
from static.utils.client import Client



app = Flask(__name__)
app.secret_key = '!@#$%^&*()11'

TIMEFORMAT = '%Y-%m-%d %H:%M:%S'
LOG_PATH = 'static/data/server_log.json'
CHAT_PATH = 'static/data/chat.json'

host = '127.0.0.1'
port = 9999


global client
client = Client()
client.c_sock.connect((host, port))


@app.route('/', methods=['GET','POST'])
def index():
    global client

    if request.method == 'GET':

        if 'username' in session:
            tr = threading.Thread(target=client.recv)
            tr.start()
            data = read('chat')
            return render_template('index.html', data=data)
        else:
            return render_template('index.html', data=[])


    if request.method == 'POST':
        print(session)

        if 'username' in session:
            if client:
                msg = request.form['msg']
                write('chat', session.get('username'), msg)
                client.send(msg)

                return redirect(url_for('index'))


        else:
            username = request.form['username']
            session['username'] = username



            # 创建一个client

            client.send(username)


            return redirect(url_for('index'))


@app.route('/logout', methods=['GET','POST'])
def logout():
    session.pop('username')
    return redirect(url_for('index'))





if __name__ == '__main__':
    app.run()
