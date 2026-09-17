from xmlrpc.server import SimpleXMLRPCServer

def multiply(a, b):
    return a * b

server = SimpleXMLRPCServer(("localhost", 8000))

server.register_function(multiply, "multiply")

print("XML-RPC Server is running...")
server.serve_forever()