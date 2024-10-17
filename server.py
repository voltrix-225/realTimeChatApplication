from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

clients = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    clients.append(request.sid)  # Keep track of connected clients

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")
    clients.remove(request.sid)  # Remove client from the list

@socketio.on('message')
def handle_message(msg):
    print(f"Message received: {msg}")
    # Broadcast message to all clients
    socketio.emit('message', msg)

@socketio.on('connect')
def handle_connect():
    update = "A client connected."
    socketio.emit(update)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
