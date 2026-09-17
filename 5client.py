import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = server.multiply(a, b)

print("Result:", result)