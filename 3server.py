import socket

server = socket.socket()
server.bind(("localhost", 12345))
server.listen(1)

print("Server is waiting...")

conn, addr = server.accept()

name = conn.recv(1024).decode()

message = "Hello " + name + "! Welcome to the server."
conn.send(message.encode())

conn.close()
server.close()