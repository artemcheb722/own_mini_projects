import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(5)

print("The server is running and waiting for a connection...")

while True:
    try:
        client, addr = s.accept()
        print("Connected:", addr)

        while True:
            data = client.recv(1024)
            if not data:
                break

            print("Message:", data.decode('utf-8'))

        client.close()

    except KeyboardInterrupt:
        print("\nServer stopped")
        s.close()
        break