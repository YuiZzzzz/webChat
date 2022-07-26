import csv
import json

from flask import Flask, render_template, request, redirect, url_for




app = Flask(__name__)
app.secret_key = '!@#$%^&*()11'
socketio = SocketIO(app)



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':

        with open('static/data/chat.json', 'r') as f:
            data = json.load(f)
        return render_template('index.html', data=data)

    if request.method == 'POST':
        msg = request.form['msg']
        msg = {'msg':msg}

        with open('static/data/chat.json', 'r') as f:
            data = json.load(f)
        data.append(msg)
        with open('static/data/chat.json', 'w') as f:
            json.dump(data, f)

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
    socketio.run(app)