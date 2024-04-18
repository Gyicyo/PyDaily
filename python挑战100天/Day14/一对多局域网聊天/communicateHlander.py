import socket
from threading import Thread
from base64 import b64encode, b64decode

class Hlander:
    __slots__ = ['client_list']
    def __init__(self):
        self.client_list = []

    def get_all_clients(self):
        return self.client_list

    def new_client(self, client: socket):
        self.client_list.append(client)
        thread = Thread(target=self.recv_message, args=(client,len(self.get_all_clients())))
        message = f'成功建立连接,你是{len(self.get_all_clients())}号用户'
        client.send(message.encode('utf-8'))
        thread.start()

    def send_message(self,client_index:int,message:str):
        client = self.client_list[client_index]
        client.send(message.encode('utf-8'))

    def recv_message(self,client: socket,index:int):
        while True:
            data = client.recv(1024)
            print(f'收到来自用户{index}的消息:{data.decode('utf-8')}')
