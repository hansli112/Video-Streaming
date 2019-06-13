from cv2 import cv2
import numpy as np
import socket
import sys
import pickle
import struct 
import threading

###為了方便觀察，讓uploader端有自己的撥放器
###此撥放器與網路無關，單純撥放，故以一個thread處理
def display():
    pause = 0
    while True:
        ret,frame=cap.read()
        key = cv2.waitKey(10)
        if (key == 27) or (key == 113):
            pass #break 
        if key == 112:
            pause += 1
            pause %= 2
    sys.exit()

cap=cv2.VideoCapture(0)                 ###開啟攝影機
###聯網
HOST = input("請輸入想連結的IP:")
uploader=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
uploader.connect((HOST,8089))
###做出一個thread
t = threading.Thread(target = display)
t.start()
while True:
    ret,frame=cap.read()                ###讀資料
    data = pickle.dumps(frame)          
    uploader.sendall(struct.pack("L", len(data))+data)  ###送出
    if t.is_alive() == 0:           ###因為只有thread那邊能收鍵盤的I/O
        break                       ###所以要是thread掛了就停止
    
