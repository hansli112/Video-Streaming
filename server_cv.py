import socket
import sys
from cv2 import cv2
import pickle
import numpy as np
import struct 

HOST=''
PORT=8089
PORT2 = 8080
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')
toc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
toc.bind((HOST,PORT2))
toc.listen(10)
conn,addr=s.accept()
print("uploader ready")
conn2,addr2 = toc.accept()
print("client ready")

data = b''
payload_size = struct.calcsize("L") 
while True:
    while len(data) < payload_size:
        tmp_data = conn.recv(4096)
        conn2.send(tmp_data)
        data += tmp_data
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    while len(data) < msg_size:
        tmp_data = conn.recv(4096)
        conn2.send(tmp_data)
        data += tmp_data
    frame_data = data[:msg_size]
    data = data[msg_size:]
    
    
    frame=pickle.loads(frame_data)
    cv2.imshow('server_frame',frame)

    key = cv2.waitKey(10)
    if (key == 27) or (key == 113):
        break

cv2.destroyAllWindows()