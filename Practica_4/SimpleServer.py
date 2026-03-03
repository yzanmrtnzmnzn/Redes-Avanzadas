import xmlrpc.server 

def add(x, y): 
    return x + y 
 
def subtract(x, y): 
    return x - y 
 
def multiply(x, y): 
    return x * y 
 
def divide(x, y): 
    return x // y 

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 9000), logRequests=False) 
print("Listening on port 9000...") 

server.register_function(add, 'add') 
server.register_function(subtract, 'subtract') 
server.register_function(multiply, 'multiply') 
server.register_function(divide, 'divide') 

server.serve_forever() 