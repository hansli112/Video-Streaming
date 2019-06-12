from cv2 import cv2
import numpy as np
import socket
import sys
import pickle
import struct 
####大致上與server相同
watcher=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
watcher.connect(('localhost',8080))
data = b''
payload_size = struct.calcsize("L") 
pause = 0
while True:
    while len(data) < payload_size:
        data += watcher.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += watcher.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    
    frame=pickle.loads(frame_data)

    if pause == 0:
        cv2.imshow('client_frame',frame)
    key = cv2.waitKey(10)
    if (key == 27) or (key == 113):
        break 
    if key == 112:
        pause += 1
        pause %= 2
    