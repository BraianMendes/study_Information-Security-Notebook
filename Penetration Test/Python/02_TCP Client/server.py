#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostName = socket.gethostname()
host = socket.gethostbyname(hostName)
port = 444

#Binding to socket
serversocket.bind((host, port))

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket, address = serversocket.accept()

    print("received connection from %s" % str(address[0]))

    message = 'Hello! Thank you for connecting to the server.' + "\r\n"
    clientsocket.sendall(message.encode('ascii'))

    clientsocket.close()