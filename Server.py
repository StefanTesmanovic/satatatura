import socket
import threading
import time
from pynput.keyboard import Key, Controller

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #Server = "192.168.0.16"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISSCONNECT"
keyboard = Controller()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(tip adrese i povezivanja ipv4/6 bluetooth, sta radi)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"NEW connection {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"{addr}:{msg}")
            time.sleep(5)
            for i in  msg:
                keyboard.press(i)
                time.sleep(0.5)
                keyboard.release(i)
    conn.close()

def start():
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections {threading.activeCount() -1 }")

print("Server is starting...")
start()

















