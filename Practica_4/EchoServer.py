from xmlrpc.server import SimpleXMLRPCServer 
 
def echo(v): 
    " Devuelve el mismo valor después de esperar un tiempo determinado" 
    return v 
 
def ping (): 
    "devuelve TRUE" 
    return "TRUE" 
 
server = SimpleXMLRPCServer(("localhost", 9000)) 
#server.register_multicall_functions() 
server.register_function(echo, "echo") 
server.register_function(ping, "ping") 
 
try: 
    print('Use Control-C to exit') 
    server.serve_forever() 
except KeyboardInterrupt: 
    print('Exiting') 
 
