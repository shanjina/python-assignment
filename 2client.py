import socket

client = socket.socket()
client.connect(("localhost", 12345))

name = input("Enter your name: ")

client.send(name.encode())

message = client.recv(1024).decode()
print(message)

client.close()