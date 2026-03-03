import xmlrpc.client 

server = xmlrpc.client.ServerProxy('http://localhost:9000') 

print (" add (2,3) = %s" % str(server.add(2,3))) 
print (" subtract (3,2) = %s" % str(server.subtract(3,2))) 
print (" multiply (2,3) = %s" % str(server.multiply(3,2))) 
print (" divide (3,2) = %s" % str(server.divide(3,2))) 