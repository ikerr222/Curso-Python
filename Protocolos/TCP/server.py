#!/usr/bin/env python3

#TCP
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1234)
server_socket.bind(server_address)

#Limite de conexiones=1
server_socket.listen(1)

while True:

    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024)

    print(f"\nMensaje recibido del cliente: {data.decode()}")
    print(f"Información del cliente que se ha comunicado con nosotros: {client_address}")

    client_socket.sendall(f"Un saludo crack\n".encode())
    client_socket.close()

