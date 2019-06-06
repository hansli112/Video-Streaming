import socket

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host_ip, 8080)) # use port 8080 as our listening port
server.listen(0) # can support only one connection simultaneously (can increase the number of clients in the future)

client, address = server.accept()

""" lots of TODO """

client.close()
server.close()
