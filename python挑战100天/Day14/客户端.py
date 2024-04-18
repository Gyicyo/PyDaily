from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
from threading import Thread

username = '用户  '
def main():
    client = socket()
    client.connect(('10.130.65.214', 6789))
    print('连接到了服务器.')
    # 5.发送数据
    client.send('已建立连接'.encode('utf-8'))
    send = Thread(target=send_message,args=(client,))
    get = Thread(target=get_message, args=(client,))
    send.start()
    get.start()

def send_message(client):
    while True:
        message = input('请输入要发送的信息：')
        if message == 'exit':
            client.send('对方断开了连接'.encode('utf-8'))
            client.close()
        client.send(message.encode('utf-8'))

def get_message(client):
    while True:
        message = client.recv(1024).decode('utf-8')
        print(f'收到信息：{message}')

if __name__ == '__main__':
    main()