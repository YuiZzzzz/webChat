from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import eventlet

eventlet.monkey_patch()

app = Flask('ChatRoom', static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'abcdefg'
socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('服务器收到信息:{}'.format(msg))

@socketio.event
def join_room(room_number):
    print('房间号:{}'.format(room_number))
    join_room(room_number['room'])

    emit('joined',{
        'user':request.sid,
        'room':room_number['room']
    }, to=room_number['room'])



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    socketio.run(app)