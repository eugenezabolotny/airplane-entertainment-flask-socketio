from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-secret-key'
socketio = SocketIO(app)

media = {
    'play safety message': {
        'name': 'play safety message',
        'path': 'http://192.168.52.10:81/api/src/movies/1/SampleVideo_1280x720_5mb.mp4',
        'duration': 29
    },
    'turn on entertainment': {
        'name': 'turn on entertainment',
        'path': 'http://192.168.52.10:81/api/src/movies/Atlantislaunch.mp4',
        'duration': 691
    },
}


@socketio.on('connect')
def test_connect():
    print('Connected!')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)

    if msg in media:
        emit('guest', media[msg]['path'], broadcast=True)
        emit('crew', media[msg], broadcast=True)

    if msg == 'stop':
        emit('guest', 'stop', broadcast=True)

    if msg == 'stream':
        pass


if __name__ == '__main__':
    socketio.run(app)
