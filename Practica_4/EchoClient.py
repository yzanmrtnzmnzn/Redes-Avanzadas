import xmlrpc.client 
 
server = xmlrpc.client.ServerProxy('http://localhost:9000') 
print (server.ping()) 
print (server.echo("HOLA")) 