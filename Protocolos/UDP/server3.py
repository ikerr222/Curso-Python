#!/usr/bin/env python3

#UDP
import socket

def start_udp_server():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"\nServidor UDP iniciado en {host}:{port}")

        while True:
            data, addr = s.recvfrom(1024)
            print(f"\nMensaje enviado por el cliente: {data.decode()}")
            print(f"Información del cliente que nos ha enviado el mensaje: {addr}")

start_udp_server()


