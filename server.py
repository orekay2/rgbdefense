import socket
import sys
import time


#made mostly with copilot to make things quick
print(socket.gethostbyname(socket.gethostname()))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 80)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen()


while True:
    connection, client_address = sock.accept()
    print('connection from', client_address)
    data = connection.recv(1024)
    print('received "%s"' % data)
    connection.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
    connection.sendall(b'<html><body><h1>test successful</h1></body></html>')
    connection.close()
    time.sleep(1)