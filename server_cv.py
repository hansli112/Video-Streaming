import socket
import sys
from cv2 import cv2
import pickle
import numpy as np
import struct 

#設定uploader的socket
HOST=''
PORT=8089
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')
s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')
#
#設定clinet的socket
PORT2 = 8080
toc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
toc.bind((HOST,PORT2))
toc.listen(10)
#
#準備連線
conn,addr=s.accept()
print("uploader ready")
conn2,addr2 = toc.accept()
print("client ready")
#
data = b''                    #設定buffer為b
payload_size = struct.calcsize("L") #設定上限
pause = 0                           #暫停用

#以下是連線時的處理
while True:
    ###收uploader傳來的資料，並傳送給client
    while len(data) < payload_size:          ###裝一定量在處理
        tmp_data = conn.recv(4096)
        conn2.send(tmp_data)
        data += tmp_data
    ###

    ###以下解碼
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    ###

    ###同上
    while len(data) < msg_size:
        tmp_data = conn.recv(4096)
        conn2.send(tmp_data)
        data += tmp_data
    ###

    ###終於獲得資料
    frame_data = data[:msg_size]
    data = data[msg_size:]
    
    
    frame=pickle.loads(frame_data)
    ###以下是播放
    if pause == 0:
            cv2.imshow('server_frame',frame)
    key = cv2.waitKey(10)
    if (key == 27) or (key == 113):
        break 
    if key == 112:
        pause += 1
        pause %= 2

cv2.destroyAllWindows()            ###關掉全部的視窗