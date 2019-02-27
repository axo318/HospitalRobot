#!/usr/bin/env python3

import socket
import sys

command = sys.argv[1]

host = '192.168.105.102'
port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))
sock.sendall(command.encode())
sock.close()
