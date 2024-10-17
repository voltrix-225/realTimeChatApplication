import socket
import threading

HOST = '127.0.0.1'
PORT = 8080

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Message from server {message}")
            else:
                break
           

        except:
            print("Disconnected from server")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        message = input()
        if message:
            client_socket.send(message.encode('utf-8'))


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"Connected to server at {HOST} : {PORT}")

thread = threading.Thread(target = receive_messages, args = (client_socket, ))
thread.start()

send_messages(client_socket)