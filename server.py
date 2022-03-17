import socket
import threading

host, port = ('127.0.0.1', 8777)

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.bind((host, port))
Socket.listen()

roomMembers = {}


def toAll(msg, sender):
    for member in roomMembers.keys():
        if member == sender:
            continue
        member.send(msg.encode('utf-8'))


def recieve(sender):
    while True:
        msg = sender.recv(1024).decode('utf-8')
        if msg == '':
            toAll(f"{roomMembers[sender]} has left the Chatroom", sender)
            roomMembers.pop(sender)
            break

        toAll(msg, sender)


if __name__ == '__main__':
    while True:
        print("Server is running...")
        
        conn, addr = Socket.accept()
        print(f"Connected by {addr}")

        roomMembers[conn] = conn.recv(1024).decode('utf-8')
        conn.send("You are connected..".encode('utf-8'))
        toAll(f"{roomMembers[conn]} HAS JOINED", conn)

        client = threading.Thread(target=recieve, args=(conn,))
        client.start()
