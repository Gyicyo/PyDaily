import socket
from communicateHlander import Hlander
from threading import Thread
import time

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 6827))
    s.listen(512)
    print('Waiting for connection...')
    hlander = Hlander()
    messageHlander = Thread(target=send_message,args=(hlander,))
    messageHlander.start()
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        hlander.new_client(conn)

def send_message(hlander):
    while True:
        client_list = hlander.get_all_clients()
        if len(client_list) == 0:
            time.sleep(1)
            continue
        for i in range(len(client_list)):
            print(f"Client {i}")

        while True:
            try:
                client_index = int(input("Enter the client index: "))
                break
            except ValueError:
                print('输入错误,重新输入:')

        message = input("Enter the message: ")
        hlander.send_message(client_index, message)
        time.sleep(1)

start_server()
