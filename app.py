from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, async_mode = 'eventlet')

#main chat app page
@app.route('/')

def index():
    return render_template('index.html')

#handle client messages

@socketio.on('message')

def handle_message(msg):
    print(f"Message : {msg}")

    send(msg, broadcast = True)


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
