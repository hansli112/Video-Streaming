import socket
import os

print("ready for connection, please enter the IP address and port number of server")
print("\"usage: < server IP > < port number >\"")

address = input().strip().split()
address = (address[0], int(address[1]))

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(address)

""" lots of TODO """
browser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
browser.bind(('',80))
#browser.bind = (address[0],8096)
browser.listen(5)
browser.setblocking(1)

askfile = ""
check = 0

while 1:
    (web,web_address) = browser.accept()
    message_browser = web.recv(1024).decode("utf-8")
    if (len(message_browser) != 0):
        print(message_browser)
        filename = message_browser.split()[1]
        print(filename)
        f = open(filename[1:])
        inidata = f.read()
        outputdata = inidata.split()
        print(outputdata)
        web.send(outputdata[0].encode("utf-8"))

        askfile = outputdata[5].split("\"")
        askfile = askfile[1]
        print(askfile)
        outputdata[5] = "src=" + os.getcwd() + "\\" + askfile
        print(outputdata[5])

        # send HTTP status to client
        web.send("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /><head>".encode("utf-8"))
        outputdata[2] = outputdata[2] + " " + outputdata[3] + ' ' + outputdata[4] + " " + outputdata[5] + " " + outputdata[6] + " " + outputdata[7] + " " + outputdata[8]
        web.send("<link rel=\"icon\" href=\"data:;base64,=\"></head>".encode("utf-8"))
        del outputdata[3:8]
        for i in range(1, len(outputdata)):
            web.send(outputdata[i].encode("utf-8"))
        web.send("\r\n".encode("utf-8"))
        check = 1
        
        




#client.close()
