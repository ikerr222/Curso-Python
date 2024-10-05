#!/usr/bin/env python3

#UDP
import socket

def start_udp_client():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"Hola servidor", (host, port))

start_udp_client()
