import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.10"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

message = None

def Client_Response():
    while True:
        if message == DISCONNECT_MESSAGE:
            break
        
        res = client.recv(512).decode(FORMAT)
        print(res)
        

def Client_Chat():
    global message
    input('Enter Chat Name: ')
    while True:
        message = input()
        client.send(message.encode(FORMAT))
        if message == DISCONNECT_MESSAGE:
            break

thread1 = threading.Thread(target=Client_Chat)
thread2 = threading.Thread(target=Client_Response)

thread1.start()
thread2.start()

thread1.join()
thread2.join()