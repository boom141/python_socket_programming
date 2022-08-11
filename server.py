import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

client_list = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def Client_Chat(conn, addr):
    while True:
        msg = conn.recv(512).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            break
        else:
            for client in client_list:
                if client == conn:
                    pass
                else:
                    client.send(f'{addr}:{msg}'.encode(FORMAT))
    
    print(f'[DISCONNECTED] client: {addr} is disconnected!')
    client_list.remove(conn)
    conn.close()
    print(f'[ACTIVE CONNECTIONS] {len(client_list)}')

def Handle_Client_Connection(conn, addr):
    print(f'[NEW CONNECTION] {addr} is connected')

def Start_Server():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')

    while True:
        conn, addr = server.accept()
        client_list.append(conn)
        thread1 = threading.Thread(target=Handle_Client_Connection, args=(conn, addr))
        thread2 = threading.Thread(target=Client_Chat, args=(conn, addr))
        thread1.start()
        thread2.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount()-1}')


        
print('[STARTING SERVER] Server is starting....')
Start_Server()