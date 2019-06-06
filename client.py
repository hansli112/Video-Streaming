import socket

print("ready for connection, please enter the IP address and port number of server")
print("\"usage: < server IP > < port number >\"")

address = input().strip().split()
address = (address[0], int(address[1]))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

""" lots of TODO """

client.close()
