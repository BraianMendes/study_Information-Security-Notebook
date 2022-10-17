#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostName = "google.com"
host = socket.gethostbyname(hostName)
port = 444

serversocket.bind(("127.0.0.1", port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print("received connection from " + str(address[0]))

    message = b'Hello! Thank you for connecting to the server.'
    clientsocket.sendall(message)

    clientsocket.close()