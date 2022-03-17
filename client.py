import socket
import threading

host, port = ("127.0.0.1", 8777)
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.connect((host, port))


name = input("Enter your name: ")
Socket.send(name.encode('utf-8'))


def receive():
    while True:
        new_msg = Socket.recv(1024)
        print(new_msg.decode('utf-8'))

def send_msgs():
    while True:
        msg = f"{name}: {input()}"
        Socket.send(msg.encode('utf-8'))
        if msg == '':
            break

receiver = threading.Thread(target=receive)
receiver.start()
sender = threading.Thread(target=send_msgs)
sender.start()
