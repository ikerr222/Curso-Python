#!/usr/bin/env python3

#TCP
import socket
import threading #Hilos
import pdb # Debugging

class ClientThread(threading.Thread): #Hereda de la clase Thread para implementarla a mi gusto
    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

        print(f"\nNuevo cliente conectado: {client_addr}")

    def run(self):

        message = ''

        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()

            if message.strip() == 'bye': #hay que quitar el salto de linea -> strip
                break

            print(f"\nMensaje enviado por el cliente: {message.strip()}")
            self.client_sock.send(data)

        print(f"\nCliente {self.client_addr} desconectado")
        self.client_sock.close()

HOST = 'localhost'
PORT = 1234


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TIME_WAIT, socket.IPPROTO...
    server_socket.bind((HOST, PORT))

    print(f"\nEn espera de conexiones entrantes...")

    while True:

        server_socket.listen() #Python lo hace automáticamente
        client_sock, client_addr = server_socket.accept()
        new_thread = ClientThread(client_sock, client_addr)
        new_thread.start() #run()





