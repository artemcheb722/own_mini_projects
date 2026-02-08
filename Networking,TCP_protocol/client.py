import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
while True:

    m = input("Enter your message: ")
    s.send(m.encode('utf-8'))

s.close()
