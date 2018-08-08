from flask import Flask
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-secret-key'
socketio = SocketIO(app)


@socketio.on('connect')
def test_connect():
    print('Connected!')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    # send(msg, broadcast=True)
    emit('play', 'http://192.168.52.10:81/api/src/movies/1/SampleVideo_1280x720_5mb.mp4', broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
