import socket

server = socket.socket()
server.bind(("localhost", 12345))
server.listen(1)

print("Server is waiting...")

conn, addr = server.accept()
print("Connected by:", addr)

conn.send("Hello! Welcome to my TCP Server.".encode())

conn.close()
server.close()